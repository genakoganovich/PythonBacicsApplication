import requests

answer = {True: 'Interesting', False: 'Boring'}

with open('3.5.1.input.txt', 'r') as f:
    numbers = map(lambda x: int(str(x).strip()), f.readlines())

for n in numbers:
    res = requests.get(f'http://numbersapi.com/{n}/math?json=true')
    print(answer[res.json()['found']])