import requests

resp = requests.get('https://brevvi-burger-api.herokuapp.com/burgers')
if resp.status_code != 200:
    # retorno em caso de erro
    raise ApiError('GET /task/ {}'.forma(resp.status_code))
for item in resp.json():
    print('{} {} {}'.format(item['id'], item['restaurante'], item['web']))

