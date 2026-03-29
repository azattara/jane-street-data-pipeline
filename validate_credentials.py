#!/usr/bin/env python3
"""
Script de validação de credenciais e conectividade
"""
import os
import json
import subprocess
from pathlib import Path

def validate_kaggle_credentials():
    """Valida credenciais Kaggle"""
    print("=" * 60)
    print("1. VALIDANDO KAGGLE")
    print("=" * 60)
    
    kaggle_config_path = Path.home() / ".kaggle" / "kaggle.json"
    
    # Criar diretório se não existir
    kaggle_config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Criar arquivo de credenciais
    kaggle_config = {
        "username": os.getenv("KAGGLE_USERNAME", "allanleite@eng.zz"),
        "key": os.getenv("KAGGLE_API_KEY", "KGAT_0214da58ea212220b1b25bda57f9f42f")
    }
    
    with open(kaggle_config_path, "w") as f:
        json.dump(kaggle_config, f)
    
    # Definir permissões corretas
    kaggle_config_path.chmod(0o600)
    
    print(f"✓ Arquivo Kaggle criado em: {kaggle_config_path}")
    print(f"✓ Username: {kaggle_config['username']}")
    print(f"✓ API Key configurada")
    print()

def validate_gcp_credentials():
    """Valida credenciais GCP"""
    print("=" * 60)
    print("2. VALIDANDO GCP PROJECT")
    print("=" * 60)
    
    project_id = os.getenv("GCP_PROJECT_ID", "janestreet-quantpipeline")
    print(f"✓ GCP Project ID: {project_id}")
    
    # Verificar se arquivo de credenciais existe
    sa_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if sa_path and Path(sa_path).exists():
        print(f"✓ Service Account JSON encontrado: {sa_path}")
    else:
        print(f"⚠ Service Account JSON não encontrado")
        print(f"  Configure com: $env:GOOGLE_APPLICATION_CREDENTIALS='path/to/service-account.json'")
    print()

def validate_terraform():
    """Valida Terraform"""
    print("=" * 60)
    print("3. VALIDANDO TERRAFORM")
    print("=" * 60)
    
    try:
        result = subprocess.run(
            ["terraform", "--version"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            print(f"✓ Terraform instalado:")
            print(result.stdout.strip())
        else:
            print("✗ Erro ao executar Terraform")
    except FileNotFoundError:
        print("✗ Terraform não instalado")
    print()

def validate_environment_variables():
    """Valida variáveis de ambiente"""
    print("=" * 60)
    print("4. VARIÁVEIS DE AMBIENTE")
    print("=" * 60)
    
    vars_required = {
        "KAGGLE_USERNAME": "allanleite@eng.zz",
        "KAGGLE_API_KEY": "KGAT_0214...",
        "GCP_PROJECT_ID": "janestreet-quantpipeline"
    }
    
    for var, example in vars_required.items():
        value = os.getenv(var)
        if value:
            display_value = value[:10] + "..." if len(value) > 10 else value
            print(f"✓ {var}: {display_value}")
        else:
            print(f"✗ {var}: não configurada")
    print()

def validate_env_file():
    """Valida arquivo .env"""
    print("=" * 60)
    print("5. ARQUIVO .env")
    print("=" * 60)
    
    env_file = Path(".env")
    if env_file.exists():
        print(f"✓ Arquivo .env encontrado")
        with open(env_file) as f:
            for line in f:
                if "=" in line:
                    key = line.split("=")[0]
                    print(f"  - {key} configurado")
    else:
        print("✗ Arquivo .env não encontrado")
    print()

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("VALIDAÇÃO DE CREDENCIAIS - DATA ENGINEERING PIPELINE")
    print("=" * 60 + "\n")
    
    validate_environment_variables()
    validate_kaggle_credentials()
    validate_gcp_credentials()
    validate_terraform()
    validate_env_file()
    
    print("=" * 60)
    print("PRÓXIMOS PASSOS:")
    print("=" * 60)
    print("1. Configure GOOGLE_APPLICATION_CREDENTIALS se necessário")
    print("2. Execute: terraform init")
    print("3. Execute: terraform plan")
    print("4. Inicie Kestra e configure secrets")
    print("=" * 60)
