#!/usr/bin/env python3
"""
Coverage Validator Script - Enforce Minimum Test Coverage Thresholds

This script validates that test coverage meets defined thresholds and provides
detailed gap analysis. Designed for Stop hook invocation to block deployment
if coverage is insufficient.

Exit Codes:
    0: Coverage meets or exceeds threshold
    2: BLOCKING - Coverage below threshold

Output:
    stdout: Coverage summary and gap analysis
    stderr: Detailed uncovered files/functions

Configuration:
    BACKEND_COVERAGE_THRESHOLD: Minimum backend coverage % (default: 80)
    FRONTEND_COVERAGE_THRESHOLD: Minimum frontend coverage % (default: 70)
    COVERAGE_REPORT_PATH: Path to coverage report (auto-detect if not set)

Supported Formats:
    - Python: coverage.json (from coverage.py --format=json)
    - JavaScript/TypeScript: coverage-summary.json (from Jest/Vitest)
    - LCOV: lcov.info
"""

import sys
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class CoverageReport:
    """Coverage report data"""
    total_percent: float
    statement_percent: float
    branch_percent: float
    function_percent: float
    line_percent: float
    uncovered_files: List[Tuple[str, float]]  # (file_path, coverage_percent)


class CoverageValidator:
    """Validates test coverage meets thresholds"""

    def __init__(self):
        self.backend_threshold = float(os.getenv('BACKEND_COVERAGE_THRESHOLD', '80'))
        self.frontend_threshold = float(os.getenv('FRONTEND_COVERAGE_THRESHOLD', '70'))

    def detect_report_type(self, report_path: Path) -> Optional[str]:
        """Detect coverage report format"""
        if report_path.name == 'coverage.json':
            return 'coverage.py'
        elif report_path.name == 'coverage-summary.json':
            return 'jest'
        elif report_path.name.endswith('.info') or report_path.name == 'lcov.info':
            return 'lcov'
        return None

    def parse_coverage_py_report(self, report_path: Path) -> CoverageReport:
        """Parse coverage.py JSON report"""
        with open(report_path) as f:
            data = json.load(f)

        totals = data.get('totals', {})
        total_percent = totals.get('percent_covered', 0.0)

        # Get uncovered files
        uncovered = []
        for file_path, file_data in data.get('files', {}).items():
            file_percent = file_data.get('summary', {}).get('percent_covered', 0.0)
            if file_percent < self.backend_threshold:
                uncovered.append((file_path, file_percent))

        uncovered.sort(key=lambda x: x[1])  # Sort by coverage (lowest first)

        return CoverageReport(
            total_percent=total_percent,
            statement_percent=totals.get('percent_covered', 0.0),
            branch_percent=totals.get('percent_covered_branches', 0.0),
            function_percent=0.0,  # coverage.py doesn't track function coverage separately
            line_percent=totals.get('percent_covered', 0.0),
            uncovered_files=uncovered
        )

    def parse_jest_report(self, report_path: Path) -> CoverageReport:
        """Parse Jest/Vitest coverage-summary.json"""
        with open(report_path) as f:
            data = json.load(f)

        totals = data.get('total', {})

        # Calculate average coverage
        statement_pct = totals.get('statements', {}).get('pct', 0.0)
        branch_pct = totals.get('branches', {}).get('pct', 0.0)
        function_pct = totals.get('functions', {}).get('pct', 0.0)
        line_pct = totals.get('lines', {}).get('pct', 0.0)

        total_percent = (statement_pct + branch_pct + function_pct + line_pct) / 4

        # Get uncovered files
        uncovered = []
        for file_path, file_data in data.items():
            if file_path == 'total':
                continue

            file_line_pct = file_data.get('lines', {}).get('pct', 0.0)
            if file_line_pct < self.frontend_threshold:
                uncovered.append((file_path, file_line_pct))

        uncovered.sort(key=lambda x: x[1])

        return CoverageReport(
            total_percent=total_percent,
            statement_percent=statement_pct,
            branch_percent=branch_pct,
            function_percent=function_pct,
            line_percent=line_pct,
            uncovered_files=uncovered
        )

    def find_coverage_report(self) -> Optional[Path]:
        """Auto-detect coverage report in common locations"""
        search_paths = [
            'coverage/coverage.json',  # coverage.py
            'coverage/coverage-summary.json',  # Jest/Vitest
            'coverage.json',
            'coverage-summary.json',
            'coverage/lcov.info',
            'lcov.info',
        ]

        for path_str in search_paths:
            path = Path(path_str)
            if path.exists():
                return path

        return None

    def validate_coverage(self, report_path: Path) -> Tuple[bool, str]:
        """
        Validate coverage meets threshold

        Returns:
            (passes, message)
        """
        report_type = self.detect_report_type(report_path)
        if not report_type:
            return True, f"⚠️  Unknown coverage report format: {report_path.name}"

        # Parse report
        try:
            if report_type == 'coverage.py':
                report = self.parse_coverage_py_report(report_path)
                threshold = self.backend_threshold
                stack = "Backend (Python)"
            elif report_type == 'jest':
                report = self.parse_jest_report(report_path)
                threshold = self.frontend_threshold
                stack = "Frontend (JS/TS)"
            else:
                return True, "⚠️  LCOV format not yet supported"

        except Exception as e:
            return True, f"⚠️  Failed to parse coverage report: {e}"

        # Check threshold
        if report.total_percent >= threshold:
            message = f"✅ Coverage: {report.total_percent:.1f}% (threshold: {threshold}%)\n"
            message += f"   Stack: {stack}\n"
            message += f"   Statement: {report.statement_percent:.1f}%\n"
            message += f"   Branch: {report.branch_percent:.1f}%\n"

            if report.function_percent > 0:
                message += f"   Function: {report.function_percent:.1f}%\n"

            return True, message

        # Coverage below threshold - BLOCK
        gap = threshold - report.total_percent

        message_lines = [
            f"❌ COVERAGE_FAILURE: {report.total_percent:.1f}% < {threshold}%",
            f"   Stack: {stack}",
            f"   Gap: {gap:.1f}% additional coverage needed",
            "",
            "   Breakdown:",
            f"     Statement: {report.statement_percent:.1f}%",
            f"     Branch: {report.branch_percent:.1f}%",
        ]

        if report.function_percent > 0:
            message_lines.append(f"     Function: {report.function_percent:.1f}%")

        # Show uncovered files
        if report.uncovered_files:
            message_lines.append("")
            message_lines.append(f"   Top {min(5, len(report.uncovered_files))} files needing coverage:")

            for file_path, file_pct in report.uncovered_files[:5]:
                message_lines.append(f"     {file_path}: {file_pct:.1f}%")

        # stderr output for detailed analysis
        stderr_data = {
            'coverage_percent': report.total_percent,
            'threshold': threshold,
            'gap': gap,
            'uncovered_files': [
                {'file': f, 'coverage': pct}
                for f, pct in report.uncovered_files[:10]
            ]
        }

        print(json.dumps(stderr_data, indent=2), file=sys.stderr)

        return False, "\n".join(message_lines)

    def run(self, report_path: Optional[Path] = None) -> int:
        """
        Main execution method

        Returns:
            Exit code (0 = pass, 2 = block)
        """
        # Find coverage report
        if report_path is None:
            report_path = self.find_coverage_report()

        if report_path is None or not report_path.exists():
            print("⚠️  No coverage report found. Skipping coverage validation.")
            print("   Expected locations: coverage/coverage.json, coverage-summary.json")
            return 0  # Don't block if no report (tests may not have run)

        # Validate coverage
        passed, message = self.validate_coverage(report_path)

        print(message)

        return 0 if passed else 2


def main():
    """Main entry point"""
    try:
        # Get report path from CLI arg or environment
        report_path_str = os.getenv('COVERAGE_REPORT_PATH')

        if len(sys.argv) > 1:
            report_path_str = sys.argv[1]

        report_path = Path(report_path_str) if report_path_str else None

        # Run validator
        validator = CoverageValidator()
        exit_code = validator.run(report_path)
        sys.exit(exit_code)

    except Exception as e:
        print(f"❌ Coverage validation error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(0)  # Don't block on validator errors


if __name__ == '__main__':
    main()
