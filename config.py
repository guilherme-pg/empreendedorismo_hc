import os

class Config:

    SECRET_KEY = os.getenv('S70beda1fd9c5a88cb5068d00bd56cee414eb5b472fc5984ee79c7f899a632c82c37dda2efb7201b3c11f1b1c2')

    # DEBUG: Define o modo de depuração. Deve ser False em produção.
    DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')

    MONGO_URI="mongodb+srv://recon:wDydgBlqUNrjrVDr@cluster0.h4ntq3p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    DB_NAME="hc_db"