from application import app
from flask import request, Response, jsonify

people = [{"name":"Alice Smith", "age":27}, {"name":"Bob Jones", "age":34}]

@app.route('/get/<int:index>', methods=['GET'])
def get(index):
    if index - 1 < len(people):
        person = people[index - 1]
        return jsonify(person)
    return jsonify(message="Not Found", status=404), 404

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    people.append(data)
    return jsonify(message="Person added successfully")

@app.route('/put/<int:index>', methods=['PUT'])
def put(index):
    if index - 1 < len(people):
        people[index - 1] = request.get_json()
        return jsonify(message="Updated person")
    return jsonify(message="Not Found", status=404), 404

@app.route('/patch/<int:index>', methods=['PATCH'])
def patch(index):
    if index - 1 < len(people):
        data = request.get_json()
        for k, v in data.items():
            people[index - 1][k] = v
        return jsonify(message="Updated person")
    return jsonify(message="Not Found", status=404), 404

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    if index - 1 < len(people):
        people.pop(index - 1)
        return jsonify(message="Deleted person")
    return jsonify(message="Not Found", status=404), 404