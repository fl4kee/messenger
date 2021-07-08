from flask import Flask, request, abort
import time

app = Flask(__name__)

db = [
    {
        'text': 'hello',
        'name': 'Jack',
        'time': time.time()
    },
    {
        'text': 'hello, Jack',
        'name': 'John',
        'time': time.time()
    }
]

@app.route("/")
def hello():
    return "Hello! <a href='/status'>Status<a>"

@app.route("/status")
def status():
    return {
        'status': True,
        'name': 'Messenger',
        'time': time.time()
    }

@app.route("/send", methods=["POST"])
def send_message():

    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'text' not in data or 'name' not in data:
        return abort(400)

    text = data['text']
    name = data['name']

    # TODO check data is dict with text % name
    # TODO check text & name are valid strings
    if not isinstance(text, str) or not isinstance(name, str):
        return abort(400)
    if len(text) == 0 or len(name) == 0:
        return abort(400)
    if len(text) > 1000 or len(name) > 100:
        return abort(400)


    message = {
        'text': text,
        'name': name,
        'time': time.time()
    }
    db.append(message)

    return{'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    result = []

    for message in db:
        if message['time'] > after:
            result.append(message)
    return {'messages':result[:10]}

app.run()