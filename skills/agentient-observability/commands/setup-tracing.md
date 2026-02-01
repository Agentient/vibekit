# Setup Tracing

Implement distributed tracing with OpenTelemetry across Next.js, Firebase Functions, and Python backend services to track requests end-to-end across service boundaries.

## Usage

```bash
/setup-tracing [platform]
```

**Parameters:**
- `platform` (optional): Specific platform - `nextjs`, `firebase`, `python`, or omit for full-stack tracing

## What This Command Does

This command implements distributed tracing infrastructure:

1. **Next.js Tracing**:
   - Configure OpenTelemetry Node SDK in instrumentation.ts
   - Set up automatic instrumentation for HTTP, fetch, and Next.js internals
   - Enable client-side tracing with Web SDK
   - Configure span processors and exporters
   - Set resource attributes (service.name, environment)

2. **Firebase Functions Tracing**:
   - Initialize OpenTelemetry SDK for serverless environment
   - Configure automatic instrumentation
   - Set up OTLP exporter
   - Handle cold start considerations

3. **Python Backend Tracing**:
   - Initialize OpenTelemetry TracerProvider
   - Enable automatic instrumentation (Flask, FastAPI, requests)
   - Configure span processor and exporter
   - Integrate trace IDs with logging

4. **Context Propagation**:
   - Verify W3C TraceContext header propagation
   - Test trace continuity across services
   - Validate parent-child span relationships
   - Debug propagation issues

## Observability Engineer Agent

This command activates the **observability-engineer** agent, which will:

- Analyze service architecture and communication patterns
- Design tracing strategy for your stack
- Implement OpenTelemetry SDK initialization
- Configure automatic and manual instrumentation
- Set up trace exporters (Google Cloud Trace, Jaeger, etc.)
- Verify context propagation across all service boundaries
- Create custom spans for critical business logic
- Integrate trace IDs with logging for correlation

## Expected Output

The agent will provide:

1. **Initialization Files**: OpenTelemetry SDK setup for each platform
2. **Custom Span Examples**: How to create manual spans
3. **Propagation Verification**: Steps to test cross-service tracing
4. **Dashboard Configuration**: Recommended trace visualization setup
5. **Integration Guide**: How to correlate traces with logs
6. **Troubleshooting Guide**: Common propagation issues and fixes

## Examples

```bash
# Full-stack distributed tracing
/setup-tracing

# Next.js only
/setup-tracing nextjs

# Firebase Functions only
/setup-tracing firebase

# Python backend only
/setup-tracing python
```

## Prerequisites

- **Tracing Backend**: Google Cloud Trace, Jaeger, Tempo, or other OTLP-compatible backend
- **Structured Logging**: Recommended to set up logging first for correlation
- **Service Architecture**: Understanding of service communication patterns

## Configuration Files Created

### Next.js
- `instrumentation.ts` - OpenTelemetry initialization
- `lib/tracer.ts` - Tracer utility for custom spans
- `app/providers.tsx` - Client-side tracing provider (if needed)
- `next.config.js` - Updated with experimental.instrumentationHook

### Firebase Functions
- `src/tracing.ts` - OpenTelemetry initialization
- Updated function handlers with tracing

### Python
- `tracing.py` - OpenTelemetry SDK initialization
- Updated `main.py` with tracer setup

## Environment Variables Required

```env
# Google Cloud Trace (if using GCP)
GOOGLE_CLOUD_PROJECT=your-project-id

# Jaeger (if using Jaeger)
OTEL_EXPORTER_JAEGER_ENDPOINT=http://localhost:14268/api/traces

# OTLP Generic
OTEL_EXPORTER_OTLP_ENDPOINT=https://api.honeycomb.io
OTEL_EXPORTER_OTLP_HEADERS=x-honeycomb-team=your-api-key

# Service identification
OTEL_SERVICE_NAME=api
OTEL_SERVICE_VERSION=1.0.0
```

## What Gets Traced

### Automatic Instrumentation

**Next.js**:
- Incoming HTTP requests
- React Server Component rendering
- API route handlers
- Outgoing fetch calls
- Database queries (with appropriate instrumentation)

**Firebase Functions**:
- Function invocations
- HTTP requests/responses
- Outgoing HTTP calls
- Database operations

**Python**:
- Incoming requests (Flask, FastAPI)
- Outgoing HTTP requests
- Database queries (SQLAlchemy, etc.)
- Redis operations

### Manual Spans

The agent will show how to create custom spans for:
- Critical business logic
- External API calls
- Complex calculations
- Batch operations
- Background jobs

## Context Propagation

### How It Works

1. **Request enters Next.js**: Root span created, trace_id generated
2. **Next.js calls Firebase Function**: trace_id propagated via `traceparent` header
3. **Firebase Function calls Python API**: Same trace_id continues
4. **All spans share trace_id**: Complete request flow visible

### Verification

```bash
# Check headers in Next.js
console.log(request.headers.get('traceparent'))
// => 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01

# Log headers in Python
logger.info("Incoming headers", extra={"headers": request.headers})
```

## Trace-Log Correlation

Traces and logs are correlated via `trace_id`:

```json
// Log entry
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "info",
  "message": "Processing order",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "order_id": "order_123"
}
```

In observability UI:
- Click trace → See all logs with that trace_id
- Click log → Navigate to parent trace

## Performance Considerations

**Overhead**: OpenTelemetry adds ~1-5% latency overhead

**Mitigation**:
- Use batch span processor (don't export every span immediately)
- Implement sampling for high-traffic services (see `/setup-sampling`)
- Use async exporters (don't block on export)

## Sampling

For high-traffic applications:

```typescript
// Sample 10% of traces
import { TraceIdRatioBasedSampler } from '@opentelemetry/sdk-trace-base'

const sampler = new TraceIdRatioBasedSampler(0.1)
```

See the `cost-optimized-log-trace-sampling` skill for advanced strategies.

## Best Practices

1. **Name spans clearly**: Use descriptive names (e.g., "db.query.users.findById")
2. **Add attributes**: Include relevant context (user_id, order_id)
3. **Set span status**: Mark spans as OK or ERROR
4. **Record exceptions**: Attach exception details to spans
5. **Mind cardinality**: Don't use high-cardinality values in span names

## Common Issues

### Issue 1: Spans not appearing
**Cause**: Exporter misconfigured or unreachable
**Fix**: Check exporter endpoint and credentials

### Issue 2: Broken trace (missing spans)
**Cause**: Context not propagating
**Fix**: Verify automatic instrumentation is active

### Issue 3: Missing child spans
**Cause**: Parent span ended before children
**Fix**: Ensure parent span waits for async operations

## Notes

- The agent operates in Plan Mode for full-stack tracing setup
- Requires understanding of service architecture
- Trace backends may have different configuration requirements
- Sampling should be implemented for production high-traffic services
- Structured logging should be set up first for best correlation
