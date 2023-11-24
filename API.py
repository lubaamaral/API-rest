import requests
import csv

# definindo variáveis para autenticar a solicitação HTTP
username = 'name'
password = 'password'
url = 'https://.com'

# definindo um dict com parâmetros da consulta. define a quantidade de linhas retornadas para 1 (ajustável)
params = {
    'sysparm_limit': '1'
}

# solicitação GET pra URL, fornecendo username e password + o parametro
response = requests.get(url, auth=(username, password), params=params)

# verifica se o status é 200, nesse caso deu certo
if response.status_code == 200:

    data = response.text.splitlines() # splitlines() dá uma lista de strings, onde cada uma é uma linha CSV
    reader = csv.DictReader(data) # lê o arquivo CSV como dicionário

    rows = list(reader) # lista de dicionário para converter o leitor reader

    if len(rows) > 0:

        header = list(rows[0].keys()) #armazena dados da lista rows, se houver

        with open('problemas.csv', 'w', newline='') as file: # abre o arquivo em modo gravação

            writer = csv.DictWriter(file, fieldnames=header)

            writer.writeheader()
            writer.writerows(rows)

        print('concluido')

    else:
        print('não encontrado.')

else:

    print('erro ', response.status_code)