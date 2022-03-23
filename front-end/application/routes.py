from application import app
from flask import request
import requests

@app.route('/')
def index():
    num = request.args.to_dict()['num']
    response = requests.get(f'http://back-end:5000/get/{num}')
    return response.json()

@app.route('/add')
def add():
    response = requests.post('http://back-end:5000/post', json=request.args.to_dict())
    return response.json()