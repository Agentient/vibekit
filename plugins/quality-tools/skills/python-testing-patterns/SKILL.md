---
name: python-testing-patterns
version: "1.0"
description: >
  Pytest fixtures, parametrization, mocking, and test organization patterns.
  PROACTIVELY activate for: (1) Writing pytest test suites, (2) Creating fixtures,
  (3) Implementing parametrized tests, (4) Mocking external dependencies, (5) Organizing test directories.
  Triggers: "pytest", "fixture", "parametrize", "mock", "python test", "unittest", "conftest"
core-integration:
  techniques:
    primary: ["exhaustive_edge_case_enumeration"]
    secondary: ["completeness_verification"]
  contracts:
    input: "none"
    output: "none"
  patterns: "none"
  rubrics: "none"
---

# Python Testing Patterns Skill

## Metadata (Tier 1)

**Keywords**: pytest, fixture, parametrize, mock, python test, unittest

**File Patterns**: test_*.py, *_test.py

**Modes**: testing_backend

---

## Instructions (Tier 2)

### Fixture Design

```python
import pytest

@pytest.fixture
def database():
    """Create test database"""
    db = setup_database()
    yield db  # Provide to test
    teardown_database(db)  # Cleanup

def test_query(database):
    result = database.query("SELECT * FROM users")
    assert result is not None
```

**Scopes**: function (default), class, module, session

### Parametrization

```python
@pytest.mark.parametrize("input,expected", [
    (3, 9),
    (4, 16),
    (-2, 4),
])
def test_square(input, expected):
    assert square(input) == expected
```

### Mocking

```python
from unittest.mock import patch, MagicMock

def test_api_call():
    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'data': 'test'}

        result = fetch_data('https://api.example.com')

        assert result == {'data': 'test'}
        mock_get.assert_called_once()
```

### Test Organization

```
tests/
├── unit/
│   ├── test_auth.py
│   └── test_models.py
├── integration/
│   └── test_api.py
└── conftest.py  # Shared fixtures
```

### Anti-Patterns

- Test interdependence
- Mocking implementation details
- Not using fixtures for setup/teardown
- Hardcoded test data
