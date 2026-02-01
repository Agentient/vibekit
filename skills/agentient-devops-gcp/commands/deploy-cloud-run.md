# Deploy to Cloud Run Command

You are deploying a containerized application to Google Cloud Run with production-ready best practices. Follow this structured process to ensure a secure, reliable, and zero-downtime deployment.

## Prerequisites Validation

Before proceeding with the deployment, you MUST validate these prerequisites:

### 1. Container Image
- **Verify image exists** in Google Artifact Registry or Container Registry
- **Check image tag** is immutable (use Git SHA or semantic version, NOT `:latest`)
- **Scan for vulnerabilities** using `gcloud artifacts docker images scan`
- **Block if CRITICAL vulnerabilities** are found

Command to verify:
```bash
# Check image exists
gcloud artifacts docker images describe IMAGE_URL

# Scan for vulnerabilities
gcloud artifacts docker images scan IMAGE_URL --remote

# Check scan results
gcloud artifacts docker images list-vulnerabilities SCAN_ID \
  --format='table(vulnerability.effectiveSeverity,vulnerability.cvssScore)'
```

### 2. Service Account
- **Verify dedicated service account** exists for this service
- **Check IAM permissions** follow least-privilege principle
- **Validate NO basic roles** (Owner/Editor) are granted
- **Confirm Secret Manager access** is configured if secrets are used

Command to verify:
```bash
# Check service account exists
gcloud iam service-accounts describe SA_EMAIL

# List IAM roles
gcloud projects get-iam-policy PROJECT_ID \
  --flatten="bindings[].members" \
  --filter="bindings.members:serviceAccount:SA_EMAIL" \
  --format="table(bindings.role)"
```

### 3. Secrets Configuration
- **ALL secrets MUST be in Secret Manager** (never environment variables)
- **Verify secret versions** are pinned (not using `:latest` in production)
- **Check IAM permissions** for secret access

Command to verify:
```bash
# List secrets
gcloud secrets list

# Check secret access
gcloud secrets get-iam-policy SECRET_NAME
```

### 4. Current Service Health
- **Check existing service** is healthy before deploying new version
- **Review current traffic split** and revision status
- **Document current revision** for rollback purposes

Command to verify:
```bash
# Check service health
SERVICE_URL=$(gcloud run services describe SERVICE_NAME \
  --region=REGION --format='value(status.url)')
curl -f $SERVICE_URL/health

# Check current revisions
gcloud run revisions list --service=SERVICE_NAME --region=REGION
```

## Deployment Strategy Selection

Choose the appropriate deployment strategy based on service criticality:

### Strategy 1: Blue-Green (Recommended for Production)
**Use when**: High-traffic production service, zero-downtime required, full validation needed

**Process**:
1. Deploy new revision with `--no-traffic` flag
2. Validate health checks on new revision using tagged URL
3. Run smoke tests against new revision
4. Monitor metrics for 2-5 minutes
5. Atomically shift 100% traffic to new revision
6. Keep old revision for instant rollback

**Command**:
```bash
# Deploy new revision (no traffic)
gcloud run deploy SERVICE_NAME \
  --image=IMAGE_URL \
  --region=REGION \
  --service-account=SA_EMAIL \
  --no-traffic \
  --tag=blue

# Validate (use tagged URL)
# Then shift traffic
gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-tags=blue=100
```

### Strategy 2: Canary (Recommended for Risk Mitigation)
**Use when**: Want gradual rollout, need to monitor metrics incrementally

**Process**:
1. Deploy new revision with `--no-traffic`
2. Shift 10% traffic to new revision
3. Monitor for 10 minutes
4. Gradually increase to 50%, then 100%
5. Monitor at each stage

**Command**:
```bash
# Deploy and shift to 10%
gcloud run deploy SERVICE_NAME \
  --image=IMAGE_URL \
  --region=REGION \
  --service-account=SA_EMAIL \
  --no-traffic \
  --tag=canary

CANARY_REV=$(gcloud run services describe SERVICE_NAME \
  --region=REGION --format='value(status.latestCreatedRevisionName)')

gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-revisions=$CANARY_REV=10,LATEST=90
```

### Strategy 3: Direct (Only for Low-Risk)
**Use when**: Staging environment, non-critical service, small change

**Process**:
1. Deploy directly with traffic
2. Monitor immediately after deployment

**Command**:
```bash
gcloud run deploy SERVICE_NAME \
  --image=IMAGE_URL \
  --region=REGION \
  --service-account=SA_EMAIL
```

## Service Configuration

Generate a complete Cloud Run deployment command with all required flags:

### Mandatory Flags

```bash
gcloud run deploy SERVICE_NAME \
  --image=IMAGE_URL \                          # Full image path with immutable tag
  --region=REGION \                            # e.g., us-central1
  --platform=managed \                         # Use managed Cloud Run
  --service-account=SA_EMAIL \                 # Dedicated, least-privilege SA
  --port=8080 \                                # Container port (default 8080)
  --cpu=1 \                                    # vCPUs (1, 2, 4, 8)
  --memory=512Mi \                             # RAM (128Mi to 32Gi)
  --timeout=300s \                             # Max request timeout (up to 3600s)
  --concurrency=80 \                           # Max concurrent requests per instance
  --min-instances=0 \                          # 0 for cost, >0 for latency-sensitive
  --max-instances=10 \                         # Limit for cost control
  --ingress=internal-and-cloud-load-balancing \ # Or 'all' for public
  --no-allow-unauthenticated                   # Require authentication (default)
```

### Secrets Configuration (MANDATORY if using secrets)

```bash
# Mount secrets as environment variables (less secure)
--update-secrets=DB_PASSWORD=db-password:5,API_KEY=api-key:2

# OR mount as files (more secure)
--update-secrets=/secrets/db-password=db-password:5
```

**NEVER** use `--set-env-vars` for secrets. Always use Secret Manager.

### VPC Configuration (if accessing private resources)

```bash
--vpc-connector=projects/PROJECT/locations/REGION/connectors/CONNECTOR_NAME \
--vpc-egress=private-ranges-only  # Or 'all-traffic'
```

### Labels and Annotations

```bash
--labels=environment=production,team=backend,version=v2 \
--revision-suffix=v2-0-0  # Optional: meaningful revision names
```

## Health Checks Configuration

**MANDATORY**: All Cloud Run services MUST have health checks configured.

### Via gcloud (Limited)
```bash
--no-cpu-throttling  # Keep CPU allocated during idle (for background health checks)
```

### Via service.yaml (Recommended)
Create a `service.yaml` file:

```yaml
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: SERVICE_NAME
spec:
  template:
    metadata:
      annotations:
        autoscaling.knative.dev/minScale: '0'
        autoscaling.knative.dev/maxScale: '10'
    spec:
      serviceAccountName: SA_EMAIL
      containers:
      - image: IMAGE_URL
        ports:
        - containerPort: 8080
        startupProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          failureThreshold: 3
          timeoutSeconds: 3
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          periodSeconds: 10
          failureThreshold: 3
          timeoutSeconds: 3
```

Deploy with:
```bash
gcloud run services replace service.yaml --region=REGION
```

## Post-Deployment Validation

After deployment completes, you MUST perform these validation steps:

### 1. Verify Revision is Ready
```bash
gcloud run revisions describe REVISION_NAME \
  --region=REGION \
  --format='value(status.conditions[0].status)'
# Should output: True
```

### 2. Test Health Endpoint
```bash
SERVICE_URL=$(gcloud run services describe SERVICE_NAME \
  --region=REGION --format='value(status.url)')

curl -f $SERVICE_URL/health | jq .
# Should return 200 OK with health status
```

### 3. Test Critical Endpoints
```bash
# Test API endpoints
curl -f $SERVICE_URL/api/status
curl -f $SERVICE_URL/api/version
```

### 4. Check Error Rate in Logs
```bash
gcloud logging read \
  "resource.type=cloud_run_revision \
   AND resource.labels.service_name=SERVICE_NAME \
   AND severity>=ERROR" \
  --limit=50 \
  --format="table(timestamp,severity,jsonPayload.message)"
```

### 5. Monitor Metrics
Navigate to Cloud Console:
```
https://console.cloud.google.com/run/detail/REGION/SERVICE_NAME/metrics
```

Monitor:
- Request count
- Request latency (p50, p95, p99)
- Error rate
- Container instance count
- CPU and memory utilization

## Rollback Procedure

If deployment fails or shows issues, execute immediate rollback:

### Quick Rollback (< 30 seconds)
```bash
# 1. Identify previous revision
PREVIOUS_REV=$(gcloud run revisions list \
  --service=SERVICE_NAME \
  --region=REGION \
  --format='value(metadata.name)' \
  --limit=2 | tail -n 1)

# 2. Instant traffic shift
gcloud run services update-traffic SERVICE_NAME \
  --region=REGION \
  --to-revisions=$PREVIOUS_REV=100

# 3. Verify health
SERVICE_URL=$(gcloud run services describe SERVICE_NAME \
  --region=REGION --format='value(status.url)')
curl -f $SERVICE_URL/health
```

## Output Required

After completing the deployment, provide:

1. **Deployment Summary**:
   - Service name and region
   - New revision name
   - Image deployed (with full tag)
   - Traffic split status
   - Service URL

2. **Health Check Results**:
   - Health endpoint status (pass/fail)
   - Error count in logs (past 5 minutes)
   - Response time (average)

3. **Rollback Command** (pre-filled):
   ```bash
   gcloud run services update-traffic SERVICE_NAME \
     --region=REGION \
     --to-revisions=PREVIOUS_REVISION=100
   ```

4. **Monitoring Links**:
   - Cloud Console metrics dashboard
   - Cloud Logging query for service
   - Cloud Trace for request analysis

5. **Next Steps**:
   - Recommended monitoring duration
   - Metrics to watch
   - Rollback threshold criteria

## Example Execution

```bash
# Full example for production deployment

# 1. Pre-checks
gcloud artifacts docker images describe \
  us-central1-docker.pkg.dev/my-project/my-repo/api:v2.1.0

# 2. Deploy (blue-green)
gcloud run deploy api-service \
  --image=us-central1-docker.pkg.dev/my-project/my-repo/api:v2.1.0 \
  --region=us-central1 \
  --service-account=api-service@my-project.iam.gserviceaccount.com \
  --port=8080 \
  --cpu=2 \
  --memory=1Gi \
  --timeout=300s \
  --concurrency=80 \
  --min-instances=2 \
  --max-instances=50 \
  --ingress=internal-and-cloud-load-balancing \
  --update-secrets=/secrets/db-url=database-url:5 \
  --vpc-connector=projects/my-project/locations/us-central1/connectors/vpc-conn \
  --labels=environment=production,version=v2-1-0 \
  --no-traffic \
  --tag=v2-1-0

# 3. Validate
curl -f https://v2-1-0---api-service-xxx.a.run.app/health

# 4. Shift traffic
gcloud run services update-traffic api-service \
  --region=us-central1 \
  --to-tags=v2-1-0=100

# 5. Monitor
gcloud logging tail "resource.type=cloud_run_revision \
  AND resource.labels.service_name=api-service" \
  --format="table(timestamp,severity,jsonPayload.message)"
```

## Anti-Patterns to Avoid

❌ **Using `:latest` tag** → Use immutable tags (Git SHA or version)
❌ **Skipping vulnerability scan** → Always scan before deploy
❌ **No health checks** → Always configure startup + liveness probes
❌ **Basic IAM roles** → Use least-privilege custom or predefined roles
❌ **Secrets in env vars** → Always use Secret Manager
❌ **No rollback plan** → Always prepare rollback command before deploy
❌ **Direct to production** → Use blue-green or canary for critical services
❌ **Ignoring logs** → Always check error rate after deployment

## Success Criteria

Deployment is considered successful when:
✅ Pre-deployment checks passed (image scanned, SA validated)
✅ New revision deployed and reached Ready state
✅ Health checks passing on new revision
✅ Traffic shifted according to chosen strategy
✅ Error rate < 1% in first 10 minutes
✅ Response time within acceptable threshold
✅ No increase in error logs
✅ Rollback command prepared and tested
