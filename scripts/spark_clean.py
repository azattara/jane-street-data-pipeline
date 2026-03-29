from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower, coalesce
import sys

def clean_jane_street_data(input_path: str, output_path: str):
    """
    Limpa e valida dados da Jane Street.
    - Remove linhas com valores nulos em colunas críticas
    - Normaliza nomes de colunas
    - Converte tipos de dados
    """
    
    spark = SparkSession.builder \
        .appName("JaneStreetDataCleaning") \
        .getOrCreate()
    
    # Ler dados do bucket raw
    df = spark.read.parquet(input_path)
    
    # Limpeza: remover espaços em branco
    for col_name in df.columns:
        df = df.withColumn(col_name, trim(col(col_name)))
    
    # Normalizar nomes de colunas (lowercase, sem espaços)
    df = df.select([col(c).alias(c.lower().replace(" ", "_")) for c in df.columns])
    
    # Remover linhas com valores nulos em colunas críticas
    critical_columns = ["symbol", "event_timestamp", "bid_price", "ask_price"]
    df = df.dropna(subset=critical_columns)
    
    # Conversão de tipos
    df = df.withColumn("bid_price", col("bid_price").cast("double"))
    df = df.withColumn("ask_price", col("ask_price").cast("double"))
    df = df.withColumn("volume", col("volume").cast("long"))
    
    # Salvar dados processados no bucket processed
    df.write.mode("overwrite").parquet(output_path)
    
    print(f"Dados limpos salvos em {output_path}")
    print(f"Registros processados: {df.count()}")

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    clean_jane_street_data(input_path, output_path)
