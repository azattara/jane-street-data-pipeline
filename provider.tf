terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  
  # Use application default credentials
  # Set via environment: gcloud auth application-default login
  # Or set GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
}
