# Quality Report Command

Generate comprehensive quality metrics dashboard with trends, violations, and actionable recommendations.

## Purpose

Aggregate quality metrics across codebase to provide holistic view of code health, identify areas needing attention, and track quality over time.

## Usage

### Full Report
```
/quality-report
```

### Specific Module
```
/quality-report src/auth/
```

### With Historical Comparison
```
/quality-report --compare-to=main
```

## Output Structure

```markdown
# Code Quality Report

**Generated**: 2025-01-23 14:30:00
**Scope**: src/ (42 files, 5,234 lines)
**Overall Health**: 🟡 GOOD (78/100)

---

## Executive Summary

### Quality Score: 78/100

| Metric | Score | Status | Threshold |
|--------|-------|--------|-----------|
| Test Coverage | 73.5% | ❌ BELOW | 80% |
| Code Complexity | 85/100 | ✅ PASS | 80/100 |
| Security | 92/100 | ✅ PASS | 90/100 |
| Maintainability | 74/100 | 🟡 WARN | 75/100 |
| Lint Violations | 12 | 🟡 WARN | <10 |

### Critical Actions Required

1. ❌ **Increase test coverage** from 73.5% to 80% (13 tests needed)
2. 🟡 **Reduce complexity** in 3 functions (CC >15)
3. ❌ **Fix 2 security vulnerabilities** (S105, S307)

---

## Test Coverage Analysis

### Overall Coverage: 73.5% ❌

| Type | Coverage | Status |
|------|----------|--------|
| Statement | 75.2% | 🟡 |
| Branch | 68.9% | ❌ |
| Function | 81.3% | ✅ |
| Line | 75.2% | 🟡 |

### Coverage by Module

| Module | Coverage | Lines | Status |
|--------|----------|-------|--------|
| src/auth/ | 45.2% | 328 | ❌ CRITICAL |
| src/api/ | 78.5% | 892 | 🟡 CLOSE |
| src/models/ | 85.3% | 445 | ✅ GOOD |
| src/utils/ | 92.1% | 156 | ✅ EXCELLENT |

**Worst Performers**:
1. src/auth/password_reset.py: 0%
2. src/api/webhooks.py: 12%
3. src/auth/oauth.py: 38%

---

## Code Complexity

### Average Cyclomatic Complexity: 5.2 ✅

**Distribution**:
- 1-5 (Low): 87% of functions ✅
- 6-10 (Moderate): 10% of functions ✅
- 11-20 (Complex): 2.5% of functions 🟡
- 21+ (Very Complex): 0.5% of functions ❌

### High Complexity Functions

| Function | File | CC | Status |
|----------|------|----|----|
| process_payment() | src/payment/process.py:78 | 18 | ❌ |
| handle_webhook() | src/api/webhooks.py:45 | 16 | 🟡 |
| validate_user_input() | src/api/validation.py:120 | 15 | 🟡 |

**Refactoring Recommended**: 3 functions above CC=15

---

## Security Analysis

### Security Score: 92/100 ✅

**Violations by Severity**:
- 🔴 CRITICAL: 2
- 🟡 HIGH: 4
- 🟠 MEDIUM: 7
- ⚪ LOW: 3

### Critical Security Issues

#### 1. S105: Hardcoded Password (src/auth.py:45)
```python
password = "admin123"  # ❌ CRITICAL
```
**Impact**: Credential exposure
**Fix**: Use environment variables

#### 2. S307: Use of eval() (src/api/calc.py:89)
```python
result = eval(user_input)  # ❌ CODE INJECTION
```
**Impact**: Arbitrary code execution
**Fix**: Use ast.literal_eval() or safe parser

### Security by Category (OWASP Top 10)

| Category | Count | Severity |
|----------|-------|----------|
| A01: Broken Access Control | 0 | ✅ |
| A02: Cryptographic Failures | 1 | 🟡 |
| A03: Injection | 1 | ❌ |
| A04: Insecure Design | 0 | ✅ |
| A07: Authentication Failures | 2 | 🟡 |

---

## Lint Violations

### Total Violations: 12 🟡

| Tool | Violations | Critical |
|------|------------|----------|
| Ruff | 8 | 2 |
| mypy | 3 | 0 |
| ESLint | 1 | 0 |

### Violations by Rule

| Rule | Count | Severity | Description |
|------|-------|----------|-------------|
| S105 | 1 | CRITICAL | Hardcoded password |
| S307 | 1 | CRITICAL | Use of eval |
| B006 | 3 | WARNING | Mutable default arg |
| FORMAT | 5 | INFO | Not formatted |
| type[arg-type] | 2 | WARNING | Type mismatch |

---

## Maintainability Index

### Overall MI: 74/100 🟡

**Calculation**: Combines complexity, lines of code, and comment ratio

**Distribution**:
- 85-100 (Highly Maintainable): 45% ✅
- 65-84 (Moderately Maintainable): 42% 🟡
- 0-64 (Difficult to Maintain): 13% ❌

### Low Maintainability Files

| File | MI | Issues |
|------|----|----|---|
| src/payment/process.py | 58 | High complexity, low comments |
| src/api/webhooks.py | 62 | Long functions, nested logic |
| src/auth/oauth.py | 64 | Complex conditionals |

---

## Trends (vs. main branch)

| Metric | Previous | Current | Change |
|--------|----------|---------|--------|
| Coverage | 75.2% | 73.5% | 📉 -1.7% |
| Violations | 8 | 12 | 📈 +4 |
| Complexity | 5.1 | 5.2 | 📈 +0.1 |
| Maintainability | 76 | 74 | 📉 -2 |

**⚠️ Quality Degradation Detected**

---

## Recommendations

### Immediate Actions (This Sprint)

1. **Fix Security Issues** (Est: 2 hours)
   - Remove hardcoded password (S105)
   - Replace eval() with safe parser (S307)

2. **Increase Coverage to 80%** (Est: 8 hours)
   - Add tests for src/auth/password_reset.py
   - Cover error handling in src/api/webhooks.py
   - Test edge cases in src/payment/process.py

3. **Refactor Complex Functions** (Est: 4 hours)
   - Split process_payment() (CC=18 → target <10)
   - Simplify handle_webhook() logic

### Medium-Term (Next 2 Sprints)

1. **Enable Stricter Type Checking**
   - Add `--strict` to mypy configuration
   - Fix existing type errors (3 violations)

2. **Improve Documentation**
   - Add docstrings to public APIs
   - Increase maintainability index to 80+

3. **Automate Quality Gates**
   - Add pre-commit hooks (Ruff, mypy)
   - Configure CI/CD coverage threshold

---

## CI/CD Integration Status

✅ quality_gate.py: Enabled (PostToolUse hook)
✅ coverage_validator.py: Enabled (Stop hook)
🟡 Pre-commit hooks: Not configured
❌ Automated reporting: Not enabled

**Setup Commands**:
```bash
# Install pre-commit
pip install pre-commit
pre-commit install

# Configure CI coverage check
# (Add to GitHub Actions workflow)
python3 scripts/coverage_validator.py
```

---

## Quality Score Calculation

```
Overall Score = (
    Coverage * 0.30 +
    Complexity * 0.25 +
    Security * 0.25 +
    Maintainability * 0.15 +
    LintViolations * 0.05
)

Current: 78/100
Target: 85/100
```

---

## Next Steps

1. ✅ Review this report with team
2. ⏳ Assign critical security fixes (2 issues)
3. ⏳ Plan coverage improvement sprint
4. ⏳ Schedule refactoring session for complex functions
5. ⏳ Configure automated quality reporting
```

## Configuration

Environment variables:
- `QUALITY_REPORT_FORMAT`: json, markdown, html (default: markdown)
- `QUALITY_REPORT_INCLUDE_HISTORY`: true/false
- `QUALITY_REPORT_THRESHOLD`: Minimum acceptable score

## Success Criteria

Report is complete when:
✅ All metrics calculated
✅ Trends analyzed (if historical data available)
✅ Critical issues identified
✅ Actionable recommendations provided
✅ Next steps documented
✅ CI/CD integration status reported
