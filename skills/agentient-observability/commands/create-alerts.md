# Create Alerts

Create effective alerting policies and runbooks for production monitoring using Google Cloud Monitoring, focusing on SLO-based alerts to prevent alert fatigue and enable rapid incident response.

## Usage

```bash
/create-alerts [focus]
```

**Parameters:**
- `focus` (optional): Specific focus - `slo`, `errors`, `latency`, `saturation`, or omit for comprehensive alerting strategy

## What This Command Does

This command implements production alerting:

1. **SLO Definition**:
   - Define Service Level Indicators (SLIs) for your services
   - Set Service Level Objectives (SLOs) with realistic targets
   - Calculate error budgets
   - Set up SLO monitoring dashboards

2. **Alert Policies**:
   - Create GCP alerting policies for SLO breaches
   - Configure error rate alerts
   - Set up latency threshold alerts
   - Monitor resource saturation
   - Set intelligent thresholds to reduce noise

3. **Notification Channels**:
   - Configure notification routing (email, PagerDuty, Slack)
   - Set up tiered alerting (P1 Critical, P2 Warning)
   - Implement on-call rotation integration

4. **Runbook Creation**:
   - Design actionable runbooks for each alert
   - Include triage steps
   - Document mitigation actions
   - Define escalation paths

## Observability Engineer Agent

This command activates the **observability-engineer** agent, which will:

- Analyze service requirements and traffic patterns
- Recommend appropriate SLIs and SLO targets
- Create GCP alerting policies
- Configure notification channels
- Design runbook templates
- Implement alert consolidation strategies
- Set up dashboards for on-call engineers

## Expected Output

The agent will provide:

1. **SLO Definitions**: Documented SLIs and SLO targets
2. **Alert Policies**: GCP monitoring alert configurations
3. **Runbooks**: Markdown runbook templates with response procedures
4. **Dashboard Configuration**: Monitoring dashboard JSON
5. **Notification Setup**: Channel configuration guide
6. **Validation Steps**: How to test alerts fire correctly

## Examples

```bash
# Comprehensive alerting strategy
/create-alerts

# Focus on SLO definition
/create-alerts slo

# Error-focused alerts
/create-alerts errors

# Latency-focused alerts
/create-alerts latency
```

## Prerequisites

- **Observability Infrastructure**: Tracing and logging should be set up
- **GCP Project**: Access to Google Cloud Monitoring
- **Historical Data**: At least 1-2 weeks of traffic data for baseline
- **On-Call Process**: Defined escalation path

## SLI/SLO Concepts

### Service Level Indicator (SLI)

Quantitative measure of service quality:
- **Availability**: Ratio of successful requests / total requests
- **Latency**: Proportion of requests faster than threshold
- **Throughput**: Requests per second

### Service Level Objective (SLO)

Target for SLI:
- "99.9% of requests should return 2xx/3xx status"
- "95% of requests should complete in < 500ms"

### Error Budget

Acceptable unreliability:
- 99.9% SLO = 0.1% error budget = ~43 minutes downtime/month
- When budget exhausted, focus on reliability over features

## Recommended SLOs

### API Services (Cloud Run, Firebase Functions)

**Availability**:
- Target: 99.9% (good), 99.0% (acceptable)
- Measurement window: 30 days
- SLI: (2xx + 3xx responses) / total valid requests

**Latency**:
- Target: 95% < 500ms (good), 95% < 1000ms (acceptable)
- Measurement window: 30 days
- SLI: Percentage of requests served faster than threshold

### Frontend (Next.js)

**Availability**:
- Target: 99.95%
- SLI: Pages that load successfully

**Performance**:
- Target: 90% LCP < 2.5s, 90% INP < 200ms
- SLI: Core Web Vitals thresholds

## Alert Types

### 1. SLO Burn Rate Alerts

**Best Practice**: Alert on error budget consumption rate

```
Alert if:
  Error budget burn rate > 1.0 over 1 hour (fast burn)
  OR
  Error budget burn rate > 0.1 over 24 hours (slow burn)
```

**Rationale**: Catches both sudden incidents and gradual degradation

### 2. Error Rate Alerts

```
Alert if:
  5xx error rate > 5% over 5 minutes
```

**Use case**: Immediate notification of service failures

### 3. Latency Alerts

```
Alert if:
  p95 latency > 1000ms for 10 minutes
```

**Use case**: Detect performance degradation

### 4. Saturation Alerts

```
Alert if:
  CPU utilization > 80% for 15 minutes
  OR
  Memory usage > 90%
```

**Use case**: Prevent resource exhaustion

## Alert Fatigue Prevention

### 1. Use Intelligent Thresholds

❌ **Bad**: CPU > 50%
✅ **Good**: CPU > 80% for 15 minutes AND error rate increasing

### 2. Tiered Severity

**P1 (Critical)**: Page immediately, SLO breach imminent
**P2 (Warning)**: Notify during business hours, degraded but within SLO
**P3 (Info)**: Log only, no notification

### 3. Alert Consolidation

Group related alerts into single incident:
- All errors from same service → 1 incident
- Multiple instances of same error → 1 alert

### 4. Alert Dependencies

Don't alert on downstream effects:
- If database is down, don't alert on each API endpoint failure
- Alert on root cause only

## Runbook Template

```markdown
# [Service Name] - [Alert Name] Runbook

## Service Overview
- **Service**: api.example.com
- **Owner**: @platform-team
- **Tier**: Critical

## Alert Description
What triggered this alert and why it matters.

## Triage Steps
1. Check [dashboard link] for current metrics
2. Search logs: `trace_id:xyz OR service.name:api`
3. Check recent deployments
4. Verify dependencies (database, external APIs)

## Common Causes
- Recent deployment with bug
- Database connection pool exhausted
- Downstream service failure
- DDoS or traffic spike

## Mitigation Actions

### Immediate (< 5 min)
1. Rollback recent deployment if within last hour
2. Scale up if CPU/memory saturated
3. Enable maintenance mode if critical data issue

### Short-term (< 30 min)
1. Identify root cause from logs/traces
2. Apply hotfix if possible
3. Disable problematic feature flag

### Long-term
1. Fix underlying bug
2. Add monitoring to prevent recurrence
3. Update capacity planning

## Escalation Path
- **Primary**: @oncall-engineer (PagerDuty)
- **Secondary**: @platform-lead
- **Executive**: @CTO (only for P1 lasting > 1 hour)

## Related Links
- [Dashboard](https://console.cloud.google.com/monitoring/dashboards/...)
- [Logs](https://console.cloud.google.com/logs/query?...)
- [Runbook](https://docs.example.com/runbooks/...)
```

## GCP Alert Policy Configuration

### Create via Console

1. Navigate to Cloud Monitoring → Alerting → Create Policy
2. Set condition:
   - Resource: Cloud Run / Cloud Function
   - Metric: Error rate / Latency
   - Threshold: Based on SLO
3. Configure notifications:
   - Add notification channels
   - Set auto-close duration
4. Set documentation: Link to runbook

### Create via Terraform

```hcl
resource "google_monitoring_alert_policy" "api_error_rate" {
  display_name = "API Error Rate High"
  combiner     = "OR"

  conditions {
    display_name = "Error rate > 5%"
    condition_threshold {
      filter          = "resource.type=\"cloud_run_revision\" AND metric.type=\"run.googleapis.com/request_count\""
      duration        = "300s"
      comparison      = "COMPARISON_GT"
      threshold_value = 0.05

      aggregations {
        alignment_period   = "60s"
        per_series_aligner = "ALIGN_RATE"
      }
    }
  }

  documentation {
    content = "See runbook: https://docs.example.com/runbooks/api-error-rate"
  }

  notification_channels = [
    google_monitoring_notification_channel.pagerduty.id
  ]
}
```

## Verification

### Test Alert Fires

1. Trigger condition manually (e.g., generate errors)
2. Verify alert fires within expected time
3. Confirm notification received
4. Verify runbook link works
5. Test auto-close when condition resolves

## Best Practices

1. **Every alert needs a runbook**: No exceptions
2. **Alert on symptoms, not causes**: User impact, not server metrics
3. **Actionable notifications**: Include dashboard/log links
4. **Review regularly**: Remove noisy alerts
5. **Practice incident response**: Run game days

## Notes

- The agent operates in Plan Mode for alerting strategy
- Requires historical traffic data for realistic SLO targets
- Start conservative (lower SLO targets) and tighten over time
- Monitor alert fatigue metrics (alerts per day, MTTR)
- Runbooks should be living documents, updated after each incident
