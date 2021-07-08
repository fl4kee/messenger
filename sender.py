import requests

name = input('Введите имя: ')
while True:
    text = input()
    r = requests.post('http://localhost:5000/send',
                      json={'text':text, 'name': name})
