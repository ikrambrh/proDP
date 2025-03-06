from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Importer les modèles après l'initialisation de `db`
#import models 


@app.route("/")
def home():
    return "Serveur Flask fonctionnel ! "

if __name__ == "__main__":
    app.run(debug=True)
