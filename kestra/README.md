# Configuração do Projeto Kestra para Jane Street Data Pipeline

## Estrutura de Diretórios
```
kestra/
├── flows/
│   └── jane_street_ingestion.yml
├── config.yml
└── README.md
```

## Pré-requisitos

1. **Kestra instalado e rodando**
   ```bash
   docker run -d -p 8080:8080 kestra/kestra:latest server
   ```

2. **Credenciais Kaggle**
   - Crie uma conta em Kaggle.com
   - Gere uma API Key em Account Settings
   - Exporte como variáveis:
     ```bash
     export KAGGLE_USERNAME="seu_usuario"
     export KAGGLE_API_KEY="sua_chave"
     ```

3. **Autenticação GCP**
   - Configure credenciais de sevice account
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/service-account.json"
   ```

4. **Cluster Dataproc Serverless**
   - O cluster "jane-street-cluster" deve existir no GCP

## Fluxo de Execução

1. **Download Kaggle**: Autenticação e download do dataset da Jane Street
2. **Upload GCS**: Move arquivos para o bucket `{project_id}-raw-data`
3. **Trigger Spark**: Invoca job Spark no Dataproc para limpeza de dados
4. **Finalisação**: Log de sucesso

## Variáveis de Ambiente Necessárias

- `GCP_PROJECT_ID`: ID do projeto GCP
- `KAGGLE_USERNAME`: Usuário Kaggle
- `KAGGLE_API_KEY`: API Key do Kaggle

## Deploy

1. Copie o arquivo `jane_street_ingestion.yml` para a UI do Kestra
2. Configure os secrets na UI
3. Clique em "Execute" para disparar manualmente ou aguarde o agendamento

## Monitoramento

Acesse http://localhost:8080 para visualizar:
- Status das execuções
- Logs em tempo real
- Histórico de execuções
