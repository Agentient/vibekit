# agentient-security

Comprehensive security audit and vulnerability detection covering OWASP Top 10, authentication, secure headers, privacy compliance, and GCP hardening.

**Confidence**: 99% | **Category**: Cross-Cutting | **Version**: 1.0.0

## Key Features

- **OWASP Top 10 2021**: Injection, XSS, broken access control, security misconfiguration, vulnerable components
- **Access Control Auditing**: IDOR detection, RBAC/ABAC patterns, privilege escalation prevention
- **Authentication Security**: JWT validation, session management, OAuth2/OIDC flows
- **Secure Headers**: CSP, HSTS, X-Frame-Options, SameSite cookies
- **Privacy Compliance**: GDPR/CCPA consent management, data minimization
- **GCP Hardening**: IAM least privilege, VPC security, Secret Manager

## OWASP Top 10 2021 Coverage

| Rank | Category | Detection |
|------|----------|-----------|
| A01 | Broken Access Control | IDOR patterns, privilege checks |
| A02 | Cryptographic Failures | Weak hashing, plaintext secrets |
| A03 | Injection | SQL/NoSQL/Command injection, XSS |
| A05 | Security Misconfiguration | Verbose errors, default credentials |
| A06 | Vulnerable Components | CVE scanning in package.json/requirements.txt |
| A07 | Authentication Failures | Weak session mgmt, missing MFA |
| A08 | Data Integrity Failures | Insecure deserialization |
| A09 | Security Logging Failures | Missing audit logs |
| A10 | Server-Side Request Forgery | SSRF via URL params |

## Critical Patterns

### 1. Prevent SQL Injection
```python
# ❌ WRONG - string concatenation
query = f"SELECT * FROM users WHERE id = {user_id}"

# ✅ CORRECT - parameterized query
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

### 2. Prevent IDOR (Broken Access Control)
```typescript
// ❌ WRONG - no ownership check
const post = await db.posts.findById(params.id);

// ✅ CORRECT - verify ownership
const post = await db.posts.findById(params.id);
if (post.authorId !== session.userId) {
  throw new ForbiddenError();
}
```

### 3. XSS Prevention
```typescript
// ❌ WRONG - dangerouslySetInnerHTML
<div dangerouslySetInnerHTML={{__html: userInput}} />

// ✅ CORRECT - React escapes by default
<div>{userInput}</div>

// If HTML needed - sanitize first
import DOMPurify from 'dompurify';
<div dangerouslySetInnerHTML={{__html: DOMPurify.sanitize(userInput)}} />
```

### 4. Secure HTTP Headers
```typescript
// next.config.js
module.exports = {
  async headers() {
    return [{
      source: '/(.*)',
      headers: [
        { key: 'X-Frame-Options', value: 'DENY' },
        { key: 'X-Content-Type-Options', value: 'nosniff' },
        { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains' },
        { key: 'Content-Security-Policy', value: "default-src 'self'; script-src 'self' 'unsafe-inline'" }
      ]
    }];
  }
};
```

### 5. Privacy Consent (GDPR/CCPA)
```typescript
// ❌ WRONG - track before consent
analytics.init();
analytics.track('page_view');

// ✅ CORRECT - check consent first
if (await userConsent.hasAnalyticsConsent()) {
  analytics.init();
  analytics.track('page_view');
}
```

## Components

- **Agent**: security-auditor-agent
- **Commands**: /security-audit, /check-auth, /scan-vulnerabilities, /validate-headers
- **Skills** (7): OWASP code analysis, access control, authentication/session, secure headers, privacy consent, GCP hardening, security testing

## Dependencies

**Required**: agentient-python-core, agentient-frontend-foundation
**Optional**: agentient-devops-gcp

## Anti-Patterns

❌ String concatenation for SQL queries
❌ No ownership verification for resource access
❌ Missing CSRF protection on state-changing operations
❌ Verbose error messages exposing stack traces
❌ Default/hardcoded credentials
❌ Disabled security features (CORS allow-all, CSRF disabled)
❌ Using `eval()` with user input
❌ Missing security headers (CSP, HSTS, X-Frame-Options)

---

**Generated with Claude Code** | Version 1.0.0
