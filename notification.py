import os
from email.mime.text import MIMEText
import mysql.connector
from datetime import datetime
from db_secrets import EMAIL_USER

def send_fake_email(to_email, subject, body):
    mail_dir = os.path.expanduser('~/mail') 

    # Criar o diretório se não existir
    os.makedirs(mail_dir, exist_ok=True)

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = to_email

    # Nome do arquivo para o email
    email_filename = os.path.join(mail_dir, f'email_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt')

    # Salvar email em um arquivo de texto
    with open(email_filename, 'w') as f:
        f.write(msg.as_string())

    print(f"Fake email saved to {email_filename}.")
