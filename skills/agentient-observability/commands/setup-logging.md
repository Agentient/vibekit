# Setup Logging

Set up structured JSON logging across Next.js, Python backend services, and Firebase Functions with a unified schema for centralized log aggregation and correlation.

## Usage

```bash
/setup-logging [platform]
```

**Parameters:**
- `platform` (optional): Specific platform - `nextjs`, `python`, `firebase`, or omit for full-stack setup

## What This Command Does

This command implements structured logging infrastructure:

1. **Next.js Logging**:
   - Configure Pino for high-performance JSON logging
   - Set up environment-adaptive formatting (pretty dev, JSON prod)
   - Create request-scoped loggers with automatic context injection
   - Integrate with Next.js API routes and Server Components

2. **Python Logging**:
   - Configure structlog with JSON renderer
   - Integrate with standard logging library
   - Set up log processors for consistent formatting
   - Add automatic context injection (request_id, user_id)

3. **Firebase Functions Logging**:
   - Configure firebase-functions/logger SDK
   - Ensure structured data attachment
   - Leverage automatic execution_id injection
   - Set appropriate log levels

4. **Unified Schema**:
   - Consistent field naming across platforms
   - Standard fields: level, timestamp, message, service.name, trace_id, span_id
   - Correlation keys for linking logs with traces

## Observability Engineer Agent

This command activates the **observability-engineer** agent, which will:

- Analyze existing logging setup (if any)
- Design unified logging schema for your stack
- Implement platform-specific logger configurations
- Set up PII redaction and sensitive data filtering
- Configure log levels appropriate for each environment
- Create example usage patterns for developers

## Expected Output

The agent will provide:

1. **Logger Configuration Files**: Complete config for each platform
2. **Usage Examples**: How to log from different parts of the application
3. **Schema Documentation**: Unified log schema with field descriptions
4. **Integration Guide**: How to integrate loggers into existing code
5. **Verification Steps**: How to validate logging is working correctly

## Examples

```bash
# Full-stack logging setup
/setup-logging

# Next.js only
/setup-logging nextjs

# Python backend only
/setup-logging python

# Firebase Functions only
/setup-logging firebase
```

## Prerequisites

- **Next.js**: Node.js project with package.json
- **Python**: Python 3.11+ project with virtual environment
- **Firebase Functions**: Firebase project with functions directory

## Configuration Files Created

### Next.js
- `lib/logger.ts` - Main logger configuration
- `middleware.ts` - Request logging middleware (if needed)

### Python
- `logging_config.py` - structlog configuration
- `logger.py` - Logger utility module

### Firebase Functions
- `src/utils/logger.ts` - Firebase logger wrapper

## Log Schema

The unified schema includes:

```json
{
  "level": "info",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "message": "User logged in",
  "service": {
    "name": "api",
    "version": "1.0.0"
  },
  "trace_id": "abc123...",
  "span_id": "def456...",
  "user_id": "user_789",
  "request_id": "req_xyz",
  "environment": "production",
  "context": {
    "method": "POST",
    "path": "/api/auth/login"
  }
}
```

## Security Considerations

The agent will configure automatic redaction of:
- Passwords and API keys
- Credit card numbers
- Personal health information
- Full email addresses (optionally hashed)

## Best Practices

1. **Use structured data**: Pass objects, not string interpolation
2. **Set appropriate levels**: DEBUG < INFO < WARN < ERROR
3. **Include context**: request_id, user_id, trace_id when available
4. **Redact PII**: Never log sensitive personal data
5. **Async transports**: Use non-blocking logging in production

## Notes

- The agent operates in Plan Mode for full-stack setups
- Existing logging code may need refactoring for consistency
- Log aggregation (Google Cloud Logging, Datadog) should be configured separately
- This foundation enables log-trace correlation when tracing is added later
