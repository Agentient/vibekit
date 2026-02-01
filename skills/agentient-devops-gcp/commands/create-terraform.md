# Create Terraform Infrastructure Command

You are generating modular, production-ready Terraform configurations for Google Cloud Platform resources. All Terraform MUST follow best practices: remote state, module organization, and no hardcoded values.

## Project Structure

Generate this directory structure:

```
terraform/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   ├── outputs.tf
│   │   ├── backend.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── prod/
└── modules/
    ├── cloud-run-service/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── vpc-network/
    └── iam-service-account/
```

## Step 1: Configure Remote State Backend

Create `backend.tf` in each environment:

```hcl
terraform {
  backend "gcs" {
    bucket = "my-tf-state-prod"  # Must be created beforehand
    prefix = "terraform/prod"    # Unique per environment
  }

  required_version = ">= 1.5.0"

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}
```

Bootstrap the state bucket (run once):
```bash
# Create state bucket
gsutil mb -p PROJECT_ID -l us-central1 gs://my-tf-state-prod

# Enable versioning
gsutil versioning set on gs://my-tf-state-prod

# Grant access to Terraform service account
gsutil iam ch serviceAccount:terraform@PROJECT.iam.gserviceaccount.com:objectAdmin gs://my-tf-state-prod
```

## Step 2: Define Variables

Create `variables.tf`:

```hcl
variable "project_id" {
  description = "GCP Project ID"
  type        = string
}

variable "region" {
  description = "GCP Region"
  type        = string
  default     = "us-central1"
}

variable "environment" {
  description = "Environment name (dev/staging/prod)"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "service_name" {
  description = "Cloud Run service name"
  type        = string
}

variable "container_image" {
  description = "Container image URL"
  type        = string
}

variable "min_instances" {
  description = "Minimum number of instances"
  type        = number
  default     = 0
}

variable "max_instances" {
  description = "Maximum number of instances"
  type        = number
  default     = 10
}
```

Create `terraform.tfvars`:

```hcl
project_id      = "my-gcp-project"
region          = "us-central1"
environment     = "prod"
service_name    = "api-service"
container_image = "us-central1-docker.pkg.dev/my-project/repo/api:v1.0.0"
min_instances   = 2
max_instances   = 50
```

## Step 3: Create Reusable Modules

### Module: Cloud Run Service

`modules/cloud-run-service/main.tf`:

```hcl
# Cloud Run service module
resource "google_cloud_run_service" "service" {
  name     = var.service_name
  location = var.region

  template {
    spec {
      service_account_name = google_service_account.service.email

      containers {
        image = var.container_image

        ports {
          container_port = var.container_port
        }

        resources {
          limits = {
            cpu    = var.cpu
            memory = var.memory
          }
        }

        dynamic "env" {
          for_each = var.env_vars
          content {
            name  = env.key
            value = env.value
          }
        }
      }

      container_concurrency = var.concurrency
      timeout_seconds       = var.timeout
    }

    metadata {
      annotations = {
        "autoscaling.knative.dev/minScale" = var.min_instances
        "autoscaling.knative.dev/maxScale" = var.max_instances
        "run.googleapis.com/vpc-access-connector" = var.vpc_connector_name != null ? var.vpc_connector_name : null
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  lifecycle {
    prevent_destroy = var.prevent_destroy
  }
}

# Service account for Cloud Run
resource "google_service_account" "service" {
  account_id   = "${var.service_name}-sa"
  display_name = "Service Account for ${var.service_name}"
}

# IAM policy for public access (if needed)
resource "google_cloud_run_service_iam_member" "public" {
  count = var.allow_unauthenticated ? 1 : 0

  service  = google_cloud_run_service.service.name
  location = google_cloud_run_service.service.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}
```

`modules/cloud-run-service/variables.tf`:

```hcl
variable "service_name" {
  description = "Name of the Cloud Run service"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
}

variable "container_image" {
  description = "Container image URL"
  type        = string
}

variable "container_port" {
  description = "Container port"
  type        = number
  default     = 8080
}

variable "cpu" {
  description = "Number of vCPUs"
  type        = string
  default     = "1"
}

variable "memory" {
  description = "Memory allocation"
  type        = string
  default     = "512Mi"
}

variable "concurrency" {
  description = "Maximum concurrent requests per instance"
  type        = number
  default     = 80
}

variable "timeout" {
  description = "Request timeout in seconds"
  type        = number
  default     = 300
}

variable "min_instances" {
  description = "Minimum instances"
  type        = number
  default     = 0
}

variable "max_instances" {
  description = "Maximum instances"
  type        = number
  default     = 10
}

variable "allow_unauthenticated" {
  description = "Allow unauthenticated access"
  type        = bool
  default     = false
}

variable "env_vars" {
  description = "Environment variables"
  type        = map(string)
  default     = {}
}

variable "vpc_connector_name" {
  description = "VPC connector name"
  type        = string
  default     = null
}

variable "prevent_destroy" {
  description = "Prevent accidental destruction"
  type        = bool
  default     = true
}
```

`modules/cloud-run-service/outputs.tf`:

```hcl
output "service_url" {
  description = "Cloud Run service URL"
  value       = google_cloud_run_service.service.status[0].url
}

output "service_account_email" {
  description = "Service account email"
  value       = google_service_account.service.email
}

output "service_name" {
  description = "Service name"
  value       = google_cloud_run_service.service.name
}
```

## Step 4: Main Configuration

`environments/prod/main.tf`:

```hcl
provider "google" {
  project = var.project_id
  region  = var.region
}

# Use the Cloud Run module
module "api_service" {
  source = "../../modules/cloud-run-service"

  service_name     = var.service_name
  region           = var.region
  container_image  = var.container_image
  min_instances    = var.min_instances
  max_instances    = var.max_instances
  cpu              = "2"
  memory           = "1Gi"
  concurrency      = 80
  prevent_destroy  = true

  env_vars = {
    ENVIRONMENT = var.environment
  }
}

# Grant Secret Manager access
resource "google_project_iam_member" "secret_accessor" {
  project = var.project_id
  role    = "roles/secretmanager.secretAccessor"
  member  = "serviceAccount:${module.api_service.service_account_email}"
}
```

## Step 5: Outputs

`environments/prod/outputs.tf`:

```hcl
output "service_url" {
  description = "Cloud Run service URL"
  value       = module.api_service.service_url
}

output "service_account" {
  description = "Service account email"
  value       = module.api_service.service_account_email
}
```

## Execution Workflow

```bash
# 1. Initialize
cd terraform/environments/prod
terraform init

# 2. Validate
terraform validate

# 3. Format
terraform fmt -recursive

# 4. Plan
terraform plan -out=tfplan

# 5. Apply
terraform apply tfplan

# 6. Output
terraform output
```

## Security Checklist

✅ Remote state configured with GCS backend
✅ State bucket has versioning enabled
✅ No secrets in .tf files (use Secret Manager data sources)
✅ Service accounts use least privilege
✅ prevent_destroy set for production resources
✅ Variables validated with validation blocks
✅ Outputs don't expose sensitive data

## Anti-Patterns

❌ Local state file in team projects
❌ Hardcoded project IDs, regions, or credentials
❌ Monolithic main.tf with all resources
❌ Using `:latest` tag for container images
❌ No lifecycle blocks on critical resources
❌ Exposing secrets in outputs

## Success Criteria

✅ Terraform initializes successfully
✅ Terraform plan shows expected changes
✅ Resources created match requirements
✅ Modular structure with reusable components
✅ Remote state working correctly
✅ No sensitive data in version control
