#!/usr/bin/env python3
"""
Quality Gate Script - Multi-Language Code Quality Validator

This script provides deterministic, blocking quality enforcement for Python and
TypeScript/JavaScript code. It is designed to be invoked as a PostToolUse hook
after file writes, ensuring code meets quality standards before proceeding.

Exit Codes:
    0: All quality checks passed
    1: Non-blocking warning (reserved for future use)
    2: BLOCKING - Quality violations found, prevents execution

Output:
    stdout: Human-readable summary for LLM context
    stderr: JSON-formatted violations for machine parsing

Dependencies:
    Python: ruff, mypy
    TypeScript/JS: eslint, typescript (tsc)

Usage:
    # Via stdin (hook invocation)
    echo '{"tool_input": {"file_path": "/path/to/file.py"}}' | python3 quality_gate.py

    # Direct CLI
    python3 quality_gate.py /path/to/file.py
"""

import sys
import json
import subprocess
import hashlib
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, asdict


@dataclass
class Violation:
    """Represents a code quality violation"""
    file: str
    line: int
    column: int
    rule: str
    message: str
    severity: str  # ERROR, WARNING, INFO
    tool: str  # ruff, mypy, eslint, tsc


class QualityGate:
    """Multi-language quality gate validator"""

    # File content cache (30-minute TTL)
    CACHE_TTL = 1800  # seconds
    _cache: Dict[str, Tuple[float, List[Violation]]] = {}

    LANGUAGE_MAP = {
        '.py': 'python',
        '.ts': 'typescript',
        '.tsx': 'typescript',
        '.js': 'javascript',
        '.jsx': 'javascript',
    }

    def __init__(self):
        self.violations: List[Violation] = []

    def detect_language(self, file_path: Path) -> Optional[str]:
        """Detect programming language from file extension"""
        return self.LANGUAGE_MAP.get(file_path.suffix)

    def get_file_hash(self, file_path: Path) -> str:
        """Calculate file content hash for caching"""
        try:
            content = file_path.read_bytes()
            return hashlib.sha256(content).hexdigest()
        except Exception:
            return ""

    def check_cache(self, file_path: Path) -> Optional[List[Violation]]:
        """Check if violations are cached and still valid"""
        file_hash = self.get_file_hash(file_path)
        if not file_hash:
            return None

        cache_key = str(file_path)
        if cache_key in self._cache:
            cached_time, cached_violations = self._cache[cache_key]
            if time.time() - cached_time < self.CACHE_TTL:
                return cached_violations

        return None

    def update_cache(self, file_path: Path, violations: List[Violation]):
        """Update cache with new violations"""
        cache_key = str(file_path)
        self._cache[cache_key] = (time.time(), violations)

    def run_python_checks(self, file_path: Path) -> List[Violation]:
        """Run Ruff and mypy checks on Python file"""
        violations = []

        # Ruff lint check
        try:
            result = subprocess.run(
                ['ruff', 'check', '--output-format=json', str(file_path)],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.stdout:
                try:
                    ruff_output = json.loads(result.stdout)
                    for item in ruff_output:
                        violations.append(Violation(
                            file=item.get('filename', str(file_path)),
                            line=item.get('location', {}).get('row', 0),
                            column=item.get('location', {}).get('column', 0),
                            rule=item.get('code', 'UNKNOWN'),
                            message=item.get('message', ''),
                            severity='ERROR' if item.get('code', '').startswith('E') else 'WARNING',
                            tool='ruff'
                        ))
                except json.JSONDecodeError:
                    pass

        except subprocess.TimeoutExpired:
            violations.append(Violation(
                file=str(file_path),
                line=0,
                column=0,
                rule='TIMEOUT',
                message='Ruff check timed out after 30 seconds',
                severity='ERROR',
                tool='ruff'
            ))
        except FileNotFoundError:
            violations.append(Violation(
                file=str(file_path),
                line=0,
                column=0,
                rule='MISSING_TOOL',
                message='Ruff not installed. Install with: pip install ruff',
                severity='ERROR',
                tool='ruff'
            ))

        # Ruff format check
        try:
            result = subprocess.run(
                ['ruff', 'format', '--check', str(file_path)],
                capture_output=True,
                text=True,
                timeout=15
            )

            if result.returncode != 0:
                violations.append(Violation(
                    file=str(file_path),
                    line=0,
                    column=0,
                    rule='FORMAT',
                    message='File is not formatted. Run: ruff format',
                    severity='WARNING',
                    tool='ruff'
                ))

        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass  # Format check is optional

        # mypy type check
        try:
            result = subprocess.run(
                ['mypy', '--show-column-numbers', '--show-error-codes', str(file_path)],
                capture_output=True,
                text=True,
                timeout=45
            )

            if result.returncode != 0 and result.stdout:
                # Parse mypy output (format: file:line:col: error: message [code])
                for line in result.stdout.strip().split('\n'):
                    if ':' in line and 'error:' in line:
                        parts = line.split(':', 3)
                        if len(parts) >= 4:
                            try:
                                line_num = int(parts[1])
                                col_num = int(parts[2]) if parts[2].strip().isdigit() else 0
                                message_part = parts[3].strip()

                                # Extract error code if present
                                code = 'TYPE'
                                if '[' in message_part and ']' in message_part:
                                    code = message_part[message_part.rfind('[')+1:message_part.rfind(']')]
                                    message_part = message_part[:message_part.rfind('[')].strip()

                                violations.append(Violation(
                                    file=str(file_path),
                                    line=line_num,
                                    column=col_num,
                                    rule=code,
                                    message=message_part.replace('error:', '').strip(),
                                    severity='ERROR',
                                    tool='mypy'
                                ))
                            except (ValueError, IndexError):
                                continue

        except subprocess.TimeoutExpired:
            violations.append(Violation(
                file=str(file_path),
                line=0,
                column=0,
                rule='TIMEOUT',
                message='mypy check timed out after 45 seconds',
                severity='WARNING',
                tool='mypy'
            ))
        except FileNotFoundError:
            # mypy is optional, don't fail if not installed
            pass

        return violations

    def run_typescript_checks(self, file_path: Path) -> List[Violation]:
        """Run ESLint and TypeScript compiler checks"""
        violations = []

        # ESLint check
        try:
            result = subprocess.run(
                ['eslint', '--format=json', str(file_path)],
                capture_output=True,
                text=True,
                timeout=30
            )

            if result.stdout:
                try:
                    eslint_output = json.loads(result.stdout)
                    for file_result in eslint_output:
                        for message in file_result.get('messages', []):
                            violations.append(Violation(
                                file=file_result.get('filePath', str(file_path)),
                                line=message.get('line', 0),
                                column=message.get('column', 0),
                                rule=message.get('ruleId', 'UNKNOWN'),
                                message=message.get('message', ''),
                                severity=message.get('severity', 1) == 2 and 'ERROR' or 'WARNING',
                                tool='eslint'
                            ))
                except json.JSONDecodeError:
                    pass

        except subprocess.TimeoutExpired:
            violations.append(Violation(
                file=str(file_path),
                line=0,
                column=0,
                rule='TIMEOUT',
                message='ESLint check timed out after 30 seconds',
                severity='ERROR',
                tool='eslint'
            ))
        except FileNotFoundError:
            violations.append(Violation(
                file=str(file_path),
                line=0,
                column=0,
                rule='MISSING_TOOL',
                message='ESLint not installed. Install with: npm install eslint',
                severity='ERROR',
                tool='eslint'
            ))

        # TypeScript compiler check (if .ts or .tsx)
        if file_path.suffix in ['.ts', '.tsx']:
            try:
                result = subprocess.run(
                    ['tsc', '--noEmit', '--pretty', 'false', str(file_path)],
                    capture_output=True,
                    text=True,
                    timeout=45
                )

                if result.returncode != 0 and result.stdout:
                    # Parse tsc output (format: file(line,col): error TS code: message)
                    for line in result.stdout.strip().split('\n'):
                        if '(' in line and ')' in line and 'error TS' in line:
                            try:
                                # Extract file, line, column, code, message
                                file_part, rest = line.split('(', 1)
                                pos_part, msg_part = rest.split(')', 1)
                                line_num, col_num = pos_part.split(',')

                                if 'error TS' in msg_part:
                                    error_code = msg_part[msg_part.find('TS'):msg_part.find(':', msg_part.find('TS'))]
                                    message = msg_part[msg_part.find(':', msg_part.find('TS'))+1:].strip()

                                    violations.append(Violation(
                                        file=file_part.strip(),
                                        line=int(line_num),
                                        column=int(col_num),
                                        rule=error_code,
                                        message=message,
                                        severity='ERROR',
                                        tool='tsc'
                                    ))
                            except (ValueError, IndexError):
                                continue

            except subprocess.TimeoutExpired:
                violations.append(Violation(
                    file=str(file_path),
                    line=0,
                    column=0,
                    rule='TIMEOUT',
                    message='TypeScript check timed out after 45 seconds',
                    severity='WARNING',
                    tool='tsc'
                ))
            except FileNotFoundError:
                # tsc is optional for .js files
                pass

        return violations

    def validate_file(self, file_path: Path) -> bool:
        """
        Validate a single file

        Returns:
            True if file passes all checks, False otherwise
        """
        if not file_path.exists():
            print(f"⚠️  File not found: {file_path}", file=sys.stderr)
            return True  # Don't block if file doesn't exist

        # Check cache first
        cached_violations = self.check_cache(file_path)
        if cached_violations is not None:
            self.violations.extend(cached_violations)
            return len(cached_violations) == 0

        # Detect language
        language = self.detect_language(file_path)
        if not language:
            # Unknown file type, skip validation
            return True

        # Run language-specific checks
        if language == 'python':
            file_violations = self.run_python_checks(file_path)
        else:  # typescript or javascript
            file_violations = self.run_typescript_checks(file_path)

        # Update cache
        self.update_cache(file_path, file_violations)

        # Add to overall violations
        self.violations.extend(file_violations)

        return len(file_violations) == 0

    def format_output(self) -> Tuple[str, str]:
        """
        Format violations for output

        Returns:
            (stdout_message, stderr_json)
        """
        if not self.violations:
            stdout = "✅ Quality gate passed: No violations found"
            stderr = ""
            return stdout, stderr

        # Count violations by severity
        errors = [v for v in self.violations if v.severity == 'ERROR']
        warnings = [v for v in self.violations if v.severity == 'WARNING']

        # Human-readable summary for stdout
        stdout_lines = [
            f"❌ QUALITY_GATE_FAILURE: {len(self.violations)} violation(s) found",
            f"   Errors: {len(errors)}",
            f"   Warnings: {len(warnings)}",
            ""
        ]

        # Group by tool
        by_tool = {}
        for v in self.violations:
            by_tool.setdefault(v.tool, []).append(v)

        for tool, tool_violations in sorted(by_tool.items()):
            stdout_lines.append(f"   {tool}: {len(tool_violations)} issue(s)")

        stdout = "\n".join(stdout_lines)

        # JSON output for stderr (machine-readable)
        stderr = json.dumps(
            [asdict(v) for v in self.violations],
            indent=2
        )

        return stdout, stderr

    def run(self, file_path: Path) -> int:
        """
        Main execution method

        Returns:
            Exit code (0 = pass, 2 = block)
        """
        passed = self.validate_file(file_path)

        stdout_msg, stderr_json = self.format_output()

        print(stdout_msg)

        if stderr_json:
            print(stderr_json, file=sys.stderr)

        return 0 if passed else 2


def main():
    """Main entry point"""
    try:
        # Try to read from stdin (hook invocation)
        if not sys.stdin.isatty():
            try:
                data = json.load(sys.stdin)
                file_path_str = data.get('tool_input', {}).get('file_path')

                if not file_path_str:
                    # Try content parameter (for Write tool)
                    file_path_str = data.get('tool_input', {}).get('file_path')

                if file_path_str:
                    file_path = Path(file_path_str)
                else:
                    print("⚠️  No file_path in stdin data", file=sys.stderr)
                    sys.exit(0)

            except json.JSONDecodeError:
                # Fallback to CLI arg
                if len(sys.argv) < 2:
                    print("Usage: quality_gate.py <file_path>", file=sys.stderr)
                    sys.exit(1)
                file_path = Path(sys.argv[1])

        else:
            # CLI invocation
            if len(sys.argv) < 2:
                print("Usage: quality_gate.py <file_path>", file=sys.stderr)
                sys.exit(1)
            file_path = Path(sys.argv[1])

        # Run quality gate
        gate = QualityGate()
        exit_code = gate.run(file_path)
        sys.exit(exit_code)

    except Exception as e:
        print(f"❌ Quality gate error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)  # Non-blocking error


if __name__ == '__main__':
    main()
