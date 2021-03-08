import requests

task = {"resumo": "tirar a roupa da maquina","descricao": "" }
resp = requests.post("db.json")
if resp.status_code != 201:
    raise ApiError('POST /task/ {}'.format(resp.status_code))
print('Criar tarefa. ID: {}'.formato(resp.json()['id']))
