# Sistema de Monitoramento de Transações

## Introdução
Este projeto implementa um sistema de monitoramento simples com alertas em tempo real para transações financeiras. Ele inclui um endpoint para receber dados de transação, processamento e análise dos dados, detecção de anomalias e sistema de notificação de alertas.

## Estrutura do Projeto
- `endpoint.py`: API Flask para receber e processar dados de transação.
- `db_secrets.py`: Variáveis de ambiente para configuração do banco de dados.
- `grafico_vendas.py`: Script para gerar gráficos a partir dos dados das transações.
- `monitor.py`: Script para monitorar e detectar anomalias nas transações.
- `notification.py`: Script para enviar notificações de anomalias.
- `send_request.sh`: Script para enviar requisições de teste para a API.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.
- `requirements.txt`: Dependências do projeto.
- `README.md`: Documentação do projeto.

## Configuração

### 1. Instalar Dependências

pip install -r requirements.txt


### 2. Configurar Banco de Dados

1. Crie um banco de dados MySQL.
2. Configure as variáveis de ambiente em `db_secrets.py`.
3. Crie a tabela importe os dados checkout_1.csv, checkout_2.csv, transactions_1.csv e transactions_2.csv conforme especificado.

### 3. Executar a API

python endpoint.py


### 4. Enviar Dados de Transação
Execute o script `send_request.sh` para enviar dados de teste para a API:

bash send_request.sh


### 5. Gerar Relatório de Anomalias
Execute o script `monitor.py` para detectar anomalias nas transações:

python monitor.py


### 6. Gerar Gráfico de Vendas

Execute o script `grafico_vendas.py` para gerar um gráfico de vendas:

python grafico_vendas.py

O gráfico será salvo como `grafico_vendas.png`.

### Conclusão

Com esses componentes, você terá um sistema de monitoramento de transações que detecta anomalias e gera alertas em tempo real, além de fornecer uma visualização dos dados de vendas por hora. O sistema é flexível e pode ser expandido conforme necessário.