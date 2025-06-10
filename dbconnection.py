from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
import os


MONGO_URI = os.getenv("MONGO_URI") 
DB_NAME = os.getenv("DB_NAME")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["usuarios"]
    usuarios = db["usuarios"]
    print("Conexão com MongoDB estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
