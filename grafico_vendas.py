import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from db_secrets import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Criação da URL de conexão compatível com SQLAlchemy
db_url = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Criação do engine SQLAlchemy
engine = create_engine(db_url)

# Consulta SQL compatível com MySQL 5.7
query = """
SELECT 
    STR_TO_DATE(CONCAT('2023-01-01 ', LPAD(REPLACE(time, 'h', ''), 2, '0'), ':00'), '%Y-%m-%d %H:%i:%s') AS time,
    AVG(CAST(today AS DECIMAL(10, 2))) AS avg_today, 
    AVG(CAST(yesterday AS DECIMAL(10, 2))) AS avg_yesterday, 
    AVG(CAST(same_day_last_week AS DECIMAL(10, 2))) AS avg_last_week 
FROM 
    checkout_1
GROUP BY 
    STR_TO_DATE(CONCAT('2023-01-01 ', LPAD(REPLACE(time, 'h', ''), 2, '0'), ':00'), '%Y-%m-%d %H:%i:%s')
ORDER BY 
    time;
"""

# Carregar dados da consulta em um DataFrame
df = pd.read_sql(query, engine)

# Configurar o estilo do seaborn
sns.set(style="whitegrid")

# Criar o gráfico
plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['avg_today'], label='Hoje', marker='o')
plt.plot(df['time'], df['avg_yesterday'], label='Ontem', marker='o')
plt.plot(df['time'], df['avg_last_week'], label='Mesmo Dia da Semana Passada', marker='o')

# Adicionar título e rótulos
plt.title('Média de Vendas por Hora')
plt.xlabel('Hora do Dia')
plt.ylabel('Média de Vendas')
plt.legend()

# Salvar o gráfico como uma imagem
plt.savefig('/home/thiago/cloudwalk/grafico_vendas.png')

# Fechar o plot
plt.close()
