from pymongo import MongoClient
import os

# URL do MongoDB (local ou Atlas)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
db = client["meu_banco_de_dados"]
