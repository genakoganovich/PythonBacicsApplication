import requests
import json

client_id = '461c823454c31d1e69ee'
client_secret = '043ff9d54db2a49fc59ea3db57c06b7f'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера, достаем токен, создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": r.json()["token"]}

# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
for key, value in r.json().items():
    print(key)
    print(value)
