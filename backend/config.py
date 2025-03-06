from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()

DB_NAME = "prodp_bdd"
DB_USER = "root"  # Utilisateur MySQL
DB_PASSWORD = "pfe2025"  #Mot de passe MySQL
DB_HOST = "localhost"
DB_PORT = "3306"  # Par défaut, MySQL utilise 3306

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False