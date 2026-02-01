# agentient-python-core

**Foundational Python 3.13 Development Plugin for Vibekit Marketplace**

Version: 1.0.0
Author: Agentient Labs

---

## Overview

The `agentient-python-core` plugin establishes the foundational patterns and quality standards for all Python-based development in the Vibekit ecosystem. It provides comprehensive support for modern Python 3.13, Pydantic V2 strict mode data modeling, async/await patterns, pytest-based testing, and automated code quality enforcement.

This plugin is **the standard-setter** for Python development across the Vibekit marketplace. All dependent plugins (RAG engine, frontend BFF, quality assurance) inherit its patterns and quality requirements.

## Key Features

✅ **Python 3.13 Modern Patterns**: Built-in generics, union types, match/case, async/await
✅ **Pydantic V2 Strict Mode**: Type-safe data models with zero tolerance for type coercion
✅ **Comprehensive Testing**: pytest patterns with 80%+ coverage requirement
✅ **Automated Quality Gates**: Real-time code quality enforcement via hooks
✅ **Type Safety**: mypy strict mode compliance with zero errors
✅ **2 Specialized Agents**: Architecture design and testing automation
✅ **5 Knowledge Skills**: Progressive disclosure for efficient context management

## Plugin Components

### Agents (2)

#### 1. python-architect-agent
**Specialization**: System architecture and data modeling

**Use Cases**:
- Designing Python module structures
- Creating Pydantic V2 data models
- Establishing type-safe interfaces
- Selecting appropriate design patterns
- Async architecture decisions

**Invocation**:
```bash
# Automatically invoked for architecture tasks
"Design a user management system with Pydantic models"
```

**Quality Mandate**: Enforces strict type safety, Pydantic V2 patterns, and comprehensive documentation.

#### 2. testing-agent
**Specialization**: Test suite generation and coverage analysis

**Use Cases**:
- Creating pytest test suites
- Designing test fixtures and strategies
- Achieving 80%+ code coverage
- Testing async code
- Mocking external dependencies

**Invocation**:
```bash
# Use /create-test command or direct request
/create-test user_management
```

**Quality Mandate**: Ensures AAA pattern, proper fixture scoping, and comprehensive coverage.

### Skills (5)

All skills follow a 3-tier progressive disclosure model for token efficiency:
- **Tier 1**: Metadata (activation criteria)
- **Tier 2**: Instructions (core patterns and examples)
- **Tier 3**: Resources (on-demand deep reference)

#### 1. python-3-13-patterns
**Purpose**: Modern Python 3.13 language features and idioms

**Covers**:
- Built-in generics (`list[str]`, `dict[str, int]`)
- Union types with `|` operator
- Structural pattern matching (match/case)
- Async/await patterns
- Context managers and decorators
- Generators

**Token Budget**: ~2500 tokens (Tier 2)

#### 2. pydantic-v2-strict
**Purpose**: Pydantic V2 data modeling with strict mode enforcement

**Covers**:
- BaseModel with ConfigDict
- Strict mode (no type coercion)
- Field validators (V2 syntax)
- Model serialization (model_dump)
- Field aliasing for APIs
- ORM integration

**Token Budget**: ~2000 tokens (Tier 2)

**Critical**: This skill establishes data modeling standards for the entire Vibekit ecosystem.

#### 3. async-patterns
**Purpose**: Async/await with comprehensive error handling

**Covers**:
- Async functions with timeout and error handling
- Concurrent execution (asyncio.gather)
- Async context managers
- Task management and cancellation
- Retry logic with exponential backoff
- Rate limiting

**Token Budget**: ~2500 tokens (Tier 2)

#### 4. pytest-patterns
**Purpose**: Modern pytest test structure and strategies

**Covers**:
- AAA pattern (Arrange-Act-Assert)
- Fixture design and scoping
- Parametrized tests
- Mocking strategies
- Async test patterns
- Coverage configuration

**Token Budget**: ~2500 tokens (Tier 2)

#### 5. type-hints-best-practices
**Purpose**: Type hints and mypy strict mode compliance

**Covers**:
- Explicit return type annotations
- Built-in generic types
- Type aliases with `type` keyword
- Generic types and Protocol
- mypy strict configuration
- Handling third-party libraries

**Token Budget**: ~2500 tokens (Tier 2)

### Slash Commands (4)

#### /create-module
**Purpose**: Generate a complete Python module with Pydantic models

**Usage**:
```bash
/create-module user_management
```

**Creates**:
```
user_management/
├── __init__.py       # Public API exports
├── models.py         # Pydantic V2 models
├── services.py       # Business logic
├── types.py          # Type aliases
└── exceptions.py     # Custom exceptions
```

**Quality Checks**: mypy strict, Ruff linting, Ruff formatting

#### /create-test
**Purpose**: Generate comprehensive pytest test suite

**Usage**:
```bash
/create-test user_management
```

**Creates**:
```
tests/test_user_management/
├── conftest.py       # Shared fixtures
├── test_models.py    # Model validation tests
└── test_services.py  # Business logic tests
```

**Coverage Target**: 80%+ code coverage

#### /add-validator
**Purpose**: Add Pydantic V2 validator to existing model

**Usage**:
```bash
/add-validator User email
```

**Adds**: Field or model validator using Pydantic V2 syntax (@field_validator, @model_validator)

#### /run-quality-check
**Purpose**: Execute Ruff and mypy quality checks

**Usage**:
```bash
/run-quality-check src/module.py
/run-quality-check src/module.py --fix
```

**Checks**:
- Ruff linting (with optional auto-fix)
- Ruff formatting verification
- mypy strict type checking

### Quality Gate System

#### Hook Configuration
The plugin includes a PostToolUse hook that automatically validates all Python code changes.

**Configuration**: `hooks/hooks.json`
```json
{
  "PostToolUse": [
    {
      "matcher": "Write|Edit",
      "hooks": [{"type": "command", "command": "python3 .../python_quality_gate.py"}]
    }
  ]
}
```

#### Quality Gate Script
**Script**: `scripts/python_quality_gate.py`

**Checks Performed**:
1. **Ruff Linting**: Zero warnings required
2. **Ruff Formatting**: Black-compatible style
3. **mypy Strict**: Complete type annotations

**Exit Codes**:
- `0`: All checks passed
- `2`: Checks failed (blocks Claude Code, sends errors to stderr)

**Behavior**:
- Runs automatically after Write/Edit operations on `.py` files
- Blocks code submission if quality standards not met
- Provides actionable error messages to Claude for correction

## Quality Standards

All code generated using this plugin **MUST** meet these standards:

### Type Safety
- ✅ All functions have explicit return type annotations
- ✅ Use Python 3.13 built-in generics (`list[T]` not `List[T]`)
- ✅ Use union operator (`str | None` not `Optional[str]`)
- ✅ Pass `mypy --strict` with zero errors

### Pydantic V2 Compliance
- ✅ All models use `model_config = ConfigDict(strict=True, frozen=True)`
- ✅ Use V2 validators: `@field_validator`, `@model_validator`
- ✅ Use V2 methods: `model_dump()`, `model_validate()`
- ✅ No V1 syntax allowed

### Code Quality
- ✅ Zero Ruff linting warnings
- ✅ Black-compatible formatting (via Ruff)
- ✅ Imports organized: stdlib → third-party → local
- ✅ Comprehensive docstrings

### Testing
- ✅ Minimum 80% code coverage
- ✅ AAA pattern in all tests
- ✅ Proper fixture scoping
- ✅ All external dependencies mocked

### Error Handling (Async Code)
- ✅ All async functions have try/except blocks
- ✅ Specific exception types (not bare except)
- ✅ Timeouts on all I/O operations
- ✅ Async context managers for resources

## Installation

This plugin is installed as part of the Vibekit plugin system.

**Location**: `plugins/agentient-python-core/`

**Dependencies**:
- Python 3.13+
- ruff (latest)
- mypy (latest)
- pytest (latest)
- pytest-cov (latest)
- pydantic v2.12+

**Install dependencies**:
```bash
pip install ruff mypy pytest pytest-cov pydantic>=2.12
```

## Usage Examples

### Example 1: Create a User Management Module

```bash
# Request module creation
"Create a user management module with Pydantic models for User, UserCreate, and UserUpdate"

# python-architect-agent activates:
# 1. Designs module structure
# 2. Creates Pydantic V2 models with strict mode
# 3. Implements services layer
# 4. Adds type annotations
# 5. Quality gate validates on Write
```

**Result**: Fully typed, validated module passing all quality checks.

### Example 2: Generate Test Suite

```bash
/create-test user_management

# testing-agent activates:
# 1. Analyzes user_management module
# 2. Designs test strategy
# 3. Creates fixtures (user_factory, etc.)
# 4. Generates tests following AAA pattern
# 5. Runs coverage to verify 80%+
```

**Result**: Comprehensive test suite with 85%+ coverage.

### Example 3: Add Email Validation

```bash
/add-validator User email

# Adds Pydantic V2 field validator:
@field_validator('email')
@classmethod
def validate_email(cls, v: str) -> str:
    if '@' not in v:
        raise ValueError('Invalid email address')
    return v.lower()
```

### Example 4: Quality Check Before Commit

```bash
/run-quality-check src/

# Output:
✅ Ruff linting: 0 errors
✅ Ruff formatting: All files formatted
✅ mypy: Success, no issues found

Quality checks PASSED
```

## Token Efficiency

The Skills architecture dramatically reduces token usage:

**Typical Scenario** (module creation):
- Metadata (all skills): 700 tokens
- Active skills (2): ~4500 tokens
- **Total**: ~5200 tokens

**Monolithic Approach** (all content always loaded):
- Total content: ~37,000 tokens

**Efficiency Gain**: ~86% reduction in typical usage

## Integration Points

This plugin serves as a **required dependency** for:

### agentient-rag-engine
- **Uses**: Pydantic V2 data modeling patterns
- **Skills Needed**: pydantic-v2-strict, async-patterns
- **Impact**: RAG data ingestion schemas follow this plugin's patterns

### agentient-frontend-bff
- **Uses**: Pydantic V2 for API contracts
- **Skills Needed**: pydantic-v2-strict, type-hints-best-practices
- **Impact**: API request/response schemas inherit strict mode

### agentient-quality-assurance
- **Uses**: pytest patterns as foundation
- **Skills Needed**: pytest-patterns
- **Impact**: Advanced testing strategies extend basic patterns from this plugin

## Architecture Decisions

### Why Strict Mode Only?
Pydantic's strict mode prevents silent type coercion, which is a common source of bugs. By enforcing `strict=True` globally, we ensure type contracts are honored exactly.

### Why mypy --strict?
Strict mode enables maximum type safety by disallowing implicit `Any`, untyped functions, and other type system loopholes. This catches bugs at development time, not runtime.

### Why Frozen Models?
Immutable models (`frozen=True`) prevent accidental state mutations and enable safe sharing across threads/tasks in async code.

### Why Quality Gate Hook?
Automated enforcement is more reliable than developer memory. The hook ensures standards are met before code is even committed, creating a tight feedback loop.

## Troubleshooting

### Quality Gate Blocks My Code

**Problem**: PostToolUse hook exits with code 2, blocking your code.

**Solution**:
1. Read the error message sent to Claude (it's in stderr)
2. Run `/run-quality-check <file>` manually to see details
3. Fix issues:
   - Ruff: Run `ruff check --fix <file>` and `ruff format <file>`
   - mypy: Add missing type annotations
4. Claude will retry with corrected code

### Coverage Below 80%

**Problem**: Tests don't meet coverage requirement.

**Solution**:
1. Run `pytest --cov=<module> --cov-report=term-missing`
2. Identify uncovered lines in "Missing" column
3. Add tests for those specific lines/branches
4. Focus on error handling paths (try/except branches)

### mypy Errors on Third-Party Libraries

**Problem**: mypy reports missing stubs for third-party package.

**Solution**:
1. Install type stubs: `pip install types-<package>`
2. If no stubs exist, add per-module override in `pyproject.toml`:
   ```toml
   [[tool.mypy.overrides]]
   module = "untyped_lib.*"
   ignore_missing_imports = true
   ```

### Pydantic V1 Code Rejected

**Problem**: Legacy Pydantic V1 patterns fail quality checks.

**Solution**: Migrate to V2 syntax:
- `class Config:` → `model_config = ConfigDict()`
- `@validator` → `@field_validator`
- `.dict()` → `.model_dump()`
- `.parse_obj()` → `.model_validate()`

## Contributing

This plugin follows the Vibekit Plugin Specification v2.2.

**Changes must**:
- Maintain backward compatibility with dependent plugins
- Pass all quality gates
- Include updated documentation
- Add tests for new features

## License

Copyright © 2025 Agentient Labs. All rights reserved.

---

## Quick Reference

### Common Commands
```bash
/create-module <name>          # Generate Python module
/create-test <module>          # Generate test suite
/add-validator <model> <field> # Add Pydantic validator
/run-quality-check <path>      # Run quality checks
```

### Quality Tools
```bash
ruff check --fix <file>    # Lint and auto-fix
ruff format <file>         # Format code
mypy --strict <file>       # Type check
pytest --cov=<module>      # Run tests with coverage
```

### Key Standards
- Python 3.13 modern syntax only
- Pydantic V2 with strict mode
- mypy strict compliance
- 80%+ test coverage
- Zero Ruff warnings
- Comprehensive error handling

---

**For detailed specifications, see:**
- `.reference/specifications/specification-v2.2.md`
- `.reference/plugin-specs/plugin_spec_agentient-python-core.md`
