# Run Quality Check

Execute comprehensive code quality checks using Ruff and mypy to ensure code meets Vibekit standards.

## Task

Run automated quality checks on Python code to verify it meets all quality standards before committing.

### Quality Checks Performed

1. **Ruff Linting**: Check for code quality issues, bugs, and style violations
2. **Ruff Formatting**: Verify code follows Black-compatible formatting
3. **mypy Type Checking**: Ensure strict type safety with zero errors

### Quality Standards

All code MUST pass these checks with zero errors:

1. **Ruff Check**:
   - Zero linting warnings
   - All imports organized (stdlib → third-party → local)
   - No unused imports or variables
   - Proper line length (default 88 chars)
   - No common bugs (undefined names, etc.)

2. **Ruff Format**:
   - Follows Black formatting style
   - Consistent indentation (4 spaces)
   - Proper spacing around operators
   - Correct quote style

3. **mypy Strict**:
   - All functions have type annotations
   - No implicit `Any` types
   - All return types declared
   - No missing imports or stubs

### Running Quality Checks

**Check Specific File**:
```bash
/run-quality-check src/module.py
```

**Check Entire Directory**:
```bash
/run-quality-check src/
```

**Check with Auto-Fix**:
```bash
/run-quality-check src/ --fix
```

### Command Execution

This command will execute the following:

```bash
# 1. Run Ruff linting
ruff check <path> [--fix]

# 2. Run Ruff formatting check
ruff format --check <path>

# 3. Run mypy type checking
mypy --strict <path>
```

### Expected Output

**✅ All Checks Pass**:
```
=== Ruff Linting ===
All checks passed!

=== Ruff Formatting ===
1 file left unchanged

=== mypy Type Checking ===
Success: no issues found in 1 source file

✅ Quality checks PASSED
```

**❌ Linting Errors**:
```
=== Ruff Linting ===
src/models.py:15:8: F401 'os' imported but unused
src/models.py:23:5: F841 Local variable 'result' is assigned but never used
src/services.py:45:1: E302 Expected 2 blank lines, found 1

Found 3 errors.
```

**❌ Formatting Errors**:
```
=== Ruff Formatting ===
Would reformat: src/models.py
1 file would be reformatted

Hint: Run 'ruff format src/models.py' to fix
```

**❌ Type Errors**:
```
=== mypy Type Checking ===
src/models.py:23: error: Function is missing a return type annotation  [no-untyped-def]
src/services.py:45: error: Returning Any from function declared to return "User"  [no-any-return]

Found 2 errors in 2 files (checked 5 source files)
```

### Auto-Fix Mode

Use `--fix` flag to automatically fix certain issues:

```bash
/run-quality-check src/ --fix
```

**What gets auto-fixed**:
- Unused imports removed
- Import order corrected
- Formatting applied
- Some simple linting issues

**What requires manual fixes**:
- Type annotations
- Logic errors
- Complex linting issues

### Configuration

Quality checks use project configuration from `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88
target-version = "py313"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "N",   # pep8-naming
    "UP",  # pyupgrade
]
ignore = []

[tool.mypy]
python_version = "3.13"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

### Integration with Quality Gate Hook

This command provides the same checks that run automatically via the PostToolUse hook. Running it manually lets you:

- Check code before committing
- Verify fixes before pushing
- Debug quality gate failures
- Ensure code meets standards

### Common Fixes

**Unused Import**:
```python
# ❌ Ruff error: F401
import os  # Imported but never used

# ✅ Fix: Remove unused import
# (ruff check --fix removes this automatically)
```

**Missing Type Annotation**:
```python
# ❌ mypy error: no-untyped-def
def process_data(data):
    return data.upper()

# ✅ Fix: Add type annotations
def process_data(data: str) -> str:
    return data.upper()
```

**Formatting Issue**:
```python
# ❌ Ruff format error
def func(x,y,z):
    result=x+y+z
    return result

# ✅ Fix: Run ruff format
def func(x, y, z):
    result = x + y + z
    return result
```

**Import Order**:
```python
# ❌ Ruff error: I001
from my_module import helper
import os
import sys

# ✅ Fix: Correct order (ruff check --fix does this)
import os
import sys

from my_module import helper
```

### Exit Codes

- **0**: All checks passed
- **1**: Errors found

### Example Usage Scenarios

**Before Committing**:
```bash
# Check all changes
/run-quality-check src/

# If errors, fix them
ruff check --fix src/
ruff format src/
# Add missing type annotations manually

# Verify fixes
/run-quality-check src/

# Commit when all checks pass
git add .
git commit -m "feat: add new feature"
```

**Debugging Hook Failure**:
```bash
# Quality gate hook blocked your code

# Run checks manually to see details
/run-quality-check src/module.py

# Fix issues
# Re-run to verify
```

**CI/CD Integration**:
```bash
# In CI pipeline
/run-quality-check src/

# Pipeline fails if exit code != 0
```

### Performance Notes

- **Ruff**: Very fast (~10-100x faster than alternatives)
- **mypy**: Can be slow for large codebases (use mypy daemon for development)
- **Caching**: Tools cache results for unchanged files

### When to Run

Run quality checks:
- ✅ Before every commit
- ✅ Before creating a pull request
- ✅ After resolving merge conflicts
- ✅ When quality gate hook fails
- ✅ After major refactoring

## Prompt

I need to run quality checks on `{path}`.

Please execute:
1. Ruff linting to check for code quality issues
2. Ruff formatting to verify style compliance
3. mypy type checking with strict mode

Report all errors found and suggest fixes. If `--fix` flag is provided, apply automatic fixes where possible.
