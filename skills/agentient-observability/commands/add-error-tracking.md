# Add Error Tracking

Integrate Sentry for comprehensive error and performance monitoring across Next.js frontend, Server Components, API routes, Firebase Functions, and Python backend services.

## Usage

```bash
/add-error-tracking [platform]
```

**Parameters:**
- `platform` (optional): Specific platform - `nextjs`, `firebase`, `python`, or omit for full-stack integration

## What This Command Does

This command implements Sentry error tracking:

1. **Next.js Integration**:
   - Configure separate Sentry clients for browser, server, and edge runtimes
   - Set up error boundaries for React components
   - Implement automatic error capture for App Router
   - Configure source map uploading for readable stack traces
   - Enable performance monitoring

2. **Firebase Functions Integration**:
   - Configure Sentry SDK for Node.js serverless environment
   - Set up automatic error capture
   - Configure release tracking
   - Enable performance tracing

3. **Python Backend Integration**:
   - Configure Sentry SDK for FastAPI/Flask
   - Set up ASGI/WSGI middleware
   - Enable automatic exception capture
   - Configure performance monitoring

4. **Cross-Platform Features**:
   - User identification and context
   - Trace correlation (links Sentry errors with OpenTelemetry traces)
   - Breadcrumbs for debugging context
   - Release tracking across deployments

## Observability Engineer Agent

This command activates the **observability-engineer** agent, which will:

- Set up Sentry project and obtain DSN
- Create platform-specific configuration files
- Implement error boundaries (React)
- Configure source map uploading
- Set up user context and custom tags
- Integrate with distributed tracing (if enabled)
- Configure performance monitoring thresholds

## Expected Output

The agent will provide:

1. **Configuration Files**: All necessary Sentry config files
2. **Error Boundary Components**: React error boundaries for Next.js
3. **Integration Code**: Middleware and initialization code
4. **Build Configuration**: Source map upload setup
5. **Verification Steps**: How to test error capture
6. **Dashboard Setup**: Recommended Sentry dashboard configuration

## Examples

```bash
# Full-stack Sentry integration
/add-error-tracking

# Next.js only
/add-error-tracking nextjs

# Firebase Functions only
/add-error-tracking firebase

# Python backend only
/add-error-tracking python
```

## Prerequisites

- Sentry account and project (free tier available)
- Sentry DSN (from Sentry project settings)
- For Next.js: Auth token for source map upload

## Configuration Files Created

### Next.js
- `sentry.client.config.ts` - Browser-side configuration
- `sentry.server.config.ts` - Server-side configuration
- `sentry.edge.config.ts` - Edge runtime configuration
- `app/global-error.tsx` - Global error boundary
- `instrumentation.ts` - Sentry initialization (or updated)
- `next.config.js` - Updated with withSentryConfig

### Firebase Functions
- `src/sentry.ts` - Sentry initialization
- Updated function handlers with error capture

### Python
- `sentry_config.py` - Sentry SDK configuration
- Updated `main.py` or `app.py` with initialization

## Environment Variables Required

```env
# Next.js
SENTRY_DSN=https://...@o...ingest.sentry.io/...
SENTRY_AUTH_TOKEN=...  # For source map upload
NEXT_PUBLIC_SENTRY_DSN=https://...  # Public DSN for browser

# Python
SENTRY_DSN=https://...@o...ingest.sentry.io/...
SENTRY_ENVIRONMENT=production
```

## Features Enabled

### Error Capture
- Unhandled exceptions
- Promise rejections
- React component errors
- Server-side errors
- API route errors

### Context
- User identification (user_id, email)
- Custom tags (environment, version)
- Breadcrumbs (user actions, API calls)
- Request context (URL, method, headers)

### Performance Monitoring
- Transaction tracing
- Database query tracking
- External API call monitoring
- Page load performance

### Integrations
- OpenTelemetry (trace correlation)
- Source maps (readable stack traces)
- Release tracking (deploy correlation)
- Session replay (for debugging UX issues)

## Best Practices

1. **Set release**: Track errors by deployment version
2. **Filter noise**: Ignore expected errors (404s, etc.)
3. **Set sample rates**: Adjust for traffic volume
4. **Add context**: User ID, environment, custom tags
5. **Review alerts**: Configure notification rules

## Cost Considerations

Sentry pricing is based on:
- Number of events (errors + transactions)
- Number of replays (session recordings)

**Recommendations**:
- Start with 100% error capture
- Sample performance monitoring (10-25% initially)
- Limit session replay to error sessions only

## Notes

- The agent operates in Plan Mode for full-stack integration
- Source map uploading requires build-time configuration
- Sentry can correlate errors with OpenTelemetry traces
- Performance monitoring is separate from error tracking
- Consider privacy implications of session replay
