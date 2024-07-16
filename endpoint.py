from flask import Flask, request, jsonify
import mysql.connector
import random
from db_secrets import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from notification import send_fake_email  # Importa a função de envio de email
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados
config = {
    'user': DB_USER,
    'password': DB_PASSWORD,
    'host': DB_HOST,
    'database': DB_NAME
}

def insert_transaction(data):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    query = ("INSERT INTO transactions_1 (time, status, f1) "
             "VALUES (%s, %s, %s)")
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    time = data['time']
    
    # Escolhe um status aleatório
    status_options = ['approved', 'failed', 'reversed', 'denied']
    status = random.choice(status_options)
    
    f1 = data['f1']
    insert_transaction((time, status, f1))

    # Verifica anomalias e envia o email
    if status in ['failed', 'reversed', 'denied']:
        send_fake_email("tdsantos.cloud@gmail.com", "Alerta de Anomalia", f"Uma anomalia foi detectada: {status}")

    # Gera uma resposta aleatória
    random_response = {
        "message": "Transaction added successfully!",
        "status": status,
        "f1": f1
    }
    
    return jsonify(random_response), 200

@app.route('/add_transaction', methods=['GET'])
def get_transaction():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Escolhe um status aleatório
    status_options = ['approved', 'failed', 'reversed', 'denied']
    status = random.choice(status_options)
    
    f1 = random.randint(1, 100)  # Gera um valor aleatório para f1
    insert_transaction((current_time, status, f1))

    # Verifica anomalias e envia o email
    if status in ['failed', 'reversed', 'denied']:
        send_fake_email("tdsantos.cloud@gmail.com", "Alerta de Anomalia", f"Uma anomalia foi detectada: {status}")

    # Gera uma resposta aleatória
    random_response = {
        "message": "Transaction added successfully!",
        "status": status,
        "f1": f1
    }
    
    return jsonify(random_response), 200

if __name__ == '__main__':
    app.run(debug=True)
