# Carrega variáveis de ambiente
$env:GOOGLE_APPLICATION_CREDENTIALS = 'C:\Users\aleite\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\Roaming\gcloud\application_default_credentials.json'
$env:KAGGLE_USERNAME = 'allanleite@eng.zz'
$env:KAGGLE_API_KEY = 'KGAT_0214da58ea212220b1b25bda57f9f42f'
$env:GCP_PROJECT_ID = 'janestreet-quantpipeline'

Write-Host "Variaveis de ambiente carregadas"
Write-Host "OK: GOOGLE_APPLICATION_CREDENTIALS"
Write-Host "OK: GCP_PROJECT_ID = $env:GCP_PROJECT_ID"
Write-Host ""

# Executa Terraform passando argumentos
terraform apply -auto-approve
