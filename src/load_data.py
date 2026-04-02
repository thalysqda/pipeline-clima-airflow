from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(env_path)

user = os.getenv('user')
password = os.getenv('password')
database = os.getenv('database')
#host = 'host.docker.internal'
host = 'localhost'

def get_engine():
    logging.info(f"→ Conectando em {host}:5432/{database}")
    return create_engine(
        f"postgresql+psycopg2://{user}:{quote_plus(password)}@{host}:5432/{database}"
    )
    
engine = get_engine()

def load_weather_data(table_name:str, df):
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append',
        index=False
    )
    
    logging.info(f"✅ Dados carregados com sucesso!\n") 
    
    df_check = pd.read_sql(f'SELECT * FROM {table_name}', con=engine)
    logging.info(f"Total de registros na tabela: {len(df_check)}\n")

# --- BLOCO DE TESTE FINAL ---
if __name__ == "__main__":
    from transform import data_transformations
    
    try:
        logging.info("=== INICIANDO PIPELINE DE TESTE ===")
        # 1. Roda a extração e transformação (Traz o DataFrame pronto)
        df_final = data_transformations()
        
        # 2. Carrega no PostgreSQL
        if not df_final.empty:
            load_weather_data(table_name="sao_paulo_weather", df=df_final)
        else:
            logging.warning("O DataFrame está vazio!")
            
    except Exception as e:
        logging.error(f"Erro no pipeline: {e}")