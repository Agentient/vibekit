# Setup CI/CD Pipeline Command

You are creating a production-ready CI/CD pipeline for deploying applications to Google Cloud Run. Choose between GitHub Actions or Google Cloud Build based on the project's version control system and team preferences.

## Pipeline Requirements Analysis

Before generating the pipeline, gather this information:

### 1. Project Context
- **Version Control**: GitHub, GitLab, Bitbucket, or Google Cloud Source Repositories?
- **Application Type**: Python, Node.js, Go, Java, or other?
- **Test Framework**: pytest, Jest, Go test, JUnit, or other?
- **Current Structure**: Existing CI/CD, or starting from scratch?

### 2. Deployment Target
- **GCP Project ID**: Which project for deployment?
- **Region**: us-central1, europe-west1, asia-northeast1, or other?
- **Service Name**: Cloud Run service name
- **Environment Strategy**: Single environment, or dev/staging/prod?

### 3. Security Requirements
- **Vulnerability Scanning**: Enable container image scanning?
- **Secret Management**: Secrets stored in Secret Manager?
- **Code Quality**: Lint and format checks required?
- **Test Coverage**: Minimum coverage threshold?

## Pipeline Architecture

Design a multi-stage pipeline following best practices:

```
┌──────────────────────────────────────────────────────────────┐
│                     CI/CD Pipeline                            │
├──────────────────────────────────────────────────────────────┤
│ Stage 1: Code Quality                                         │
│   → Lint (Ruff/ESLint/golangci-lint)                         │
│   → Format check (Black/Prettier/gofmt)                      │
│   → Type check (mypy/TypeScript)                             │
├──────────────────────────────────────────────────────────────┤
│ Stage 2: Testing                                              │
│   → Unit tests (pytest/Jest/go test)                         │
│   → Coverage report (pytest-cov/Istanbul)                    │
│   → Integration tests                                         │
├──────────────────────────────────────────────────────────────┤
│ Stage 3: Security Scanning                                    │
│   → Dependency vulnerability scan (Snyk/Trivy)               │
│   → Secret leak detection (gitleaks)                         │
│   → SAST (Static Application Security Testing)               │
├──────────────────────────────────────────────────────────────┤
│ Stage 4: Build                                                │
│   → Build Docker image (with BuildKit)                       │
│   → Tag with Git SHA + semantic version                      │
│   → Optimize with multi-stage build                          │
├──────────────────────────────────────────────────────────────┤
│ Stage 5: Container Security                                   │
│   → Scan image vulnerabilities (Artifact Registry)           │
│   → Block if CRITICAL/HIGH vulnerabilities                   │
│   → Verify image signature                                   │
├──────────────────────────────────────────────────────────────┤
│ Stage 6: Deploy to Staging                                    │
│   → Deploy to staging Cloud Run service                      │
│   → Run smoke tests against staging                          │
│   → Validate health checks                                   │
├──────────────────────────────────────────────────────────────┤
│ Stage 7: Deploy to Production (Manual Approval)               │
│   → Require manual approval/tag                              │
│   → Blue-green deployment to production                      │
│   → Monitor metrics                                          │
│   → Auto-rollback on error threshold                         │
└──────────────────────────────────────────────────────────────┘
```

## Option 1: GitHub Actions Pipeline

### Prerequisites Setup

#### 1. Create Workload Identity Federation (Secure Authentication)

**NEVER use service account keys**. Use Workload Identity Federation:

```bash
# Create Workload Identity Pool
gcloud iam workload-identity-pools create "github-pool" \
  --project=PROJECT_ID \
  --location="global" \
  --display-name="GitHub Actions Pool"

# Create Workload Identity Provider
gcloud iam workload-identity-pools providers create-oidc "github-provider" \
  --project=PROJECT_ID \
  --location="global" \
  --workload-identity-pool="github-pool" \
  --display-name="GitHub Actions Provider" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository,attribute.repository_owner=assertion.repository_owner" \
  --attribute-condition="assertion.repository_owner == 'YOUR_GITHUB_ORG'" \
  --issuer-uri="https://token.actions.githubusercontent.com"

# Create Service Account for CI/CD
gcloud iam service-accounts create github-actions-deployer \
  --display-name="GitHub Actions Deployer"

# Grant minimum required permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:github-actions-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/run.developer"

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:github-actions-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"

# Allow GitHub Actions to impersonate the service account
gcloud iam service-accounts add-iam-policy-binding \
  github-actions-deployer@PROJECT_ID.iam.gserviceaccount.com \
  --project=PROJECT_ID \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/github-pool/attribute.repository/YOUR_GITHUB_ORG/YOUR_REPO"

# Get the Workload Identity Provider name (needed for workflow)
gcloud iam workload-identity-pools providers describe "github-provider" \
  --project=PROJECT_ID \
  --location="global" \
  --workload-identity-pool="github-pool" \
  --format="value(name)"
```

#### 2. Configure GitHub Secrets

Set these secrets in your GitHub repository (Settings → Secrets and variables → Actions):

- `GCP_PROJECT_ID`: Your GCP project ID
- `GCP_WORKLOAD_IDENTITY_PROVIDER`: Full provider name from above command
- `GCP_SERVICE_ACCOUNT`: Email of the service account

### GitHub Actions Workflow File

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Cloud Run

on:
  push:
    branches:
      - main          # Production
      - develop       # Staging
  pull_request:
    branches:
      - main

env:
  GCP_PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
  GCP_REGION: us-central1
  SERVICE_NAME: my-service
  ARTIFACT_REGISTRY: us-central1-docker.pkg.dev

jobs:
  # Job 1: Code Quality Checks
  quality:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python  # Adjust for your language
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          pip install ruff mypy pytest pytest-cov

      - name: Lint with Ruff
        run: ruff check .

      - name: Format check with Ruff
        run: ruff format --check .

      - name: Type check with mypy
        run: mypy src/

  # Job 2: Test Suite
  test:
    runs-on: ubuntu-latest
    needs: quality
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests with coverage
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term

      - name: Check coverage threshold
        run: |
          coverage report --fail-under=80

  # Job 3: Security Scanning
  security:
    runs-on: ubuntu-latest
    needs: quality
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          severity: 'CRITICAL,HIGH'
          exit-code: '1'  # Fail on vulnerabilities

      - name: Scan for secrets with gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

  # Job 4: Build and Push Image
  build:
    runs-on: ubuntu-latest
    needs: [test, security]
    if: github.ref == 'refs/heads/main' || github.ref == 'refs/heads/develop'
    permissions:
      contents: read
      id-token: write
    outputs:
      image-url: ${{ steps.build-image.outputs.image-url }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Authenticate to Google Cloud
        id: auth
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Configure Docker for Artifact Registry
        run: gcloud auth configure-docker ${{ env.ARTIFACT_REGISTRY }}

      - name: Build and push image
        id: build-image
        env:
          IMAGE_TAG: ${{ github.sha }}
        run: |
          IMAGE_URL="${{ env.ARTIFACT_REGISTRY }}/${{ env.GCP_PROJECT_ID }}/my-repo/${{ env.SERVICE_NAME }}:${IMAGE_TAG}"

          docker build \
            --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
            --build-arg VCS_REF=${GITHUB_SHA} \
            --tag $IMAGE_URL \
            .

          docker push $IMAGE_URL

          echo "image-url=$IMAGE_URL" >> $GITHUB_OUTPUT

      - name: Scan image with Artifact Registry
        run: |
          gcloud artifacts docker images scan ${{ steps.build-image.outputs.image-url }} --remote

          # Wait for scan to complete (max 2 minutes)
          for i in {1..24}; do
            SCAN_STATUS=$(gcloud artifacts docker images list-vulnerabilities \
              ${{ steps.build-image.outputs.image-url }} \
              --format='value(vulnerability.effectiveSeverity)' 2>/dev/null || echo "SCANNING")

            if [[ "$SCAN_STATUS" != "SCANNING" ]]; then
              break
            fi
            sleep 5
          done

          # Check for CRITICAL vulnerabilities
          CRITICAL_COUNT=$(echo "$SCAN_STATUS" | grep -c CRITICAL || true)
          HIGH_COUNT=$(echo "$SCAN_STATUS" | grep -c HIGH || true)

          if [[ $CRITICAL_COUNT -gt 0 ]]; then
            echo "❌ Found $CRITICAL_COUNT CRITICAL vulnerabilities. Deployment blocked."
            exit 1
          fi

          echo "✅ No CRITICAL vulnerabilities found ($HIGH_COUNT HIGH)"

  # Job 5: Deploy to Staging
  deploy-staging:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/develop'
    environment:
      name: staging
      url: ${{ steps.deploy.outputs.url }}
    permissions:
      contents: read
      id-token: write
    steps:
      - name: Authenticate to Google Cloud
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

      - name: Deploy to Cloud Run (Staging)
        id: deploy
        uses: google-github-actions/deploy-cloudrun@v2
        with:
          service: ${{ env.SERVICE_NAME }}-staging
          region: ${{ env.GCP_REGION }}
          image: ${{ needs.build.outputs.image-url }}
          flags: |
            --service-account=staging-sa@${{ env.GCP_PROJECT_ID }}.iam.gserviceaccount.com
            --min-instances=0
            --max-instances=5

      - name: Run smoke tests
        run: |
          curl -f ${{ steps.deploy.outputs.url }}/health || exit 1
          curl -f ${{ steps.deploy.outputs.url }}/api/status || exit 1

  # Job 6: Deploy to Production (Blue-Green)
  deploy-production:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    environment:
      name: production
      url: ${{ steps.get-url.outputs.url }}
    permissions:
      contents: read
      id-token: write
    steps:
      - name: Authenticate to Google Cloud
        uses: google-github-actions/auth@v2
        with:
          workload_identity_provider: ${{ secrets.GCP_WORKLOAD_IDENTITY_PROVIDER }}
          service_account: ${{ secrets.GCP_SERVICE_ACCOUNT }}

      - name: Set up Cloud SDK
        uses: google-github-actions/setup-gcloud@v2

      - name: Deploy new revision (no traffic)
        run: |
          gcloud run deploy ${{ env.SERVICE_NAME }} \
            --image=${{ needs.build.outputs.image-url }} \
            --region=${{ env.GCP_REGION }} \
            --service-account=prod-sa@${{ env.GCP_PROJECT_ID }}.iam.gserviceaccount.com \
            --min-instances=2 \
            --max-instances=50 \
            --no-traffic \
            --tag=v${{ github.sha }}

      - name: Validate new revision
        run: |
          # Get tagged URL
          TAGGED_URL=$(gcloud run services describe ${{ env.SERVICE_NAME }} \
            --region=${{ env.GCP_REGION }} \
            --format='value(status.traffic[?tag==`v${{ github.sha }}`].url | [0])')

          # Health check
          curl -f $TAGGED_URL/health || exit 1

          # Smoke tests
          curl -f $TAGGED_URL/api/status || exit 1

          echo "✅ New revision validated"

      - name: Shift traffic to new revision
        run: |
          gcloud run services update-traffic ${{ env.SERVICE_NAME }} \
            --region=${{ env.GCP_REGION }} \
            --to-tags=v${{ github.sha }}=100

      - name: Get service URL
        id: get-url
        run: |
          URL=$(gcloud run services describe ${{ env.SERVICE_NAME }} \
            --region=${{ env.GCP_REGION }} \
            --format='value(status.url)')
          echo "url=$URL" >> $GITHUB_OUTPUT

      - name: Monitor deployment
        run: |
          echo "Monitoring deployment for 5 minutes..."
          sleep 300

          # Check error rate
          ERROR_COUNT=$(gcloud logging read \
            "resource.type=cloud_run_revision \
             AND resource.labels.service_name=${{ env.SERVICE_NAME }} \
             AND severity>=ERROR" \
            --limit=100 \
            --format="value(timestamp)" \
            --freshness=5m \
            | wc -l)

          if [[ $ERROR_COUNT -gt 10 ]]; then
            echo "❌ High error rate detected: $ERROR_COUNT errors"
            exit 1
          fi

          echo "✅ Deployment successful. Error count: $ERROR_COUNT"
```

## Option 2: Google Cloud Build Pipeline

### Prerequisites Setup

#### 1. Create Service Account

```bash
# Create service account
gcloud iam service-accounts create cloud-build-deployer \
  --display-name="Cloud Build Deployer"

# Grant permissions
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cloud-build-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/run.developer"

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cloud-build-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:cloud-build-deployer@PROJECT_ID.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
```

#### 2. Enable APIs

```bash
gcloud services enable cloudbuild.googleapis.com \
  artifactregistry.googleapis.com \
  run.googleapis.com \
  secretmanager.googleapis.com
```

### Cloud Build Configuration

Create `cloudbuild.yaml`:

```yaml
# Cloud Build pipeline for Cloud Run deployment
options:
  machineType: 'E2_HIGHCPU_8'
  logging: CLOUD_LOGGING_ONLY
  serviceAccount: 'projects/${PROJECT_ID}/serviceAccounts/cloud-build-deployer@${PROJECT_ID}.iam.gserviceaccount.com'

substitutions:
  _SERVICE_NAME: my-service
  _REGION: us-central1
  _ARTIFACT_REGISTRY: us-central1-docker.pkg.dev
  _IMAGE_NAME: ${_ARTIFACT_REGISTRY}/${PROJECT_ID}/my-repo/${_SERVICE_NAME}:${SHORT_SHA}

steps:
  # Step 1: Run tests
  - id: 'test'
    name: 'python:3.13-slim'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        pip install -r requirements.txt pytest pytest-cov
        pytest --cov=src --cov-report=term --cov-report=xml
        coverage report --fail-under=80

  # Step 2: Lint and format check
  - id: 'lint'
    name: 'python:3.13-slim'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        pip install ruff mypy
        ruff check .
        ruff format --check .
        mypy src/

  # Step 3: Security scan (dependencies)
  - id: 'security-scan'
    name: 'aquasec/trivy'
    args:
      - 'fs'
      - '--severity'
      - 'CRITICAL,HIGH'
      - '--exit-code'
      - '1'
      - '.'

  # Step 4: Build Docker image with caching
  - id: 'build'
    name: 'gcr.io/cloud-builders/docker'
    args:
      - 'build'
      - '--cache-from'
      - '${_IMAGE_NAME}:latest'
      - '--tag'
      - '${_IMAGE_NAME}'
      - '--tag'
      - '${_IMAGE_NAME}:latest'
      - '--build-arg'
      - 'BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ")'
      - '--build-arg'
      - 'VCS_REF=${SHORT_SHA}'
      - '.'

  # Step 5: Push image to Artifact Registry
  - id: 'push'
    name: 'gcr.io/cloud-builders/docker'
    args:
      - 'push'
      - '--all-tags'
      - '${_IMAGE_NAME}'

  # Step 6: Scan image for vulnerabilities
  - id: 'image-scan'
    name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        gcloud artifacts docker images scan ${_IMAGE_NAME} --remote

        # Wait for scan completion
        for i in {1..30}; do
          SCAN_RESULT=$(gcloud artifacts docker images list-vulnerabilities ${_IMAGE_NAME} \
            --format='value(vulnerability.effectiveSeverity)' 2>/dev/null || echo "SCANNING")

          if [[ "$SCAN_RESULT" != "SCANNING" ]]; then
            break
          fi
          sleep 10
        done

        # Check for CRITICAL vulnerabilities
        CRITICAL=$(echo "$SCAN_RESULT" | grep -c CRITICAL || true)

        if [[ $CRITICAL -gt 0 ]]; then
          echo "❌ Found $CRITICAL CRITICAL vulnerabilities"
          exit 1
        fi

        echo "✅ No CRITICAL vulnerabilities found"

  # Step 7: Deploy to Cloud Run (blue-green)
  - id: 'deploy'
    name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        # Deploy new revision (no traffic)
        gcloud run deploy ${_SERVICE_NAME} \
          --image=${_IMAGE_NAME} \
          --region=${_REGION} \
          --service-account=prod-sa@${PROJECT_ID}.iam.gserviceaccount.com \
          --min-instances=2 \
          --max-instances=50 \
          --cpu=2 \
          --memory=1Gi \
          --timeout=300s \
          --concurrency=80 \
          --no-traffic \
          --tag=build-${SHORT_SHA}

        # Get tagged URL
        TAGGED_URL=$(gcloud run services describe ${_SERVICE_NAME} \
          --region=${_REGION} \
          --format='value(status.traffic[?tag==`build-${SHORT_SHA}`].url | [0])')

        # Validate health
        curl -f $TAGGED_URL/health || exit 1
        curl -f $TAGGED_URL/api/status || exit 1

        # Shift traffic
        gcloud run services update-traffic ${_SERVICE_NAME} \
          --region=${_REGION} \
          --to-tags=build-${SHORT_SHA}=100

        echo "✅ Deployment complete"

images:
  - '${_IMAGE_NAME}'
  - '${_IMAGE_NAME}:latest'

timeout: 1800s  # 30 minutes
```

### Set up Build Trigger

```bash
# Create build trigger for main branch
gcloud builds triggers create github \
  --name="deploy-to-production" \
  --repo-name=YOUR_REPO \
  --repo-owner=YOUR_ORG \
  --branch-pattern="^main$" \
  --build-config=cloudbuild.yaml \
  --substitutions=_SERVICE_NAME=my-service,_REGION=us-central1
```

## Monitoring and Notifications

### Slack Notifications

Add to GitHub Actions:
```yaml
- name: Notify Slack
  if: always()
  uses: slackapi/slack-github-action@v1
  with:
    webhook-url: ${{ secrets.SLACK_WEBHOOK_URL }}
    payload: |
      {
        "text": "Deployment ${{ job.status }}: ${{ github.repository }}@${{ github.sha }}"
      }
```

### Email Notifications (Cloud Build)

Configure in Cloud Console: Cloud Build → Settings → Email notifications

## Success Criteria

CI/CD pipeline is complete when:

✅ All stages execute in correct order with dependencies
✅ Quality gates block deployment on failure (tests, lint, security)
✅ Container image is scanned for vulnerabilities
✅ Workload Identity Federation configured (no service account keys)
✅ Blue-green deployment implemented for production
✅ Health checks validated before traffic shift
✅ Rollback procedure documented and tested
✅ Notifications configured (Slack/email)
✅ Pipeline runs successfully on test commit
