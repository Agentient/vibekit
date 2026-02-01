# Create Python Module

Generate a complete Python 3.13 module with Pydantic V2 models, following Vibekit standards.

## Task

You are tasked with creating a new Python module with the following requirements:

### Module Structure

Create the following file structure:

```
<module_name>/
├── __init__.py       # Public API exports
├── models.py         # Pydantic V2 data models
├── services.py       # Business logic
├── types.py          # Type aliases and protocols
└── exceptions.py     # Custom exceptions
```

### Quality Standards (MANDATORY)

All generated code MUST meet these standards:

1. **Type Safety**:
   - All functions have complete type annotations
   - Use Python 3.13 built-in generics: `list[T]`, `dict[K, V]`
   - Use union operator: `str | None` (not `Optional[str]`)
   - Pass `mypy --strict` with zero errors

2. **Pydantic V2 Strict Mode**:
   - All models use `model_config = ConfigDict(strict=True, frozen=True)`
   - Use `@field_validator` for validation (not V1 `@validator`)
   - Use `model_dump()`, `model_validate()` (not V1 methods)

3. **Documentation**:
   - All modules have module-level docstrings
   - All classes have docstrings
   - All exported functions have docstrings with parameters and return values

4. **Code Quality**:
   - Pass Ruff linting with zero warnings
   - Follow Black formatting style
   - Imports organized: stdlib → third-party → local

### Implementation Steps

1. **Invoke python-architect-agent**:
   - The architect will design the module structure
   - They will create Pydantic models with strict mode
   - They will define clear interfaces and type annotations

2. **Generate Files**:
   - Create `__init__.py` with `__all__` exports
   - Create `models.py` with Pydantic BaseModel definitions
   - Create `services.py` with business logic
   - Create `types.py` with type aliases using `type` keyword
   - Create `exceptions.py` with custom exception classes

3. **Quality Checks**:
   - Run `mypy --strict` on generated code
   - Run `ruff check` to verify linting
   - Run `ruff format --check` to verify formatting

### Example Usage

```bash
# User invokes the command
/create-module user_management

# Result: Creates user_management/ with:
# - models.py: UserSchema, UserCreate, UserUpdate (Pydantic V2)
# - services.py: create_user(), update_user(), get_user()
# - types.py: type UserId = int
# - exceptions.py: class UserNotFoundError(Exception)
# - __init__.py: Exports public API
```

### Validation

After generation, the module MUST:
- ✅ Pass `mypy --strict <module_name>` with zero errors
- ✅ Pass `ruff check <module_name>` with zero warnings
- ✅ Have no `Any` types except where explicitly required
- ✅ Use `ConfigDict(strict=True)` for all Pydantic models
- ✅ Be ready for test generation by testing-agent

## Prompt

I need to create a Python module called `{module_name}` that {description}.

Please use the python-architect-agent to design and implement a complete module following all Vibekit quality standards.
