# Create Test Suite

Generate a comprehensive pytest test suite for a Python module, achieving 80%+ coverage.

## Task

You are tasked with creating a complete test suite for an existing Python module with the following requirements:

### Test Suite Structure

Create the following test structure:

```
tests/
├── conftest.py                    # Shared fixtures
└── test_<module_name>/
    ├── test_models.py             # Pydantic model tests
    ├── test_services.py           # Business logic tests
    └── test_integration.py        # Integration tests (if needed)
```

### Quality Standards (MANDATORY)

All generated tests MUST meet these standards:

1. **Coverage**:
   - Achieve minimum 80% code coverage
   - Test all public functions and methods
   - Cover all branches (if/else, try/except)
   - Test error handling paths

2. **Test Structure**:
   - Follow AAA pattern (Arrange-Act-Assert)
   - One logical assertion per test
   - Clear test names: `test_<feature>_<scenario>_<expected>`
   - Tests are independent and can run in any order

3. **Fixtures**:
   - Use pytest fixtures for setup/teardown
   - Proper scoping (function, module, session)
   - Yield fixtures for cleanup
   - Type-annotated fixtures

4. **Parametrization**:
   - Use `@pytest.mark.parametrize` for multiple inputs
   - No conditional logic inside tests
   - Clear parameter names

5. **Mocking**:
   - Mock all external dependencies (APIs, databases, file I/O)
   - Use `@patch` or `Mock` from unittest.mock
   - Verify mock call counts and arguments

### Implementation Steps

1. **Invoke testing-agent**:
   - The testing agent will analyze the module to be tested
   - They will design a comprehensive test strategy
   - They will create fixtures, parametrized tests, and mocks

2. **Generate Test Files**:
   - Create `conftest.py` with shared fixtures
   - Create `test_*.py` files for each source file
   - Organize tests by feature/function

3. **Run Coverage**:
   - Execute `pytest --cov=<module> --cov-report=term-missing`
   - Identify uncovered lines
   - Add tests to reach 80%+ coverage

4. **Quality Checks**:
   - All tests pass: `pytest tests/`
   - Coverage meets threshold: `pytest --cov --cov-fail-under=80`
   - No warnings or errors

### Example Test Patterns

**AAA Pattern**:
```python
def test_user_creation_with_valid_data():
    """Test that User.create() creates user with valid data."""
    # ARRANGE
    user_data = {"email": "test@example.com", "username": "testuser"}

    # ACT
    user = User.create(user_data)

    # ASSERT
    assert user.email == "test@example.com"
    assert user.username == "testuser"
```

**Parametrized Test**:
```python
@pytest.mark.parametrize("email,expected_valid", [
    ("user@example.com", True),
    ("invalid-email", False),
    ("", False),
])
def test_email_validation(email: str, expected_valid: bool):
    assert EmailValidator.is_valid(email) == expected_valid
```

**Fixture with Cleanup**:
```python
@pytest.fixture
def database_connection():
    """Provide test database connection with cleanup."""
    conn = connect_to_test_db()
    yield conn
    conn.close()
```

**Mocking External API**:
```python
@patch('requests.get')
def test_api_client(mock_get):
    """Test API client with mocked HTTP request."""
    mock_get.return_value.json.return_value = {"id": 123}
    client = APIClient()
    result = client.get_user(123)
    assert result["id"] == 123
```

### Example Usage

```bash
# User invokes the command
/create-test user_management

# Result: Creates tests/test_user_management/ with:
# - conftest.py: Shared fixtures (user_factory, etc.)
# - test_models.py: Tests for UserSchema validation
# - test_services.py: Tests for create_user(), update_user()
# - Coverage: 85%+ achieved
```

### Validation

After generation, the test suite MUST:
- ✅ All tests pass: `pytest tests/`
- ✅ Coverage ≥ 80%: `pytest --cov=<module> --cov-fail-under=80`
- ✅ No test warnings or errors
- ✅ Tests follow AAA pattern
- ✅ External dependencies are mocked
- ✅ Async tests use `@pytest.mark.asyncio`

### Coverage Report

The testing-agent will provide a coverage report:

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
user_management/models.py    45      3    93%   23, 45, 67
user_management/services.py  67      8    88%   12-15, 89-92
-------------------------------------------------------
TOTAL                       112     11    90%
```

## Prompt

I need to create a comprehensive test suite for the `{module_name}` module.

Please use the testing-agent to:
1. Analyze the module and identify all functions/classes to test
2. Design a test strategy with fixtures and mocking plan
3. Generate tests following AAA pattern and pytest best practices
4. Achieve 80%+ code coverage
5. Provide a coverage report showing results
