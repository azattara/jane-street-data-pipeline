resource "google_bigquery_dataset" "silver" {
  dataset_id = "${replace(var.project_id, "-", "_")}_silver"
  location   = var.region
  description = "Silver layer dataset for Jane Street Market Data"
}

resource "google_bigquery_dataset" "gold" {
  dataset_id = "${replace(var.project_id, "-", "_")}_gold"
  location   = var.region
  description = "Gold layer dataset for Jane Street Market Data"
}
