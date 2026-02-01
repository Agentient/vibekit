# Suggest Tests Command

Generate AI-powered test case suggestions for functions, classes, or components with ready-to-use test code templates.

## Purpose

Analyze code structure and suggest comprehensive test cases covering happy paths, edge cases, error handling, and integration scenarios.

## Usage

### Single Function
```
/suggest-tests src/auth.py::hash_password
```

### Component
```
/suggest-tests components/LoginForm.tsx
```

### Class
```
/suggest-tests src/models/User.py::User
```

## Output Structure

```markdown
## Test Suggestions: hash_password()

### Function Analysis
**File**: src/auth.py
**Function**: hash_password(password: str, salt: Optional[str] = None) -> str
**Complexity**: 3 (Low)
**Current Coverage**: 60% (3 of 5 paths covered)

### Suggested Test Cases

#### 1. Happy Path Tests

##### test_hash_password_valid_input
**Purpose**: Verify basic password hashing with valid input
**Coverage**: +10%

```python
def test_hash_password_valid_input():
    """Test password hashing with valid input"""
    password = "SecureP@ssw0rd"
    hashed = hash_password(password)

    assert hashed is not None
    assert len(hashed) == 60  # bcrypt output length
    assert hashed.startswith("$2b$")  # bcrypt identifier
```

##### test_hash_password_with_custom_salt
**Purpose**: Verify hashing with custom salt
**Coverage**: +8%

```python
def test_hash_password_with_custom_salt():
    """Test password hashing with provided salt"""
    password = "Test123"
    salt = bcrypt.gensalt(rounds=12)

    hashed = hash_password(password, salt=salt)

    assert bcrypt.checkpw(password.encode(), hashed.encode())
```

---

#### 2. Edge Case Tests

##### test_hash_password_empty_string
**Purpose**: Verify handling of empty password
**Coverage**: +6%

```python
def test_hash_password_empty_string():
    """Test password hashing with empty string"""
    with pytest.raises(ValueError, match="Password cannot be empty"):
        hash_password("")
```

##### test_hash_password_very_long_input
**Purpose**: Verify handling of maximum length password
**Coverage**: +5%

```python
def test_hash_password_very_long_input():
    """Test password hashing with 72-byte limit (bcrypt max)"""
    # bcrypt has 72-byte limit
    password = "A" * 100

    hashed = hash_password(password)

    # Should truncate or raise error
    assert hashed is not None or pytest.raises(ValueError)
```

##### test_hash_password_unicode_characters
**Purpose**: Verify handling of non-ASCII characters
**Coverage**: +4%

```python
def test_hash_password_unicode_characters():
    """Test password hashing with unicode characters"""
    password = "Pässwörd123!🔒"

    hashed = hash_password(password)

    assert bcrypt.checkpw(password.encode('utf-8'), hashed.encode())
```

---

#### 3. Error Handling Tests

##### test_hash_password_none_input
**Purpose**: Verify handling of None value
**Coverage**: +7%

```python
def test_hash_password_none_input():
    """Test password hashing with None input"""
    with pytest.raises(TypeError, match="Password must be string"):
        hash_password(None)
```

---

#### 4. Security Tests

##### test_hash_password_consistent_output
**Purpose**: Verify same password produces different hashes (salt)
**Coverage**: +3%

```python
def test_hash_password_consistent_output():
    """Test that same password produces different hashes"""
    password = "Test123"

    hash1 = hash_password(password)
    hash2 = hash_password(password)

    assert hash1 != hash2  # Different salts
    assert bcrypt.checkpw(password.encode(), hash1.encode())
    assert bcrypt.checkpw(password.encode(), hash2.encode())
```

---

### Coverage Impact Summary

| Test Case | Coverage Gain | Priority |
|-----------|---------------|----------|
| test_hash_password_valid_input | +10% | HIGH |
| test_hash_password_with_custom_salt | +8% | MEDIUM |
| test_hash_password_none_input | +7% | HIGH |
| test_hash_password_empty_string | +6% | HIGH |
| test_hash_password_very_long_input | +5% | MEDIUM |
| test_hash_password_unicode_characters | +4% | LOW |
| test_hash_password_consistent_output | +3% | MEDIUM |

**Total Projected Coverage**: 60% → 103% ✅ (overlap expected, realistic: 95%)

---

### Implementation Template

```python
# tests/test_auth.py
import pytest
import bcrypt
from src.auth import hash_password


class TestHashPassword:
    """Tests for password hashing function"""

    def test_hash_password_valid_input(self):
        """Test password hashing with valid input"""
        password = "SecureP@ssw0rd"
        hashed = hash_password(password)

        assert hashed is not None
        assert len(hashed) == 60
        assert hashed.startswith("$2b$")

    def test_hash_password_empty_string(self):
        """Test password hashing with empty string"""
        with pytest.raises(ValueError, match="Password cannot be empty"):
            hash_password("")

    def test_hash_password_none_input(self):
        """Test password hashing with None input"""
        with pytest.raises(TypeError, match="Password must be string"):
            hash_password(None)

    # Add remaining tests...
```

---

### Next Steps

1. Copy suggested tests to `tests/test_auth.py`
2. Run `pytest tests/test_auth.py::TestHashPassword -v`
3. Verify coverage: `pytest --cov=src.auth --cov-report=term`
4. Adjust assertions based on actual implementation
5. Add fixtures if needed for test data setup
```

## For React Components

```markdown
## Test Suggestions: LoginForm Component

### Component Analysis
**File**: components/LoginForm.tsx
**Props**: { onSubmit, isLoading }
**State**: email, password, errors
**Current Coverage**: 45%

### Suggested Test Cases

#### 1. Rendering Tests

```typescript
test('renders login form with all fields', () => {
  render(<LoginForm onSubmit={jest.fn()} />);

  expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /log in/i })).toBeInTheDocument();
});
```

#### 2. User Interaction Tests

```typescript
test('submits form with valid credentials', async () => {
  const handleSubmit = jest.fn();
  render(<LoginForm onSubmit={handleSubmit} />);

  await userEvent.type(screen.getByLabelText(/email/i), 'user@example.com');
  await userEvent.type(screen.getByLabelText(/password/i), 'password123');
  await userEvent.click(screen.getByRole('button', { name: /log in/i }));

  expect(handleSubmit).toHaveBeenCalledWith({
    email: 'user@example.com',
    password: 'password123'
  });
});
```

#### 3. Validation Tests

```typescript
test('shows error for invalid email', async () => {
  render(<LoginForm onSubmit={jest.fn()} />);

  await userEvent.type(screen.getByLabelText(/email/i), 'invalid-email');
  await userEvent.click(screen.getByRole('button', { name: /log in/i }));

  expect(await screen.findByText(/invalid email/i)).toBeInTheDocument();
});
```

#### 4. Loading State Tests

```typescript
test('disables submit button when loading', () => {
  render(<LoginForm onSubmit={jest.fn()} isLoading={true} />);

  const submitButton = screen.getByRole('button', { name: /log in/i });
  expect(submitButton).toBeDisabled();
});
```
```

## Success Criteria

Suggestions are complete when:
✅ Function/component analyzed
✅ Test cases categorized (happy path, edge cases, errors)
✅ Ready-to-use code templates provided
✅ Coverage impact estimated
✅ Implementation guidance included
