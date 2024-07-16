# Transaction Monitoring System

## Introduction
This project implements a simple monitoring system with real-time alerts for financial transactions. It includes an endpoint for receiving transaction data, data processing and analysis, anomaly detection, and alert notification system.

## Project Structure
- `endpoint.py`: Flask API for receiving and processing transaction data.
- `db_secrets.py`: Environment variables for database configuration.
- `grafico_vendas.py`: Script to generate graphs from transaction data.
- `monitor.py`: Script to monitor and detect anomalies in transactions.
- `notification.py`: Script to send anomaly notifications.
- `send_request.sh`: Script to send test requests to the API.
- `docker-compose.yml`: Docker Compose configuration file.
- `requirements.txt`: Project dependencies.
- `README.md`: Project documentation.

## Settings

### 1. Install Dependencies

pip install -r requirements.txt


### 2. Configure Database

1. Create a MySQL database.
2. Configure environment variables in `db_secrets.py`.
3. Create the table and import the checkout_1.csv, checkout_2.csv, transactions_1.csv and transactions_2.csv data as specified.

### 3. Run the API

python endpoint.py


### 4. Send Transaction Data
Run the `send_request.sh` script to send test data to the API:

bash send_request.sh


### 5. Generate Anomaly Report
Run the `monitor.py` script to detect transaction anomalies:

python monitor.py


### 6. Generate Sales Chart

Run the `grafico_vendas.py` script to generate a sales graph:

python grafico_vendas.py

The graph will be saved as `grafico_vendas.png`.

### Conclusion

With these components, you will have a transaction monitoring system that detects anomalies and generates real-time alerts, as well as providing a view of hourly sales data. The system is flexible and can be expanded as needed.
