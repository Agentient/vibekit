---
name: type-hints-best-practices
description: |
  Type hints best practices with mypy strict mode for Python 3.13. Use this skill when writing type annotations, configuring mypy, or ensuring static type safety.
  PROACTIVELY use for: type annotations, mypy configuration, Generic types, Protocol definitions, TypeAlias, strict type checking.
  Keywords: type hints, mypy, typing, Generic, Protocol, TypeAlias, strict mode, type checking.
---

# Type Hints Best Practices with mypy Strict Mode

## Core Principles

**All Python code in Vibekit MUST pass mypy in strict mode** with zero errors. Type hints are not optional—they are a fundamental requirement for code quality and maintainability.

## Explicit Return Type Annotations

Every exported function must declare its return type:

```python
# ✅ REQUIRED: Explicit return types for all exported functions
def calculate_total(items: list[float]) -> float:
    """Calculate sum of items."""
    return sum(items)

def get_user_by_id(user_id: int) -> User | None:
    """Retrieve user or None if not found."""
    result = database.query(user_id)
    return result

def process_data(data: str) -> None:
    """Process data with no return value."""
    print(data.upper())

# ❌ FORBIDDEN: Implicit Any return type
def bad_function(x):  # Returns Any - rejected by strict mypy
    return x * 2

# ❌ FORBIDDEN: No return type annotation
def also_bad(x: int):  # Missing return type
    return x * 2

# ✅ GOOD: Explicit return type
def good_function(x: int) -> int:
    return x * 2
```

## Using Built-in Generic Types

Use built-in types for generic annotations (Python 3.9+):

```python
# ✅ REQUIRED: Use built-in generics
def process_items(items: list[str]) -> dict[str, int]:
    """Process items and return counts."""
    return {item: len(item) for item in items}

def merge_configs(
    config1: dict[str, any],
    config2: dict[str, any]
) -> dict[str, any]:
    """Merge two configuration dictionaries."""
    return {**config1, **config2}

def get_first_item(items: list[int]) -> int | None:
    """Get first item or None."""
    return items[0] if items else None

# ❌ FORBIDDEN: Legacy typing imports
from typing import List, Dict, Optional

def old_style(items: List[str]) -> Dict[str, int]:  # Don't use these!
    pass
```

## Type Aliases for Complex Types

Use the `type` statement for readable type aliases:

```python
# ✅ REQUIRED: Use type statement for type aliases (Python 3.12+)
type UserId = int
type UserData = dict[str, str | int | bool]
type ValidationResult = tuple[bool, str]

def validate_user(user_id: UserId, data: UserData) -> ValidationResult:
    """Validate user data."""
    if user_id < 0:
        return False, "Invalid user ID"
    return True, "Valid"

# For Python 3.9-3.11, use TypeAlias
from typing import TypeAlias

UserIdLegacy: TypeAlias = int
UserDataLegacy: TypeAlias = dict[str, str | int | bool]

# ❌ FORBIDDEN: Inline complex types
def process(
    data: dict[str, str | int | bool | list[dict[str, any]]]  # Too complex!
) -> tuple[bool, str, dict[str, any]]:
    pass

# ✅ GOOD: Named type alias
type ComplexData = dict[str, str | int | bool | list[dict[str, any]]]
type ProcessResult = tuple[bool, str, dict[str, any]]

def process(data: ComplexData) -> ProcessResult:
    pass
```

## Generic Types and Classes

Create reusable generic functions and classes:

```python
from typing import TypeVar, Generic

# ✅ REQUIRED: Use TypeVar for generic functions
T = TypeVar('T')

def get_first(items: list[T]) -> T | None:
    """Get first item from list, preserving type."""
    return items[0] if items else None

# Usage preserves types
first_int: int | None = get_first([1, 2, 3])  # Type: int | None
first_str: str | None = get_first(["a", "b"])  # Type: str | None

# Generic class
class Stack(Generic[T]):
    """Generic stack implementation."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Add item to stack."""
        self._items.append(item)

    def pop(self) -> T | None:
        """Remove and return top item."""
        return self._items.pop() if self._items else None

# Usage
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)

str_stack: Stack[str] = Stack()
str_stack.push("hello")
```

## Protocol for Structural Typing

Use Protocol to define interfaces without inheritance:

```python
from typing import Protocol

# ✅ REQUIRED: Use Protocol for structural subtyping
class Closable(Protocol):
    """Protocol for objects that can be closed."""

    def close(self) -> None:
        """Close the resource."""
        ...

class Serializable(Protocol):
    """Protocol for serializable objects."""

    def to_dict(self) -> dict[str, any]:
        """Convert to dictionary."""
        ...

def cleanup_resource(resource: Closable) -> None:
    """Clean up any closable resource."""
    resource.close()

# Any class with a close() method satisfies the protocol
class FileHandler:
    def close(self) -> None:
        print("Closing file")

class DatabaseConnection:
    def close(self) -> None:
        print("Closing connection")

# Both work with cleanup_resource
cleanup_resource(FileHandler())  # ✅ Works
cleanup_resource(DatabaseConnection())  # ✅ Works
```

## mypy Strict Mode Configuration

Configure mypy for maximum type safety:

```python
# pyproject.toml
[tool.mypy]
python_version = "3.13"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_any_generics = true
disallow_subclassing_any = true
disallow_untyped_calls = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

# For gradual typing of legacy code
[[tool.mypy.overrides]]
module = "legacy.module.*"
disallow_untyped_defs = false  # Temporarily disable for legacy
```

## Handling Third-Party Libraries Without Stubs

Deal with untyped third-party code:

```python
# ❌ BAD: Global ignore_missing_imports
[tool.mypy]
ignore_missing_imports = true  # Don't do this!

# ✅ GOOD: Install type stubs when available
# pip install types-requests types-redis

# ✅ GOOD: Per-module ignore when stubs don't exist
[[tool.mypy.overrides]]
module = "untyped_library.*"
ignore_missing_imports = true

# ✅ GOOD: Create custom stub file
# untyped_library.pyi
def some_function(arg: str) -> int: ...
class SomeClass:
    def method(self) -> None: ...
```

## Specific Error Code Ignores

When type ignore is necessary, use specific error codes:

```python
# ❌ FORBIDDEN: Bare type ignore
result = legacy_function()  # type: ignore  # Too broad!

# ✅ REQUIRED: Specific error code
result = legacy_function()  # type: ignore[no-any-return]

# ✅ REQUIRED: Inline type annotation when possible
result: dict[str, any] = legacy_function()  # Better than ignore

# Common error codes:
# [no-any-return]         - Function returns Any
# [attr-defined]          - Attribute not defined
# [arg-type]              - Wrong argument type
# [assignment]            - Type mismatch in assignment
# [override]              - Override signature mismatch
# [misc]                  - Miscellaneous errors
```

## Union Types with | Operator

Use the modern union syntax:

```python
# ✅ REQUIRED: Use | for union types
def process_value(value: str | int | float) -> str:
    """Handle multiple types."""
    return str(value)

def find_user(query: str) -> User | None:
    """Return User or None if not found."""
    result = database.find(query)
    return result

# ✅ REQUIRED: None always comes last in unions
def get_config(key: str) -> str | int | None:
    """Get configuration value."""
    return config.get(key)

# ❌ FORBIDDEN: Legacy Union and Optional
from typing import Union, Optional

def old_style(value: Union[str, int]) -> Optional[User]:  # Don't use
    pass

# ✅ GOOD: Modern style
def new_style(value: str | int) -> User | None:
    pass
```

## Literal Types for Specific Values

Use Literal for exact value matching:

```python
from typing import Literal

# ✅ REQUIRED: Use Literal for specific string/int values
def set_log_level(level: Literal["DEBUG", "INFO", "WARNING", "ERROR"]) -> None:
    """Set logging level to specific value."""
    logging.setLevel(level)

def get_status_code(status: Literal[200, 404, 500]) -> str:
    """Get status message for specific codes."""
    messages = {200: "OK", 404: "Not Found", 500: "Error"}
    return messages[status]

# Usage
set_log_level("DEBUG")  # ✅ OK
set_log_level("INFO")   # ✅ OK
set_log_level("TRACE")  # ❌ Type error: "TRACE" not in Literal
```

## TypedDict for Structured Dictionaries

Define exact dictionary structures:

```python
from typing import TypedDict

# ✅ REQUIRED: Use TypedDict for structured dicts
class UserDict(TypedDict):
    """Typed dictionary for user data."""
    id: int
    email: str
    username: str
    is_active: bool

def create_user(data: UserDict) -> User:
    """Create user from typed dict."""
    return User(
        id=data["id"],
        email=data["email"],
        username=data["username"],
        is_active=data["is_active"]
    )

# Usage
user_data: UserDict = {
    "id": 1,
    "email": "user@example.com",
    "username": "user",
    "is_active": True
}
user = create_user(user_data)

# ❌ Type error: missing required key
bad_data: UserDict = {"id": 1, "email": "user@example.com"}  # Missing username

# Optional keys
class PartialUserDict(TypedDict, total=False):
    """User dict with optional fields."""
    id: int  # Still required (would need NotRequired for truly optional)
    metadata: dict[str, str]  # Optional
```

## Any vs object

Use `object` instead of `Any` when possible:

```python
from typing import Any

# ❌ BAD: Any disables type checking
def log_anything(value: Any) -> None:
    print(str(value))  # No type safety

# ✅ GOOD: object is more precise
def log_value(value: object) -> None:
    """Log any object by converting to string."""
    print(str(value))  # object has __str__, so this is safe

# Any should only be used when truly dynamic
def dynamic_dispatch(operation: str, *args: Any) -> Any:
    """Truly dynamic operation dispatcher."""
    return getattr(operations, operation)(*args)
```

## Anti-Patterns to Avoid

### ❌ Missing Return Type Annotations
```python
# BAD: Implicit Any return
def calculate(x: int):  # Missing return type
    return x * 2

# GOOD: Explicit return type
def calculate(x: int) -> int:
    return x * 2
```

### ❌ Using Legacy typing Imports
```python
# BAD
from typing import List, Dict, Optional, Union

def process(items: List[str]) -> Optional[Dict[str, int]]:
    pass

# GOOD
def process(items: list[str]) -> dict[str, int] | None:
    pass
```

### ❌ Bare type: ignore Comments
```python
# BAD: Too broad
result = untypedFunction()  # type: ignore

# GOOD: Specific error code
result = untypedFunction()  # type: ignore[no-any-return]
```

### ❌ Global ignore_missing_imports
```python
# BAD: pyproject.toml
[tool.mypy]
ignore_missing_imports = true  # Disables too many checks

# GOOD: Per-module overrides
[[tool.mypy.overrides]]
module = "specific_untyped_lib.*"
ignore_missing_imports = true
```

### ❌ Any Instead of object
```python
# BAD: Disables type checking
def print_value(value: Any) -> None:
    print(value.upper())  # No type safety!

# GOOD: Use specific type
def print_value(value: str) -> None:
    print(value.upper())

# GOOD: Use object if truly any type
def print_value(value: object) -> None:
    print(str(value))  # Safe conversion
```

## Gradual Typing Strategy

Adopt strict typing incrementally for legacy code:

```python
# pyproject.toml - Gradual typing approach
[tool.mypy]
# Global strict mode
strict = true

# Disable strict for legacy modules
[[tool.mypy.overrides]]
module = "legacy.old_module.*"
disallow_untyped_defs = false
disallow_incomplete_defs = false

# Re-enable strict for new code in legacy area
[[tool.mypy.overrides]]
module = "legacy.new_feature.*"
disallow_untyped_defs = true

# Strategy:
# 1. Enable strict=true globally
# 2. Disable specific checks for legacy code
# 3. Gradually remove overrides as code is updated
```

## Running mypy in CI/CD

Ensure type safety in continuous integration:

```bash
# Run mypy with strict mode
mypy src/

# Fail CI if mypy finds errors
# (exit code non-zero on errors)

# Generate type coverage report
mypy --html-report ./mypy-report src/

# Check specific files only
mypy src/module.py src/another.py

# Show error context
mypy --show-error-context src/
```

## When to Use This Skill

Activate this skill when:
- Writing new Python modules with type hints
- Configuring mypy for a project
- Debugging type errors
- Implementing generic types or protocols
- Migrating untyped code to typed
- Setting up CI/CD type checking

## Integration Points

This skill is a **required dependency** for:
- All Python-based Vibekit plugins
- `pydantic-v2-strict` - Type hints are foundational for Pydantic
- `python-code-quality-automation` - mypy is part of quality gates

## Related Resources

For additional information:
- mypy Documentation: https://mypy.readthedocs.io/
- Python typing Documentation: https://docs.python.org/3/library/typing.html
- Type Hints Best Practices: https://typing.python.org/en/latest/reference/best_practices.html
