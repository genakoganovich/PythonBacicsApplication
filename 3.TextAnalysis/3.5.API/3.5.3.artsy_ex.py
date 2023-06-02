import requests


def get_headers():

    client_id = '461c823454c31d1e69ee'
    client_secret = '043ff9d54db2a49fc59ea3db57c06b7f'

    # инициируем запрос на получение токена
    r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={
                          "client_id": client_id,
                          "client_secret": client_secret
                      })

    # разбираем ответ сервера, достаем токен, создаем заголовок, содержащий наш токен
    return {"X-Xapp-Token": r.json()["token"]}


headers = get_headers()

# инициируем запрос с заголовком
with open('3.5.2.input.txt', 'r', encoding='utf-8') as f:
    art_id_list = map(lambda x: str(x).strip(), f.readlines())

artist_list = list()

for art_id in art_id_list:
    r = requests.get(f"https://api.artsy.net/api/artists/{art_id}", headers=headers)
    j = r.json()
    artist_list.append((j['sortable_name'], j['birthday']))

artist_list = sorted(artist_list, key=lambda element: (element[1], element[0]))

# list(map(lambda x: print(x[0]), artist_list))
with open('3.5.2.output.txt', 'w', encoding='utf-8') as f_out:
    f_out.writelines(list(map(lambda x: f'{x[0]}\n', artist_list)))
# list(map(lambda x: print(x), artist_list))

