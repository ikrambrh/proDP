from app import db, app

with app.app_context():
    db.create_all()  # Crée toutes les tables définies dans SQLAlchemy
    print("Base de données initialisée avec succès ! ")