# Add Pydantic Validator

Add a Pydantic V2 validator to an existing model following strict mode requirements.

## Task

You are tasked with adding a validator to a Pydantic V2 model with the following requirements:

### Validator Requirements

1. **Use Pydantic V2 Syntax**:
   - Use `@field_validator` for field-level validation
   - Use `@model_validator` for cross-field validation
   - NEVER use V1 `@validator` or `@root_validator`

2. **Validation Modes**:
   - `mode='before'`: Transform raw input BEFORE type validation
   - `mode='after'`: Validate AFTER type validation (default)
   - `mode='wrap'`: Full control over validation process

3. **Error Handling**:
   - Raise `ValueError` for validation failures (not TypeError)
   - Provide clear, actionable error messages
   - Include context about what failed

4. **Type Safety**:
   - Validators must be `@classmethod`
   - Proper type annotations for input and return
   - Return the validated (possibly transformed) value

### Validator Patterns

**Field Validator (Single Field)**:
```python
from pydantic import BaseModel, ConfigDict, field_validator

class User(BaseModel):
    model_config = ConfigDict(strict=True)

    email: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str) -> str:
        """Validate email format and normalize to lowercase."""
        if '@' not in v:
            raise ValueError('Invalid email address: missing @ symbol')
        if v.count('@') > 1:
            raise ValueError('Invalid email address: multiple @ symbols')
        return v.lower()  # Normalize
```

**Field Validator (Multiple Fields)**:
```python
class Product(BaseModel):
    model_config = ConfigDict(strict=True)

    price: float
    discount_price: float

    @field_validator('price', 'discount_price')
    @classmethod
    def validate_positive(cls, v: float) -> float:
        """Ensure price values are positive."""
        if v <= 0:
            raise ValueError('Price must be positive')
        return v
```

**Model Validator (Cross-Field Validation)**:
```python
from typing import Self

class UserRegistration(BaseModel):
    model_config = ConfigDict(strict=True)

    password: str
    confirm_password: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> Self:
        """Ensure password and confirmation match."""
        if self.password != self.confirm_password:
            raise ValueError('Passwords do not match')
        return self
```

**Before Validator (Transform Input)**:
```python
class DataModel(BaseModel):
    model_config = ConfigDict(strict=True)

    data: str

    @field_validator('data', mode='before')
    @classmethod
    def clean_data(cls, v: any) -> str:
        """Clean and normalize input data before validation."""
        # Runs BEFORE Pydantic checks if v is a string
        if isinstance(v, bytes):
            v = v.decode('utf-8')
        return str(v).strip()
```

**Complex Validation with Dependencies**:
```python
class Order(BaseModel):
    model_config = ConfigDict(strict=True)

    total_amount: float
    discount: float
    final_amount: float

    @model_validator(mode='after')
    def validate_amounts(self) -> Self:
        """Ensure final_amount = total_amount - discount."""
        expected = self.total_amount - self.discount
        if abs(self.final_amount - expected) > 0.01:  # Float comparison
            raise ValueError(
                f'Final amount {self.final_amount} does not match '
                f'total {self.total_amount} - discount {self.discount}'
            )
        return self
```

### Implementation Steps

1. **Identify Validation Need**:
   - Determine if validation is field-level or model-level
   - Decide on validation mode (before/after/wrap)
   - Define clear error messages

2. **Add Validator**:
   - Import required decorators
   - Add validator method as `@classmethod`
   - Include proper type annotations
   - Raise `ValueError` with descriptive message
   - Return validated value

3. **Test the Validator**:
   - Test with valid input (should pass)
   - Test with invalid input (should raise ValueError)
   - Verify error message is clear

### Example Usage

```bash
# User wants to add email validation
/add-validator User email

# Result: Adds @field_validator to User model
```

### Common Validation Patterns

**Email Validation**:
```python
@field_validator('email')
@classmethod
def validate_email(cls, v: str) -> str:
    if '@' not in v or v.count('@') != 1:
        raise ValueError('Invalid email format')
    return v.lower()
```

**Age Range**:
```python
@field_validator('age')
@classmethod
def validate_age(cls, v: int) -> int:
    if not (18 <= v <= 120):
        raise ValueError('Age must be between 18 and 120')
    return v
```

**URL Validation**:
```python
@field_validator('website')
@classmethod
def validate_url(cls, v: str) -> str:
    if not v.startswith(('http://', 'https://')):
        raise ValueError('URL must start with http:// or https://')
    return v
```

**Enum Validation**:
```python
@field_validator('status')
@classmethod
def validate_status(cls, v: str) -> str:
    allowed = ['pending', 'approved', 'rejected']
    if v not in allowed:
        raise ValueError(f'Status must be one of {allowed}')
    return v
```

**List Length**:
```python
@field_validator('tags')
@classmethod
def validate_tags(cls, v: list[str]) -> list[str]:
    if len(v) > 10:
        raise ValueError('Maximum 10 tags allowed')
    return v
```

**Mutual Exclusivity**:
```python
@model_validator(mode='after')
def check_mutually_exclusive(self) -> Self:
    if self.field_a is not None and self.field_b is not None:
        raise ValueError('Cannot specify both field_a and field_b')
    if self.field_a is None and self.field_b is None:
        raise ValueError('Must specify either field_a or field_b')
    return self
```

### Anti-Patterns to Avoid

❌ **Using V1 @validator**:
```python
@validator('email')  # DON'T USE V1 decorator
def check_email(cls, v):
    pass
```

❌ **Raising TypeError**:
```python
@field_validator('age')
@classmethod
def check_age(cls, v: int) -> int:
    if v < 0:
        raise TypeError('Age negative')  # Use ValueError!
    return v
```

❌ **Not Returning Value**:
```python
@field_validator('email')
@classmethod
def validate_email(cls, v: str) -> str:
    if '@' not in v:
        raise ValueError('Invalid')
    # MISSING: return v
```

❌ **Conditional Logic Without Clear Message**:
```python
@field_validator('value')
@classmethod
def check(cls, v: int) -> int:
    if v < 0 or v > 100:
        raise ValueError('Invalid')  # Too vague!
    return v
```

### Validation

After adding validator, verify:
- ✅ Validator uses `@field_validator` or `@model_validator` (V2 syntax)
- ✅ Validator is a `@classmethod`
- ✅ Type annotations are complete
- ✅ Raises `ValueError` with clear message
- ✅ Returns validated value
- ✅ Tests verify valid and invalid inputs

## Prompt

I need to add a validator to the `{model_name}` Pydantic model for the field/logic: `{validation_description}`.

Please:
1. Identify if this should be a field validator or model validator
2. Choose the appropriate mode (before/after/wrap)
3. Add the validator with proper Pydantic V2 syntax
4. Include clear error messages
5. Suggest tests to verify the validator works correctly
