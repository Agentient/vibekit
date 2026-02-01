---
name: security-testing
version: "0.1"
description: >
  [STUB - Not implemented] Security testing strategies including vulnerability scanning and penetration testing guidance.
  PROACTIVELY activate for: [TODO: Define on implementation].
  Triggers: [TODO: Define on implementation]
core-integration:
  techniques:
    primary: ["[TODO]"]
    secondary: []
  contracts:
    input: "[TODO]"
    output: "[TODO]"
  patterns: "[TODO]"
  rubrics: "[TODO]"
---

# Security Testing

> **STUB: This skill is not yet implemented**
>
> This placeholder preserves the documented plugin structure.
> See parent plugin README for planned capabilities.

## Planned Capabilities

- **Vulnerability Scanning**: Automated CVE detection in dependencies
- **SAST**: Static Application Security Testing patterns
- **DAST**: Dynamic Application Security Testing guidance
- Penetration testing methodology
- Security regression testing
- CI/CD security gate integration

## Anti-Patterns to Detect

- String concatenation for SQL queries
- No ownership verification for resource access
- Missing CSRF protection on state-changing operations
- Verbose error messages exposing stack traces
- Default/hardcoded credentials
- Disabled security features (CORS allow-all, CSRF disabled)
- Using `eval()` with user input
- Missing security headers (CSP, HSTS, X-Frame-Options)

## Implementation Status

- [ ] Core implementation
- [ ] References documentation
- [ ] Output templates
- [ ] Integration tests
