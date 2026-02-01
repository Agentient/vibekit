# agentient-devops-gcp

Google Cloud Platform DevOps automation plugin with security-first deployment practices, Cloud Run orchestration, Terraform IaC, and CI/CD pipeline patterns.

## Overview

This plugin provides comprehensive automation for deploying and managing applications on Google Cloud Platform, with a focus on:

- **Security-First Design**: Least-privilege IAM, Secret Manager integration, vulnerability scanning
- **Zero-Downtime Deployments**: Blue-green and canary deployment strategies
- **Infrastructure as Code**: Modular Terraform configurations with remote state
- **Production-Ready CI/CD**: GitHub Actions and Cloud Build pipelines with quality gates

**Confidence Level**: 99%
**Category**: Cross-Cutting
**Version**: 1.0.0

## Components

### Agents

#### 1. devops-engineer-agent
**Purpose**: Infrastructure architecture, Terraform design, GCP resource planning

**Responsibilities**:
- Cloud Run service configuration and optimization
- IAM policy design with least-privilege principle
- VPC network architecture and firewall rules
- Terraform module creation and organization
- Secret Manager integration patterns
- Monitoring and observability setup

**Activation**: Keywords like `infrastructure`, `terraform`, `gcp`, `iam`, `vpc`, `architecture`

**Use Cases**:
- "Design the infrastructure for a production API with database"
- "Create Terraform for a Cloud Run service with VPC access"
- "Configure IAM for a CI/CD pipeline"

#### 2. deployment-agent
**Purpose**: Release management, deployment automation, rollback procedures

**Responsibilities**:
- Blue-green deployments to Cloud Run
- Canary releases with gradual traffic shifting
- Health check validation and smoke testing
- Instant rollback procedures
- Multi-service coordinated deployments

**Activation**: Keywords like `deploy`, `release`, `rollback`, `production`, `traffic split`

**Use Cases**:
- "Deploy this Docker image to production Cloud Run"
- "Do a canary release with 10% → 50% → 100% traffic"
- "Rollback the API service immediately"

### Commands

#### `/deploy-cloud-run`
Deploy containerized applications to Cloud Run with production-ready configuration.

**Features**:
- Pre-deployment validation (image scan, IAM check, secret validation)
- Deployment strategy selection (blue-green, canary, direct)
- Health check configuration enforcement
- Post-deployment validation and monitoring
- Automatic rollback command generation

**Example**:
```
/deploy-cloud-run
Service: api-service
Image: us-central1-docker.pkg.dev/my-project/repo/api:v2.0.0
Strategy: blue-green
```

#### `/setup-cicd`
Generate production-ready CI/CD pipelines for GitHub Actions or Cloud Build.

**Features**:
- Multi-stage pipeline (lint → test → security → build → scan → deploy)
- Workload Identity Federation setup (no service account keys)
- Container vulnerability scanning
- Blue-green deployment integration
- Environment-specific configurations (dev/staging/prod)

**Outputs**:
- `.github/workflows/deploy.yml` for GitHub Actions
- `cloudbuild.yaml` for Google Cloud Build
- IAM configuration commands
- Secret configuration instructions

#### `/configure-iam`
Design least-privilege IAM policies for service accounts and users.

**Features**:
- Service account creation with minimal permissions
- Custom role design for specific needs
- IAM audit and validation commands
- Group-based access management
- Conditional IAM policies for temporary access

**Anti-Patterns Blocked**:
- Basic roles (Owner/Editor) on service accounts
- Service account key creation
- Overly permissive policies

#### `/create-terraform`
Generate modular Terraform infrastructure configurations.

**Features**:
- Remote state backend configuration (GCS)
- Reusable module structure
- Environment separation (dev/staging/prod)
- Variable management with validation
- Lifecycle management for critical resources

**Outputs**:
- Complete Terraform project structure
- Cloud Run service module
- IAM and networking configurations
- Backend and provider setup

### Skills

#### 1. cloud-run-deployment
Expert knowledge on Cloud Run service configuration, scaling, health checks, and traffic management.

**Topics**:
- Deployment strategies (blue-green, canary, direct)
- Scaling configuration (min/max instances, concurrency)
- Health checks (startup and liveness probes)
- Traffic splitting and revision management
- Instant rollback procedures

**Token Estimate**: ~2,900 tokens

#### 2. gcp-services
Comprehensive patterns for IAM, Secret Manager, and VPC networking.

**Topics**:
- Least-privilege IAM policy design
- Service account management
- Secret Manager integration and rotation
- VPC custom network design
- Firewall rule configuration
- VPC connectors for Cloud Run

**Token Estimate**: ~8,000 tokens

#### 3. cicd-patterns
CI/CD pipeline automation with GitHub Actions and Cloud Build.

**Topics**:
- Pipeline stage design (quality → test → security → deploy)
- Workload Identity Federation setup
- Container security scanning
- Automated deployment with validation
- Rollback strategies

**Token Estimate**: ~2,700 tokens

#### 4. infrastructure-as-code
Terraform best practices for GCP infrastructure.

**Topics**:
- Remote state management with GCS backend
- Modular architecture with reusable components
- Variable management and validation
- Lifecycle management for production resources
- Multi-environment strategy

**Token Estimate**: ~3,000 tokens

### Security Hooks

This plugin implements deterministic security gates that **block** dangerous operations using Exit Code 2:

#### PreToolUse Hooks

**1. Dangerous Command Blocker**
Prevents execution of destructive commands:
- `rm -rf`
- `gcloud projects delete`
- `gsutil rm -r`
- `terraform destroy` (without confirmation)
- Resource deletion commands

**2. Secret Leak Prevention**
Scans code before writing to detect hardcoded secrets:
- API keys (40-character alphanumeric)
- Google API keys (AIza...)
- OAuth client IDs
- Service account key paths
- AWS credentials

**Blocks**: Writing files with detected secrets to `.tf`, `.yaml`, `.yml`, `.py`, `.js`, `.ts` files.

#### PostToolUse Hooks

**IAM & Terraform Policy Validator**
Validates infrastructure code after writing:

**Terraform (.tf) checks**:
- ❌ `roles/owner` (basic Owner role)
- ❌ `roles/editor` (basic Editor role)
- ❌ `google_service_account_key` (key creation)

**Cloud Run YAML checks**:
- ⚠️ `--allow-unauthenticated` (public access)
- ⚠️ Missing health checks in production

**Action**: Blocks commit/deployment if violations detected.

#### SessionStart Hook

Displays security status on session initialization:
```
🔐 GCP DevOps Security Hooks Active:
  ✓ Dangerous command blocker
  ✓ Secret leak prevention
  ✓ IAM policy validator
  ✓ Terraform security checks

💡 Use Plan Mode for infrastructure changes
```

## Installation

### Prerequisites

1. **Claude Code 2.0** installed
2. **GCP Project** with billing enabled
3. **gcloud CLI** installed and authenticated
4. **Terraform** 1.5+ (for IaC features)
5. **Docker** 24+ (for container builds)

### Setup

1. Clone or link this plugin to your Claude Code plugins directory:
```bash
# Option 1: Clone into plugins directory
cd ~/.claude/plugins
git clone <vibekit-repo> vibekit
ln -s vibekit/plugins/agentient-devops-gcp ./

# Option 2: Symlink from project
ln -s /path/to/vibekit/plugins/agentient-devops-gcp ~/.claude/plugins/
```

2. Enable the plugin in Claude Code settings:
```json
{
  "plugins": {
    "enabled": ["agentient-devops-gcp"]
  }
}
```

3. Verify installation:
```
/help
```
You should see commands: `/deploy-cloud-run`, `/setup-cicd`, `/configure-iam`, `/create-terraform`

### GCP Configuration

1. **Enable Required APIs**:
```bash
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  secretmanager.googleapis.com \
  cloudbuild.googleapis.com \
  compute.googleapis.com
```

2. **Create Artifact Registry** (for container images):
```bash
gcloud artifacts repositories create my-repo \
  --repository-format=docker \
  --location=us-central1
```

3. **Create State Bucket** (for Terraform):
```bash
gsutil mb -p PROJECT_ID -l us-central1 gs://my-tf-state
gsutil versioning set on gs://my-tf-state
```

## Usage Examples

### Example 1: Deploy to Cloud Run

```
User: Deploy my Python API to Cloud Run

Agent: [Activates devops-engineer-agent]
I'll help you deploy your API to Cloud Run. Let me first validate the prerequisites:

1. Checking if container image exists...
2. Verifying IAM configuration...
3. Validating secrets are in Secret Manager...

Now I'll create a blue-green deployment configuration:

[Generates deployment command with health checks, proper scaling, and security settings]

After deployment, I'll provide:
- Service URL
- Health check validation results
- Rollback command (pre-filled)
- Monitoring dashboard links
```

### Example 2: Setup CI/CD Pipeline

```
User: Create a GitHub Actions pipeline to deploy to Cloud Run on every push to main

Agent: [Activates devops-engineer-agent]
I'll set up a production-ready GitHub Actions pipeline with Workload Identity Federation (no service account keys).

First, I'll configure the GCP prerequisites:
[Shows Workload Identity Pool and Provider creation commands]

Then I'll generate the workflow file with these stages:
1. Lint & Format (Ruff)
2. Test (pytest with coverage)
3. Security Scan (Trivy + gitleaks)
4. Build & Push (Docker to Artifact Registry)
5. Image Scan (Artifact Registry)
6. Deploy to Staging (automated)
7. Deploy to Production (manual approval + blue-green)

[Generates complete .github/workflows/deploy.yml]
```

### Example 3: Create Terraform Infrastructure

```
User: Generate Terraform for a Cloud Run service with VPC access and Cloud SQL

Agent: [Activates devops-engineer-agent with infrastructure-as-code skill]
I'll create a modular Terraform configuration with:

Structure:
- environments/prod/ (environment-specific configs)
- modules/cloud-run/ (reusable Cloud Run module)
- modules/vpc/ (network module with Cloud SQL subnet)
- modules/iam/ (service account module)

Key features:
✓ Remote state in GCS
✓ Least-privilege service account
✓ VPC connector for Cloud SQL access
✓ Secrets from Secret Manager
✓ Health checks configured
✓ prevent_destroy on production resources

[Generates complete Terraform project]
```

### Example 4: Emergency Rollback

```
User: The API service is showing high error rate, rollback immediately!

Agent: [Activates deployment-agent - Direct Mode for emergencies]
🚨 ROLLBACK INITIATED

Identifying previous stable revision...
Found: api-service-00042-xyz

Executing instant rollback:
[Runs traffic shift command]

✅ Rollback complete in 12 seconds
Current status:
- Traffic: 100% on revision api-service-00042-xyz
- Health: ✓ Passing
- Error rate: 0.2% (normal)

Monitor: https://console.cloud.google.com/run/detail/us-central1/api-service/metrics
```

## Best Practices

### Security

✅ **Always use Secret Manager** for credentials (never environment variables)
✅ **Least-privilege IAM** (no Owner/Editor roles on service accounts)
✅ **Scan container images** for vulnerabilities before deployment
✅ **Use Workload Identity Federation** (avoid service account keys)
✅ **Enable VPC for database access** (never public databases)

### Deployment

✅ **Blue-green for production** (zero-downtime deployments)
✅ **Health checks mandatory** (startup + liveness probes)
✅ **Validate before traffic shift** (smoke tests, log checks)
✅ **Keep previous revisions** (for instant rollback)
✅ **Monitor metrics post-deployment** (5-10 minute soak time)

### Infrastructure as Code

✅ **Remote state with locking** (GCS backend mandatory)
✅ **Modular design** (reusable components)
✅ **Variable-driven configuration** (no hardcoded values)
✅ **Lifecycle blocks** (prevent_destroy for production)
✅ **Separate environments** (dev/staging/prod isolation)

### CI/CD

✅ **Multi-stage pipelines** (quality → test → security → deploy)
✅ **Automated testing** (unit + integration)
✅ **Security scanning** (dependencies + container images)
✅ **Manual approval for production** (guard against accidents)
✅ **Notification on failures** (Slack/email alerts)

## Troubleshooting

### Hook Errors

If you see `SECURITY_VIOLATION` or `POLICY_VIOLATION` errors:

1. **Review the error message** - it indicates what was blocked
2. **Fix the violation**:
   - Secrets → Move to Secret Manager
   - IAM → Use predefined or custom roles (not Owner/Editor)
   - Commands → Verify you're not running destructive operations
3. **Retry the operation**

To temporarily disable hooks for debugging (NOT recommended):
```json
{
  "hooks": {
    "enabled": false
  }
}
```

### Deployment Failures

Common issues:

**"Image not found"**
- Verify image exists: `gcloud artifacts docker images list --repository=REPO`
- Check permissions: Service account needs `artifactregistry.reader`

**"Health check failed"**
- Verify `/health` endpoint returns 200 OK
- Check startup time (may need longer timeout)
- Review logs: `gcloud logging read "resource.type=cloud_run_revision"`

**"Permission denied"**
- Check service account has required roles
- Verify IAM policy bindings: `gcloud projects get-iam-policy PROJECT`

## Dependencies

- **agentient-security**: Container vulnerability scanning
- **agentient-quality-assurance**: Test integration patterns
- **agentient-observability**: Monitoring and alerting setup (optional)

## Technology Requirements

| Technology | Minimum Version | Purpose |
|------------|----------------|---------|
| Terraform | 1.5.0 | Infrastructure as Code |
| Docker | 24.0 | Container builds (BuildKit) |
| gcloud CLI | Latest | GCP API access |
| Python | 3.13 | Hook scripts |
| Node.js | 20 LTS | GitHub Actions (if used) |

## Contributing

This plugin follows the vibekit quality standards:

- **Quality Threshold**: 99%
- **Security**: Mandatory Secret Manager, least-privilege IAM
- **Documentation**: All patterns documented with anti-patterns
- **Testing**: All hooks must have test coverage

## License

Part of the vibekit Claude Code plugin marketplace.

## Support

For issues or questions:
- Check troubleshooting section above
- Review plugin specification: `.reference/plugin-specs/plugin_spec_agentient-devops-gcp.md`
- Report bugs in vibekit repository

---

**Generated with Claude Code** | Version 1.0.0 | Confidence 99%
