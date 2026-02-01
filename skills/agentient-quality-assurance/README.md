# agentient-quality-assurance

Comprehensive quality assurance plugin providing AI-driven testing guidance and deterministic quality gates for Python and TypeScript/JavaScript development.

## Overview

This plugin serves a dual purpose:
1. **Non-Deterministic Guidance**: AI-powered test strategy, code review analysis, and quality recommendations
2. **Deterministic Enforcement**: Fast, blocking quality gates via hook scripts with Exit Code 2

**Confidence Level**: 99%
**Category**: Cross-Cutting
**Version**: 1.0.0

## Core Architecture

### Deterministic vs Non-Deterministic Separation

```
┌─────────────────────────────────────────┐
│     Non-Deterministic (LLM-Powered)     │
├─────────────────────────────────────────┤
│ - Test strategy design                  │
│ - Code review interpretation            │
│ - Refactoring suggestions               │
│ - Coverage gap analysis                 │
│ - Quality metrics explanation           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│      Deterministic (Script-Based)       │
├─────────────────────────────────────────┤
│ - quality_gate.py (lint, type check)    │
│ - coverage_validator.py (thresholds)    │
│ - Exit Code 2 blocking                  │
│ - Fast validation (<60s)                │
└─────────────────────────────────────────┘
```

**Token Efficiency**: Quality checks offloaded to scripts, LLM reserved for complex analysis.

## Components

### 🤖 Agents

#### 1. qa-engineer-agent
**Role**: Test strategy design, quality metrics interpretation, automation setup

**Activation**: Keywords like `strategy`, `testing pyramid`, `metrics`, `quality`, `test plan`

**Responsibilities**:
- Testing pyramid implementation (70-80% unit, 15-20% integration, 5-10% E2E)
- Coverage threshold planning (Backend ≥80%, Frontend ≥70%)
- Cyclomatic complexity analysis
- Test framework configuration (pytest, Jest, Vitest)
- Quality metrics dashboard

**Example Use**:
```
User: "Design a test strategy for our payment processing feature"

Agent: [Plan Mode]
1. Analyzes security requirements (PCI compliance)
2. Designs testing pyramid:
   - Unit: 75% (payment validation, amount calculations)
   - Integration: 20% (gateway API, database transactions)
   - E2E: 5% (complete purchase flow)
3. Defines 95% coverage target (financial code)
4. Lists test scenarios with risk priority
```

#### 2. code-reviewer-agent
**Role**: Automated code review, anti-pattern detection, security analysis

**Activation**: Triggered by `quality_gate.py` PostToolUse hook

**Responsibilities**:
- Interpret quality gate violations
- Explain security risks (OWASP, CWE mapping)
- Provide refactoring guidance
- Flag anti-patterns (B rules, type errors)

**Example Use**:
```
[User writes Python file]
[quality_gate.py runs automatically]

Agent: [Analyzes violations]
🔴 CRITICAL: S105 (line 45) - Hardcoded password
   Risk: Credential exposure via git history
   Fix: Use environment variables or Secret Manager

🟡 WARNING: B006 (line 78) - Mutable default argument
   Risk: Shared state bug across function calls
   Fix: Use None and create new list in function
```

### 📝 Commands

#### `/review-code`
Comprehensive code review with security analysis and refactoring recommendations.

```
/review-code src/auth.py
```

**Output**:
- Violations categorized by severity (Critical → Low)
- Security issues with OWASP/CWE references
- Refactoring examples (before/after code)
- Next steps and priority guidance

#### `/analyze-coverage`
Coverage gap analysis with high-value test recommendations.

```
/analyze-coverage
```

**Output**:
- Current coverage vs threshold
- Critical gaps (uncovered security code, error handlers)
- Prioritized test suggestions with estimated coverage impact
- Coverage improvement roadmap

#### `/suggest-tests`
AI-powered test case generation with ready-to-use code templates.

```
/suggest-tests src/auth.py::hash_password
```

**Output**:
- Happy path, edge case, and error handling tests
- Coverage impact estimates
- Ready-to-copy pytest/Jest code
- Implementation guidance

#### `/quality-report`
Comprehensive quality metrics dashboard with trends and recommendations.

```
/quality-report
```

**Output**:
- Quality score (0-100)
- Coverage, complexity, security, maintainability metrics
- Trend analysis (vs previous version)
- Actionable recommendations with effort estimates

### 🎓 Skills (7 Total)

All skills follow 3-tier progressive disclosure:

| Skill | Tier 2 Tokens | Purpose |
|-------|---------------|---------|
| qa-strategy-and-metrics | ~2,200 | Testing pyramid, CC, MI, coverage principles |
| python-testing-patterns | ~2,800 | pytest fixtures, parametrization, mocking |
| typescript-component-testing | ~3,000 | React Testing Library, Jest, Vitest |
| advanced-js-mocking-patterns | ~2,500 | Module mocks, spies, timers |
| python-code-review-and-linting | ~2,600 | Ruff, mypy, security rules (S prefix) |
| typescript-code-review-and-linting | ~2,700 | ESLint, typescript-eslint, React rules |
| test-coverage-analysis | ~2,000 | coverage.py, Jest coverage, gap analysis |

**Token Budget**:
- Metadata: ~700 tokens (constant)
- Typical code review: ~5,800 tokens
- Test strategy task: ~7,700 tokens
- Peak (all skills): ~18,500 tokens

### 🔒 Quality Gates (Deterministic Enforcement)

#### quality_gate.py

**Multi-language code validator** (Exit Code 2 blocking)

**Checks**:
- **Python**: Ruff lint + format, mypy type checking
- **TypeScript/JS**: ESLint, TypeScript compiler (tsc)

**Features**:
- 30-minute file content caching
- JSON violation output for machine parsing
- Human-readable stderr for LLM context
- Comprehensive error handling

**Invocation**: PostToolUse hook (after file writes)

**Exit Codes**:
- 0: All checks passed
- 2: BLOCKING - violations found

**Example Output**:
```json
[
  {
    "file": "src/auth.py",
    "line": 45,
    "column": 8,
    "rule": "S105",
    "message": "Possible hardcoded password",
    "severity": "ERROR",
    "tool": "ruff"
  }
]
```

#### coverage_validator.py

**Coverage threshold enforcer** (Exit Code 2 blocking)

**Thresholds**:
- Backend (Python): 80% (configurable)
- Frontend (JS/TS): 70% (configurable)

**Features**:
- Auto-detect coverage reports (coverage.json, coverage-summary.json)
- Gap analysis with uncovered files
- Prioritized recommendations

**Invocation**: Stop hook (before agent finishes)

**Exit Codes**:
- 0: Coverage meets threshold
- 2: BLOCKING - coverage below threshold

**Example Output**:
```
❌ COVERAGE_FAILURE: 73.5% < 80%
   Gap: 6.5% (estimated 13 additional tests)

   Top 5 files needing coverage:
     src/auth/password_reset.py: 0%
     src/api/webhooks.py: 12%
     src/payment/process.py: 45%
```

## Installation

### Prerequisites

1. **Claude Code 2.0** installed
2. **Python 3.13** or later
3. **Python Tools**:
   ```bash
   pip install ruff mypy pytest pytest-cov coverage
   ```
4. **Node.js 20 LTS** (for TypeScript/JavaScript)
5. **Node Tools**:
   ```bash
   npm install -g eslint typescript
   ```

### Setup

1. Link plugin to Claude Code:
```bash
ln -s /path/to/vibekit/plugins/agentient-quality-assurance ~/.claude/plugins/
```

2. Verify installation:
```
/help
```

You should see: `/review-code`, `/analyze-coverage`, `/suggest-tests`, `/quality-report`

3. Make hook scripts executable:
```bash
chmod +x plugins/agentient-quality-assurance/scripts/*.py
```

### Configuration

Environment variables (optional):

```bash
# Coverage thresholds
export BACKEND_COVERAGE_THRESHOLD=80
export FRONTEND_COVERAGE_THRESHOLD=70

# Coverage report path (auto-detect if not set)
export COVERAGE_REPORT_PATH=coverage/coverage.json
```

## Usage Examples

### Example 1: Automatic Quality Gate

```python
# 1. Write code with a security issue
# src/auth.py
password = "admin123"  # Hardcoded secret

# 2. quality_gate.py runs automatically (PostToolUse hook)
# Output:
❌ QUALITY_GATE_FAILURE: 1 violation found
   Errors: 1

   ruff: 1 issue

[stderr JSON]
{
  "file": "src/auth.py",
  "line": 3,
  "rule": "S105",
  "message": "Possible hardcoded password: 'admin123'",
  "severity": "ERROR",
  "tool": "ruff"
}

# 3. code-reviewer-agent activates
Agent: 🔴 CRITICAL: S105 - Hardcoded Password

Risk: Credentials exposed in source code
Fix: import os; password = os.getenv("ADMIN_PASSWORD")

# 4. Fix applied
# 5. quality_gate.py passes
✅ Quality gate passed: No violations found
```

### Example 2: Coverage Analysis

```bash
# 1. Run tests with coverage
pytest --cov=src --cov-report=json

# 2. Analyze coverage
/analyze-coverage

# Output:
## Coverage Analysis Report

**Current Coverage**: 73.5%
**Threshold**: 80%
**Gap**: 6.5% (13 tests needed)

### Critical Gaps

1. src/auth/password_reset.py (0% coverage)
   Risk: CRITICAL - Security code untested
   Recommended Tests (Est. +3.5%):
   - test_generate_reset_token()
   - test_validate_reset_token_expired()
   - test_send_reset_email_failure()

[Provides ready-to-use test code]
```

### Example 3: Test Suggestions

```
/suggest-tests src/payment/process.py::process_payment

# Output:
## Test Suggestions: process_payment()

### Suggested Test Cases

1. test_process_payment_valid_card
2. test_process_payment_declined
3. test_process_payment_timeout
4. test_process_payment_invalid_amount

[Provides complete pytest code for each]

Coverage Impact: 45% → 85% (+40%)
```

## Technology Stack

### Python
- **Testing**: pytest 8.x
- **Coverage**: coverage.py 7.x
- **Linting**: Ruff 0.1.x (replaces Black, isort, flake8)
- **Type Checking**: mypy latest

### TypeScript/JavaScript
- **Testing**: Jest 29.x / Vitest 1.x
- **Component Testing**: React Testing Library 14.x
- **Linting**: ESLint 8.x with typescript-eslint
- **Type Checking**: TypeScript 5.x
- **Coverage**: Istanbul / c8

## Best Practices

### Testing Pyramid Ratios
✅ Unit: 70-80%
✅ Integration: 15-20%
✅ E2E: 5-10%

### Coverage Targets
✅ Backend (Python): ≥80%
✅ Frontend (JS/TS): ≥70%
✅ Security-critical paths: 100%

### Cyclomatic Complexity
✅ Target: <10
🟡 Review: 11-20
❌ Refactor: >20

### Code Review
✅ Fix CRITICAL security issues immediately
✅ Address HIGH priority violations before merge
🟡 Plan MEDIUM issues for next sprint
⚪ LOW issues optional

## Anti-Patterns

### Testing
❌ Testing implementation details
❌ Interdependent tests
❌ Over-mocking internal logic
❌ Ignoring edge cases
❌ No async testing (missing await, waitFor)

### Code Quality
❌ Hardcoded secrets (S105, S106)
❌ Use of eval (S307)
❌ Mutable default arguments (B006)
❌ Overuse of `any` type
❌ Array index as React key

## Troubleshooting

### Hook Script Errors

**Issue**: `quality_gate.py` fails with "Tool not found"

**Solution**:
```bash
# Install missing tools
pip install ruff mypy  # Python
npm install -g eslint typescript  # JS/TS
```

**Issue**: Coverage validator can't find report

**Solution**:
```bash
# Ensure coverage report is generated
pytest --cov=src --cov-report=json

# Or specify path
export COVERAGE_REPORT_PATH=coverage/coverage.json
```

### Exit Code 2 Blocking

**Issue**: Quality gate blocks but I need to proceed

**Solution**: Fix the violations! Exit Code 2 is designed to block.
If absolutely necessary (emergency hotfix):
```bash
# Temporarily disable hooks (NOT RECOMMENDED)
# Edit hooks.json and comment out PostToolUse hook
```

## Integration with CI/CD

### GitHub Actions

```yaml
- name: Run quality gate
  run: |
    python3 .claude/plugins/agentient-quality-assurance/scripts/quality_gate.py src/

- name: Check coverage
  run: |
    pytest --cov=src --cov-report=json
    python3 .claude/plugins/agentient-quality-assurance/scripts/coverage_validator.py
```

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: quality-gate
        name: Quality Gate
        entry: python3 .claude/plugins/agentient-quality-assurance/scripts/quality_gate.py
        language: system
        pass_filenames: true
```

## Dependencies

### Required
- **agentient-security**: OWASP vulnerability patterns, CWE mapping

### Optional
- **agentient-devops-gcp**: CI/CD pipeline integration
- **agentient-python-core**: Python best practices (foundational)
- **agentient-frontend-foundation**: React patterns (foundational)

## Contributing

This plugin follows vibekit quality standards:
- Quality Threshold: 99%
- Exit Code 2 blocking for deterministic enforcement
- Token efficiency via script-based validation
- 3-tier progressive disclosure for skills

## License

Part of the vibekit Claude Code plugin marketplace.

---

**Generated with Claude Code** | Version 1.0.0 | Confidence 99%
