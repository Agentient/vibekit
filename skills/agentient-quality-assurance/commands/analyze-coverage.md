# Analyze Coverage Command

Generate comprehensive test coverage analysis with gap identification and high-value test recommendations.

## Purpose

Analyze test coverage reports to identify critical gaps, suggest high-impact test additions, and provide a roadmap to meet coverage thresholds.

## How It Works

1. **Locate Coverage Report**: Auto-detect or use specified path
2. **Parse Report**: Support coverage.py (Python) and Jest/Vitest (JS/TS)
3. **Identify Gaps**: Find uncovered critical paths, error handlers, edge cases
4. **Prioritize**: Risk-based ranking of uncovered code
5. **Generate Recommendations**: Specific test suggestions with coverage impact

## Usage

### Auto-detect Report
```
/analyze-coverage
```

### Specify Report Path
```
/analyze-coverage coverage/coverage.json
```

### With Threshold Check
```
/analyze-coverage --threshold=80
```

## Output Structure

```markdown
## Coverage Analysis Report

### Summary
**Current Coverage**: 73.5%
**Threshold**: 80% (Backend)
**Gap**: 6.5% (13 additional tests estimated)
**Status**: ❌ BELOW THRESHOLD

### Coverage Breakdown
- Statement: 75.2%
- Branch: 68.9% ⚠️ (low branch coverage)
- Function: 81.3%
- Line: 75.2%

---

### Critical Gaps (High Risk, Low Coverage)

#### 1. src/auth/password_reset.py (0% coverage)
**Risk**: CRITICAL - Security-sensitive code
**Lines**: 45-72 (28 lines uncovered)

**Uncovered Functions**:
- `generate_reset_token()` - Creates password reset tokens
- `validate_reset_token()` - Verifies token expiry and signature
- `send_reset_email()` - Email delivery

**Why Critical**:
- Security-sensitive password reset flow
- No validation of token generation logic
- Email delivery failures not tested

**Recommended Tests** (Est. +3.5% coverage):
```python
def test_generate_reset_token():
    """Test token generation with valid user"""
    token = generate_reset_token(user)
    assert token is not None
    assert len(token) == 64  # Verify token format

def test_validate_reset_token_expired():
    """Test expired token rejection"""
    old_token = generate_reset_token(user, expires_in=-3600)
    with pytest.raises(TokenExpiredError):
        validate_reset_token(old_token)

def test_send_reset_email_failure():
    """Test email delivery error handling"""
    with patch('smtplib.SMTP') as mock_smtp:
        mock_smtp.side_effect = SMTPException("Connection failed")
        with pytest.raises(EmailDeliveryError):
            send_reset_email(user.email, token)
```

---

#### 2. src/payment/process.py:120-145 (15% coverage)
**Risk**: HIGH - Financial transaction handling
**Lines**: 25 uncovered (of 26 total in error handling)

**Uncovered Paths**:
- Payment gateway timeout handling
- Declined card processing
- Refund failure scenarios
- Invalid amount validation

**Why Critical**:
- Financial impact of bugs
- Edge cases not validated
- Incomplete error recovery testing

**Recommended Tests** (Est. +2.1% coverage):
```python
def test_payment_gateway_timeout():
    """Test timeout handling with retry logic"""
    with patch('payment_gateway.charge') as mock:
        mock.side_effect = TimeoutError()
        result = process_payment(amount, card)
        assert result.status == "RETRY_SCHEDULED"

def test_declined_card_handling():
    """Test declined transaction flow"""
    with patch('payment_gateway.charge') as mock:
        mock.return_value = {"status": "declined"}
        result = process_payment(amount, declined_card)
        assert result.status == "DECLINED"
        assert result.user_message == "Card declined"
```

---

#### 3. components/UserProfile.tsx:78-95 (40% coverage)
**Risk**: MEDIUM - User experience
**Lines**: 18 uncovered (avatar upload error states)

**Uncovered Scenarios**:
- File size too large
- Invalid file type
- Upload network failure
- S3 upload permission denied

**Recommended Tests** (Est. +1.2% coverage):
```typescript
test('shows error when file too large', async () => {
  const largeFile = new File(['x'.repeat(6_000_000)], 'large.jpg');

  render(<UserProfile />);
  const input = screen.getByLabelText(/upload avatar/i);

  await userEvent.upload(input, largeFile);

  expect(screen.getByText(/file too large/i)).toBeInTheDocument();
});

test('shows error when upload fails', async () => {
  server.use(
    rest.post('/api/upload', (req, res, ctx) => {
      return res(ctx.status(500));
    })
  );

  render(<UserProfile />);
  const input = screen.getByLabelText(/upload avatar/i);
  const validFile = new File(['data'], 'avatar.jpg');

  await userEvent.upload(input, validFile);

  expect(await screen.findByText(/upload failed/i)).toBeInTheDocument();
});
```

---

### Medium Priority Gaps

| File | Coverage | Lines | Risk | Est. Impact |
|------|----------|-------|------|-------------|
| src/api/validation.py | 55% | 45 uncovered | Medium | +1.8% |
| src/db/migrations.py | 60% | 32 uncovered | Low | +1.3% |
| components/Dashboard.tsx | 65% | 28 uncovered | Medium | +1.0% |

---

### Coverage Improvement Roadmap

**Phase 1: Critical Security (Target: +3.5%)**
- [ ] Add 5 tests for password_reset.py
- [ ] Cover token generation edge cases
- [ ] Test email delivery failures

**Phase 2: Financial Transactions (Target: +2.1%)**
- [ ] Add 8 tests for payment error handling
- [ ] Test gateway timeout/retry logic
- [ ] Cover refund scenarios

**Phase 3: User Flows (Target: +1.2%)**
- [ ] Add 4 tests for avatar upload
- [ ] Test file validation
- [ ] Test upload error states

**Projected Total**: 73.5% → 80.3% ✅ MEETS THRESHOLD

---

### Recommendations

1. **Prioritize Security**: Password reset has 0% coverage, critical risk
2. **Focus on Error Handling**: 68.9% branch coverage indicates missing error paths
3. **Add Integration Tests**: Current tests are mostly happy-path unit tests
4. **Automate Coverage**: Add coverage check to CI/CD (use coverage_validator.py)

---

### Next Steps

1. Implement Phase 1 tests (Est. 2-3 hours)
2. Run `pytest --cov=src --cov-report=html` to verify
3. Review coverage report for new gaps
4. Proceed to Phase 2 if threshold met
```

## Supported Report Formats

### Python (coverage.py)
- **coverage.json**: JSON format (preferred)
- **coverage.xml**: Cobertura XML
- **.coverage**: SQLite database

### JavaScript/TypeScript
- **coverage-summary.json**: Jest/Vitest summary
- **lcov.info**: LCOV format
- **coverage/**: HTML report directory

## Gap Analysis Criteria

**Critical Gaps** (must test):
- Security-sensitive code (auth, payment, encryption)
- Error handlers (try/except, catch blocks)
- Boundary conditions (null, empty, max values)
- Complex conditional logic (high cyclomatic complexity)

**High Priority**:
- Business logic
- API endpoints
- Database operations
- State management

**Medium Priority**:
- Utility functions
- UI components
- Data transformations

**Low Priority**:
- Generated code
- Third-party integrations (mocked)
- Deprecated code

## Configuration

Environment variables:
- `BACKEND_COVERAGE_THRESHOLD`: Default 80
- `FRONTEND_COVERAGE_THRESHOLD`: Default 70
- `COVERAGE_REPORT_PATH`: Override auto-detection

## Success Criteria

Analysis is complete when:
✅ Coverage report parsed successfully
✅ Gaps identified and categorized by risk
✅ Specific test recommendations provided
✅ Coverage improvement roadmap created
✅ Projected coverage calculated
✅ Next steps documented
