# Data Engineering Pipeline - Jane Street Market Data

Pipeline de engenharia de dados para ingestão, validação e processamento do dataset **Jane Street Real-Time Market Data Forecasting**.

---

## 📋 Arquitetura

```
     Kaggle Dataset
          ↓
      Kestra Flow
          ↓
   ┌─────┴─────┐
   ↓           ↓
  GCS       BigQuery
(raw-data)  (silver)
   ↓           ↓
Spark Job   (gold)
   ↓
GCS
(processed)
```

---

## 🛠️ Componentes

### 1. **Terraform** (Infraestrutura)
Cria automaticamente na GCP:
- **GCS Buckets:**
  - `janestreet-quantpipeline-raw-data` (dados brutos)
  - `janestreet-quantpipeline-processed-data` (dados processados)
  - `janestreet-quantpipeline-scripts` (scripts)

- **BigQuery Datasets:**
  - `janestreet_quantpipeline_silver` (camada silver)
  - `janestreet_quantpipeline_gold` (camada gold)

### 2. **Kestra** (Orquestração)
Pipeline com 4 etapas:
1. ✅ Autenticar no Kaggle
2. 📥 Fazer download do dataset Jane Street
3. ☁️ Upload para GCS bucket raw
4. ⚡ Trigger Spark Job no Dataproc para limpeza

### 3. **Spark** (Transformação)
Script `spark_clean.py`:
- Remove espaços em branco
- Normaliza nomes de colunas
- Remove valores nulos em colunas críticas
- Converte tipos de dados
- Salva dados limpos em processed bucket

---

## 📦 Pré-requisitos

- [x] Python 3.11+
- [x] Terraform 1.14+
- [x] Kaggle CLI
- [ ] GCP Account com projeto criado
- [ ] Credenciais GCP configuradas
- [ ] Docker (para Kestra)

---

## 🚀 Quick Start

### 1. Autenticar no GCP

```powershell
# Opção A: Usando gcloud CLI (recomendado)
gcloud auth application-default login
gcloud config set project janestreet-quantpipeline

# Opção B: Usando service account JSON
$env:GOOGLE_APPLICATION_CREDENTIALS = "C:\path\to\service-account.json"
```

### 2. Verificar Validação

```powershell
cd "c:\Users\aleite\Documents\Data Engineering\data-engineering-project"
python validate_credentials.py
```

### 3. Provisionar Infraestrutura

```powershell
terraform plan
terraform apply
```

### 4. Iniciar Kestra

```powershell
# Interface Web: http://localhost:8080
docker run -d -p 8080:8080 kestra/kestra:latest server
```

### 5. Fazer Deploy do Flow

- Acesse http://localhost:8080
- Vá para "Editor"
- Cole o conteúdo de `kestra/flows/jane_street_ingestion.yml`
- Configure os secrets:
  - `KAGGLE_USERNAME`
  - `KAGGLE_API_KEY`
  - `GCP_PROJECT_ID`
- Clique "Execute"

---

## 📁 Estrutura de Arquivos

```
.
├── provider.tf                  # Configuração do provider GCP
├── variables.tf                 # Definição de variáveis
├── gcs.tf                      # Recursos GCS
├── bigquery.tf                 # Recursos BigQuery
├── terraform.tfvars            # Valores das variáveis
├── .env                        # Variáveis de ambiente (não commitar)
├── .gitignore                  # Arquivos ignorados no git
├── validate_credentials.py     # Script de validação
├── VALIDATION_REPORT.md        # Relatório de validação
├── kestra/
│   ├── flows/
│   │   └── jane_street_ingestion.yml  # Pipeline Kestra
│   ├── config.yml                      # Configuração Kestra
│   └── README.md                       # Documentação Kestra
├── scripts/
│   └── spark_clean.py          # Script de limpeza Spark
└── README.md                   # Este arquivo
```

---

## 📊 Dados

**Dataset:** Jane Street Real-Time Market Data Forecasting
- **Fonte:** Kaggle (janestreet/jane-street-real-time-market-data-forecasting)
- **Tamanho:** ~8GB
- **Frequência:** Uma execução diária (configurável em Kestra)

---

## 🔒 Segurança

Credenciais são armazenadas em:
- `.env` - Variáveis de ambiente locais (não commitar!)
- `terraform.tfvars` - Valores de variáveis Terraform (não commitar!)
- Secrets do Kestra - Gerenciados via UI

**Arquivo `.gitignore` protege automaticamente estas informações.**

---

## 📝 Próximos Passos

1. **Completar autenticação GCP** (crítico)
2. **Executar `terraform apply`** para criar infraestrutura
3. **Iniciar Kestra** com Docker
4. **Configurar secrets** no Kestra
5. **Disparar primeiro run** do pipeline
6. **Monitorar execução** na UI do Kestra

---

## 🐛 Troubleshooting

### Erro: "No credentials loaded"
```powershell
gcloud auth application-default login
```

### Erro: "Kaggle API not authorized"
Verifique se `~/.kaggle/kaggle.json` tem as credenciais corretas

### Kestra não inicia
```powershell
docker logs $(docker ps -q --filter ancestor=kestra/kestra:latest)
```

---

## 📚 Documentação

- [Terraform GCP Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [Kestra Documentation](https://kestra.io/docs/)
- [Kaggle API](https://www.kaggle.com/docs/api)
- [GCP BigQuery](https://cloud.google.com/bigquery/docs)
- [GCS](https://cloud.google.com/storage/docs)

---

**Criado:** 29/03/2026
**Status:** ✅ Pronto para configuração GCP
