import mysql.connector
from email.mime.text import MIMEText
import os
import random
from datetime import datetime
from db_secrets import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, EMAIL_USER

def send_fake_email(to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = to_email

    # Ensure the mail directory exists
    mail_dir = '/mail'
    os.makedirs(mail_dir, exist_ok=True)

    # Save email to a uniquely named text file
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{mail_dir}/fake_email_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(msg.as_string())
    
    print(f"Fake email saved to {filename}.")

def insert_transaction(time, status, f1):
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    query = ("INSERT INTO transactions_1 (time, status, f1) "
             "VALUES (%s, %s, %s)")
    cursor.execute(query, (time, status, f1))
    conn.commit()
    cursor.close()
    conn.close()

def check_anomalies():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM transactions_1 WHERE status IN ('failed', 'reversed', 'denied')")
    result = cursor.fetchone()

    if result[0] > 5:  # Adjust threshold as necessary
        send_fake_email("tdsantos.cloud@gmail.com", "Alerta de Anomalia", "Uma anomalia foi detectada nas transações.")

    cursor.close()
    conn.close()

def main():
    # Generate sample data
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status_options = ['approved', 'failed', 'reversed', 'denied']
    status = random.choice(status_options)
    f1 = random.randint(1, 100)

    # Insert the transaction
    insert_transaction(current_time, status, f1)

    # Check for anomalies
    check_anomalies()

if __name__ == "__main__":
    main()
