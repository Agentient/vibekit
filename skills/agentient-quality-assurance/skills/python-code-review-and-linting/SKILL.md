# Python Code Review and Linting Skill

## Metadata (Tier 1)

**Keywords**: ruff, lint, refactor, security, anti-pattern, python review, mypy

**File Patterns**: *.py

**Modes**: code_review

---

## Instructions (Tier 2)

### Ruff Configuration

```toml
# pyproject.toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "B", "S", "I"]
ignore = ["E501"]  # Line too long (handled by formatter)

[tool.ruff.format]
quote-style = "double"
```

### Critical Security Rules (S prefix)

**S101**: Assert used (disabled in production)
```python
# ❌ Insecure
assert user.is_admin, "Not admin"  # Can be disabled with -O flag

# ✅ Secure
if not user.is_admin:
    raise PermissionError("Not admin")
```

**S105/S106**: Hardcoded secrets
```python
# ❌ Violation
password = "admin123"

# ✅ Fix
import os
password = os.getenv("PASSWORD")
```

**S301**: Unsafe pickle
```python
# ❌ Code execution risk
data = pickle.loads(user_input)

# ✅ Safe
import json
data = json.loads(user_input)
```

**S307**: Use of eval
```python
# ❌ Arbitrary code execution
result = eval(user_input)

# ✅ Safe
import ast
result = ast.literal_eval(user_input)  # Only literals
```

### Common Anti-Patterns (B prefix)

**B006**: Mutable default argument
```python
# ❌ Shared state bug
def add_item(item, items=[]):
    items.append(item)
    return items

# ✅ Fix
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

**B007**: Unused loop variable
```python
# ❌ Confusing
for i in range(10):
    do_something()  # 'i' not used

# ✅ Clear
for _ in range(10):
    do_something()
```

### mypy Type Errors

```python
# error: Argument 1 has incompatible type "str"; expected "int"
def process(x: int) -> int:
    return x * 2

process("5")  # ❌ Type error

# ✅ Fix
process(int("5"))
```

### Anti-Patterns

❌ Ignoring lint errors with # noqa
❌ Using basic exceptions (Exception, BaseException)
❌ Star imports (from module import *)
❌ Bare except clauses
