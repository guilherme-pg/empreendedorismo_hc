from pymongo import MongoClient
import os

MONGO_URI="mongodb+srv://recon:wDydgBlqUNrjrVDr@cluster0.h4ntq3p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME="hc_db"

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    usuarios = db["usuarios"]
    print("Conexão com MongoDB estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
