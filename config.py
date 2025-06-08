# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    MONGO_URI = os.getenv("MONGO_URI") 
    DB_NAME = os.getenv("DB_NAME") 
