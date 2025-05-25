import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = os.getenv("DB_NAME", "meu_banco_de_dados")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    APP_PORT = int(os.getenv("APP_PORT", 5000))
    