# Review Code Command

Perform comprehensive automated code review with security analysis, anti-pattern detection, and refactoring recommendations.

## Purpose

This command activates the code-reviewer-agent to analyze code quality, identify violations, and provide actionable feedback across Python and TypeScript/JavaScript codebases.

## How It Works

1. **Trigger Quality Gate**: Runs `quality_gate.py` on specified file(s)
2. **Collect Violations**: Parses JSON output from Ruff, mypy, ESLint, tsc
3. **Analyze Context**: Loads security patterns from agentient-security
4. **Generate Review**: Produces prioritized, actionable feedback
5. **Provide Fixes**: Includes before/after code examples

## Usage

### Single File Review
```
/review-code src/auth.py
```

### Multiple Files
```
/review-code src/auth.py src/utils.py components/LoginForm.tsx
```

### Directory Review
```
/review-code src/
```

## Review Output Structure

```markdown
## Code Review Summary

**Files Analyzed**: 3
**Total Violations**: 12
- 🔴 Critical: 2
- 🟡 High: 4
- 🟠 Medium: 3
- ⚪ Low: 3

---

### 🔴 Critical Issues (MUST FIX)

#### src/auth.py:45 - S105: Hardcoded Password
**Tool**: Ruff (flake8-bandit)
**Severity**: CRITICAL - Security Violation

**Code**:
```python
45 | password = "admin123"  # ❌ Exposed credential
```

**Risk**: Hardcoded credentials can be extracted from:
- Git history
- Compiled bytecode
- Memory dumps
- Accidental logging

**Fix**:
```python
import os
password = os.getenv("ADMIN_PASSWORD")
if not password:
    raise ValueError("ADMIN_PASSWORD environment variable required")
```

**Security Reference**: CWE-798 (Use of Hard-coded Credentials)

---

#### components/UserProfile.tsx:89 - react/no-danger
**Tool**: ESLint
**Severity**: CRITICAL - XSS Vulnerability

**Code**:
```tsx
89 | <div dangerouslySetInnerHTML={{__html: userBio}} />
```

**Risk**: Unsanitized HTML can execute malicious scripts:
```javascript
userBio = "<img src=x onerror='alert(document.cookie)'>"
```

**Fix**:
```tsx
import DOMPurify from 'dompurify';

const sanitizedBio = DOMPurify.sanitize(userBio);
<div dangerouslySetInnerHTML={{__html: sanitizedBio}} />

// Or better: Use markdown
import ReactMarkdown from 'react-markdown';
<ReactMarkdown>{userBio}</ReactMarkdown>
```

---

### 🟡 High Priority Issues

[Additional violations...]

---

### Recommendations

1. **Security Audit**: 2 critical vulnerabilities require immediate attention
2. **Code Complexity**: `process_payment()` has CC=18, consider refactoring
3. **Test Coverage**: `src/auth.py` has 45% coverage, add tests for security-critical paths
4. **Type Safety**: Enable `--strict` mode in mypy for stronger guarantees

---

### Next Steps

1. Fix 2 critical security issues
2. Run `ruff format` to auto-fix formatting
3. Add tests for `src/auth.py` (priority: password validation, token generation)
4. Re-run `/review-code` to verify fixes
```

## Supported Languages

### Python
- **Linter**: Ruff (E, F, B, S, I rules)
- **Type Checker**: mypy
- **Formatter**: Ruff format
- **Security**: flake8-bandit (S rules)

### TypeScript/JavaScript
- **Linter**: ESLint with typescript-eslint
- **Type Checker**: TypeScript compiler (tsc)
- **Security**: ESLint security plugins
- **React**: React Testing Library conventions

## Integration with Quality Gates

This command respects the `quality_gate.py` Exit Code 2 blocking:
- **Exit Code 0**: Review complete, no blocking issues
- **Exit Code 2**: BLOCKING violations found, deployment prevented

Critical violations (security, syntax errors) trigger Exit Code 2.

## Configuration

Environment variables (optional):
- `CODE_REVIEW_SEVERITY_THRESHOLD`: Minimum severity to report (default: WARNING)
- `CODE_REVIEW_MAX_VIOLATIONS`: Limit output (default: 50)

## Anti-Patterns Detected

### Python
- Mutable default arguments (B006)
- Unused loop variables with side effects (B007)
- Hardcoded secrets (S105, S106)
- Unsafe deserialization (S301, S302)
- Use of eval (S307)

### TypeScript/JavaScript
- Overuse of `any` type
- Array index as React key
- Missing error boundaries
- Unhandled promise rejections
- XSS vulnerabilities (dangerouslySetInnerHTML)

## Success Criteria

Review is complete when:
✅ All files analyzed
✅ Violations categorized by severity
✅ Each issue has explanation + fix
✅ Security issues flagged as CRITICAL
✅ Refactoring recommendations provided
✅ Next steps documented
