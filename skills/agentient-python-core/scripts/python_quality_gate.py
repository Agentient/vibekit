#!/usr/bin/env python3
"""
Python Quality Gate Script for agentient-python-core plugin.

This script runs as a PostToolUse hook to enforce code quality standards:
- Ruff linting and formatting checks
- mypy strict type checking

Exit Codes:
  0: All quality checks passed
  2: Quality checks failed (blocks Claude Code with feedback to stderr)
  1: Script error (non-blocking)
"""

import sys
import json
import subprocess
import os
from pathlib import Path
from typing import Any


# --- Configuration ---
PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
CACHE_DIR = PROJECT_ROOT / ".python_quality_cache"
CACHE_TTL_SECONDS = 3600  # 1 hour

# Quality checks to run
RUFF_CHECK_CMD = ["ruff", "check", "--format=json"]
RUFF_FORMAT_CMD = ["ruff", "format", "--check"]
MYPY_CMD = ["mypy", "--strict", "--no-error-summary"]


def fail(message: str) -> None:
    """Print error message to stderr and exit with code 2 (blocking)."""
    print(message, file=sys.stderr)
    sys.exit(2)


def read_stdin_json() -> dict[str, Any]:
    """Read and parse JSON from stdin."""
    try:
        return json.load(sys.stdin)
    except json.JSONDecodeError:
        # If no stdin or invalid JSON, exit gracefully
        sys.exit(0)


def get_file_path(data: dict[str, Any]) -> Path | None:
    """Extract file path from hook data."""
    tool_input = data.get("tool_input", {})
    file_path_str = tool_input.get("file_path")

    if not file_path_str:
        return None

    # Only check Python files
    if not file_path_str.endswith(".py"):
        return None

    file_path = PROJECT_ROOT / file_path_str
    if not file_path.exists():
        return None

    return file_path


def run_command(cmd: list[str], file_path: Path) -> tuple[int, str, str]:
    """
    Run a command and capture output.

    Returns:
        (exit_code, stdout, stderr)
    """
    try:
        result = subprocess.run(
            cmd + [str(file_path)],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
            timeout=30
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out after 30 seconds"
    except FileNotFoundError:
        return 1, "", f"Command not found: {cmd[0]}"
    except Exception as e:
        return 1, "", f"Error running command: {e}"


def check_ruff_linting(file_path: Path) -> list[str]:
    """
    Run Ruff linting check.

    Returns:
        List of error messages (empty if no errors)
    """
    returncode, stdout, stderr = run_command(RUFF_CHECK_CMD, file_path)

    if returncode != 0 and stdout:
        try:
            findings = json.loads(stdout)
            if findings:
                errors = []
                for finding in findings:
                    code = finding.get("code", "???")
                    message = finding.get("message", "Unknown error")
                    location = finding.get("location", {})
                    row = location.get("row", "?")
                    col = location.get("column", "?")
                    errors.append(
                        f"  Line {row}:{col} - [{code}] {message}"
                    )
                return errors
        except json.JSONDecodeError:
            return [f"  Failed to parse Ruff output: {stdout[:200]}"]

    return []


def check_ruff_formatting(file_path: Path) -> str | None:
    """
    Run Ruff formatting check.

    Returns:
        Error message if formatting issues found, None otherwise
    """
    returncode, stdout, stderr = run_command(RUFF_FORMAT_CMD, file_path)

    if returncode != 0:
        return "  File is not formatted correctly. Run 'ruff format <file>' to fix."

    return None


def check_mypy_types(file_path: Path) -> list[str]:
    """
    Run mypy strict type checking.

    Returns:
        List of error messages (empty if no errors)
    """
    returncode, stdout, stderr = run_command(MYPY_CMD, file_path)

    if returncode != 0:
        # Parse mypy output (not JSON, but structured text)
        errors = []
        output = stdout + stderr
        for line in output.strip().split('\n'):
            if "error:" in line.lower():
                # Remove file path prefix for cleaner output
                line = line.replace(str(file_path) + ":", "Line ")
                errors.append(f"  {line}")

        return errors if errors else [f"  mypy check failed (exit code {returncode})"]

    return []


def run_quality_checks(file_path: Path) -> None:
    """
    Run all quality checks on a Python file.

    Exits with code 2 (blocking) if any checks fail.
    """
    errors = []

    # 1. Ruff Linting
    lint_errors = check_ruff_linting(file_path)
    if lint_errors:
        errors.append("❌ RUFF LINTING ERRORS:")
        errors.extend(lint_errors)

    # 2. Ruff Formatting
    format_error = check_ruff_formatting(file_path)
    if format_error:
        errors.append("❌ RUFF FORMATTING ERROR:")
        errors.append(format_error)

    # 3. mypy Type Checking
    type_errors = check_mypy_types(file_path)
    if type_errors:
        errors.append("❌ MYPY TYPE CHECKING ERRORS:")
        errors.extend(type_errors)

    # If any errors, fail with blocking exit code
    if errors:
        error_message = (
            f"CODE_QUALITY_FAILURE: The Python file '{file_path.name}' failed quality checks.\n\n"
            + "\n".join(errors)
            + "\n\n"
            + "Please fix these issues before proceeding:\n"
            + "  1. Run 'ruff check --fix <file>' to auto-fix linting issues\n"
            + "  2. Run 'ruff format <file>' to fix formatting\n"
            + "  3. Add missing type annotations for mypy errors\n"
        )
        fail(error_message)

    # All checks passed
    sys.exit(0)


def main() -> None:
    """Main entry point for quality gate script."""
    # Read hook data from stdin
    data = read_stdin_json()

    # Extract file path
    file_path = get_file_path(data)

    # If no Python file, exit successfully
    if not file_path:
        sys.exit(0)

    # Run quality checks
    run_quality_checks(file_path)


if __name__ == "__main__":
    main()
