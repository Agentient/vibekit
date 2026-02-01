# Agentient Observability Plugin

Production-grade observability plugin for implementing structured logging, distributed tracing (OpenTelemetry), error tracking (Sentry), and SRE practices across Next.js 14+, Python, and serverless applications.

## Overview

The `agentient-observability` plugin transforms Claude Code into an expert observability engineer capable of implementing comprehensive monitoring, logging, and tracing systems that enable rapid incident diagnosis and resolution.

## Key Capabilities

- **Structured Logging**: Unified JSON logging across Next.js, Python, and Firebase Functions
- **Distributed Tracing**: OpenTelemetry instrumentation for end-to-end request tracking
- **Error Tracking**: Sentry integration for comprehensive error monitoring
- **Context Propagation**: W3C TraceContext propagation across service boundaries
- **SRE Practices**: SLO/SLI definition, error budgets, and monitoring
- **Cost Optimization**: Intelligent log and trace sampling strategies
- **Actionable Alerting**: Alert policies with runbooks to prevent alert fatigue

## Installation

This plugin is part of the vibekit marketplace and is automatically available when the marketplace is installed.

### Dependencies

- `agentient-python-core` - Python backend fundamentals
- `agentient-devops-gcp` - GCP infrastructure knowledge

## Commands

### `/setup-logging`

Set up structured JSON logging across all platforms.

```bash
/setup-logging           # Full-stack setup
/setup-logging nextjs    # Next.js only
/setup-logging python    # Python only
/setup-logging firebase  # Firebase Functions only
```

### `/add-error-tracking`

Integrate Sentry for error and performance monitoring.

```bash
/add-error-tracking        # Full-stack integration
/add-error-tracking nextjs # Next.js only
/add-error-tracking python # Python only
```

### `/setup-tracing`

Implement OpenTelemetry distributed tracing.

```bash
/setup-tracing           # Full-stack tracing
/setup-tracing nextjs    # Next.js only
/setup-tracing python    # Python only
```

### `/create-alerts`

Create SLO-based alerts with runbooks.

```bash
/create-alerts           # Comprehensive alerting
/create-alerts slo       # Focus on SLO definition
/create-alerts errors    # Error-focused alerts
```

## Agent

The **observability-engineer** agent is activated automatically for observability-related tasks.

## Skills

### Always-Loaded (Core Foundation)
- **cross-platform-structured-logging**
- **nextjs-opentelemetry-instrumentation**
- **python-backend-opentelemetry-instrumentation**
- **distributed-tracing-context-propagation**

### On-Demand (Advanced Features)
- **full-stack-error-tracking-with-sentry**
- **serverless-slo-definition-monitoring**
- **cost-optimized-log-trace-sampling**
- **actionable-alerting-runbook-design**

## Quick Start

### 1. Structured Logging (5 minutes)

```bash
/setup-logging
```

Establishes JSON logging with unified schema across all platforms.

### 2. Error Tracking (10 minutes)

```bash
/add-error-tracking
```

Integrates Sentry for immediate error visibility.

### 3. Distributed Tracing (15 minutes)

```bash
/setup-tracing
```

Implements OpenTelemetry for end-to-end request tracking.

### 4. SLOs & Alerts (20 minutes)

```bash
/create-alerts
```

Defines SLOs and creates actionable alerts with runbooks.

## Technology Stack

- **Logging**: Pino (Node.js), structlog (Python), firebase-functions/logger
- **Tracing**: OpenTelemetry, Google Cloud Trace
- **Error Tracking**: Sentry
- **Monitoring**: Google Cloud Monitoring
- **Standards**: W3C TraceContext, JSON structured logging

## Observability Maturity Levels

**Level 1: Ad-hoc** (Starting point)
- console.log debugging
- No structured logging
- Manual error checking

**Level 2: Foundational** (Minimum target)
- ✓ Structured JSON logs
- ✓ Centralized log aggregation
- ✓ Basic error tracking

**Level 3: Observable** (Recommended)
- ✓ Distributed tracing
- ✓ Log-trace correlation
- ✓ Context propagation
- ✓ Metrics and dashboards

**Level 4: Reliable** (Production-ready)
- ✓ Defined SLOs/SLIs
- ✓ Alert policies with runbooks
- ✓ Error budget tracking
- ✓ Sampling strategies

This plugin helps you reach Level 3-4 quickly.

## Examples

### Example 1: Debugging Slow Request

With proper observability:
1. User reports slow page → Check Sentry performance
2. Get trace_id from Sentry → Search traces
3. Find slow span (e.g., database query 2s)
4. Search logs by trace_id → See query details
5. Optimize query → Verify improvement

### Example 2: Tracking Intermittent Error

With proper observability:
1. Sentry alerts on error rate spike
2. Error includes trace_id, user_id, breadcrumbs
3. Follow trace across services
4. Identify failure point (Cloud Run 5xx)
5. Check logs → Find auth error
6. Fix IAM permissions → Verify error rate drops

## Best Practices

1. **Start with logging**: Foundation for everything else
2. **Verify correlation**: Ensure logs and traces link via trace_id
3. **Monitor costs**: Implement sampling for high-traffic services
4. **Document runbooks**: Every alert needs an actionable runbook
5. **Review regularly**: Update SLOs and alerts based on actual traffic

## Version

1.0.0

## License

Copyright © 2024 Agentient Labs. All rights reserved.

## Support

For issues, questions, or contributions, contact Agentient Labs at contact@agentient.dev.
