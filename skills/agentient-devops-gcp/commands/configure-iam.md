# Configure IAM Command

You are configuring Google Cloud IAM with strict adherence to the principle of least privilege. All IAM configurations MUST follow security best practices and NEVER grant excessive permissions.

## IAM Policy Design Process

### 1. Identify Requirements

Gather information about what the service or user needs to accomplish:

- **What GCP services** will be accessed? (Cloud Run, Cloud SQL, Secret Manager, Storage)
- **What operations** are required? (read, write, deploy, configure)
- **What resources** are in scope? (specific buckets, databases, secrets)
- **Is this for** a service account, user, or group?

### 2. Select Appropriate Roles

**Priority Order** (most to least restrictive):
1. **Custom Role**: Most restrictive, tailored to exact needs
2. **Predefined Role**: Google-managed, scoped to specific services
3. **Basic Role**: ❌ NEVER use in production (Owner/Editor/Viewer)

### 3. Common IAM Patterns

#### Pattern 1: Cloud Run Service Account

```bash
# Create dedicated service account
gcloud iam service-accounts create SERVICE_NAME-sa \
  --display-name="Service Account for SERVICE_NAME Cloud Run service"

# Grant Secret Manager access
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SERVICE_NAME-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"

# Grant Cloud SQL client access (if using Cloud SQL)
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SERVICE_NAME-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"

# Grant Storage object viewer (if reading from GCS)
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:SERVICE_NAME-sa@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/storage.objectViewer" \
  --condition="resource.name.startsWith('projects/_/buckets/MY-BUCKET')"
```

#### Pattern 2: CI/CD Deployment Service Account

```bash
# Create CI/CD service account
gcloud iam service-accounts create cicd-deployer \
  --display-name="CI/CD Pipeline Deployer"

# Grant Cloud Run deployment permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cicd-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/run.developer"

# Grant Artifact Registry push permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cicd-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"

# Grant service account user (to deploy as other service accounts)
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cicd-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
```

#### Pattern 3: Custom Role for Specific Needs

Create `custom-role.yaml`:
```yaml
title: "Cloud Run Deployer"
description: "Minimum permissions to deploy Cloud Run services"
stage: "GA"
includedPermissions:
- run.services.create
- run.services.get
- run.services.update
- run.services.getIamPolicy
- run.services.setIamPolicy
- run.revisions.get
- run.revisions.list
- iam.serviceAccounts.actAs
```

Apply:
```bash
gcloud iam roles create cloudRunDeployer \
  --project=PROJECT_ID \
  --file=custom-role.yaml

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cicd-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="projects/PROJECT_ID/roles/cloudRunDeployer"
```

### 4. Grant to Groups, Not Individuals

```bash
# Create Google Group: devops-team@example.com
# Grant to group instead of individual users
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="group:devops-team@example.com" \
  --role="roles/run.developer"
```

### 5. Use Conditional IAM Policies

Grant temporary access:
```bash
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="user:contractor@example.com" \
  --role="roles/viewer" \
  --condition='title=Temporary Access,description=Access expires on 2025-12-31,expression=request.time < timestamp("2025-12-31T23:59:59Z")'
```

## IAM Audit and Validation

### Check for Overly Permissive Roles

```bash
# Find all basic roles granted
gcloud projects get-iam-policy PROJECT_ID \
  --flatten="bindings[].members" \
  --filter="bindings.role:(roles/owner OR roles/editor OR roles/viewer)" \
  --format="table(bindings.role,bindings.members)"

# ❌ If any service accounts have Owner/Editor, FIX IMMEDIATELY
```

### Validate Service Account Permissions

```bash
# List all permissions for a service account
gcloud projects get-iam-policy PROJECT_ID \
  --flatten="bindings[].members" \
  --filter="bindings.members:serviceAccount:SA_EMAIL" \
  --format="table(bindings.role)"
```

## Mandatory Security Checks

Before considering IAM configuration complete:

✅ No basic roles (Owner/Editor/Viewer) granted to service accounts
✅ Each service account has only permissions it needs
✅ Permissions granted to groups, not individuals (where possible)
✅ Conditional bindings used for temporary access
✅ Service account keys NOT created (use Workload Identity instead)
✅ IAM policies documented and version-controlled

## Anti-Patterns (NEVER DO THIS)

❌ `roles/owner` or `roles/editor` on service accounts
❌ Project-wide permissions when resource-level would work
❌ Creating service account keys for authentication
❌ Granting permissions to individual users instead of groups
❌ Using default compute service account for Cloud Run
❌ Granting `roles/iam.serviceAccountKeyAdmin` to anyone

## Output Required

Provide:
1. List of service accounts created
2. IAM policy bindings applied
3. Custom roles created (if any)
4. Validation commands to verify permissions
5. Documentation of what each service account can do
