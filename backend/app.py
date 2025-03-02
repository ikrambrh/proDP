from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Permet d'éviter les problèmes de CORS

# Configuration de la base de données
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'ma_bdd'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/api/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM table_exemple")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)