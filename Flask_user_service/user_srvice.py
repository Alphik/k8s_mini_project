from flask import Flask, request
import json

app = Flask(__name__)

users = {}


@app.route('/', methods=['GET'])
def home_page():

    return '/register -> for a new register \n /login -> for login', 201


@app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')

    if not username:
        return 'Username required!', 400

    if not password:
        return 'password is required!' , 400

    if username in users:
        return 'User already exists!', 400

    users[username] = password
    return json.dumps({'message': f'User {username} registered successfully!'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')

    if not username:
        return 'Username required!', 400

    if not password:
        return 'password is required!' , 400

    if users.get(username) == password:
        return json.dumps({'message': f'Hello, {username}!'}), 200
    else:
        return 'Invalid username or password!', 401

app.run(port=5001,host='0.0.0.0')
