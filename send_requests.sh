#!/bin/bash

# Defina o URL do endpoint
URL="http://localhost:5000/add_transaction"

# Loop infinito para enviar requisições
while true; do
    # Gera um timestamp atual no formato adequado
    TIME=$(date +'%Y-%m-%d %H:%M:%S')
    
    # Gera um valor aleatório para f1
    F1=$(( RANDOM % 100 + 1 ))

    # Envia a requisição POST
    curl -X POST "$URL" -H "Content-Type: application/json" -d "{\"time\": \"$TIME\", \"f1\": $F1}"

    # Aguarda um segundo antes de enviar a próxima requisição
    sleep 1
done
