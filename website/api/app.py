from flask import Flask, jsonify, request
from json import load, dump
from os import getcwd

app = Flask(__name__)
path = getcwd()

def database_read():
    with open(path + '/database.json') as database_file:
        data = load(database_file)["todo"]
    return data

def database_write(data):
    with open(path + '/database.json', 'w') as database_file:
        dump(data, database_file, indent=4)
    return 'successful data!'

@app.route('/', methods=['GET'])
def index_connection():
    return jsonify({'status': '200', 'message': 'Nice, API is Online!'})

@app.route('/getall', methods=['GET'])
def get_all_todo():
    return jsonify([i for i in database_read().keys()])

@app.route('/newtodo', methods=['POST'])
def set_new_todo():
    # logic to add a new todo to database
    title, description, autor = (request.json["title"], request.json["description"], request.json["autor"])
    data = database_read()
    todo_data = {
        "id": data["last_id"] + 1,
        "title": title,
        "description": description,
        "autor": autor
    }
    data["last_id"] += 1
    data[todo_data['id']+1] = todo_data
    return jsonify({"message": f"{str(title)} added successfully!", "data": todo_data})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
