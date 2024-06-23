from flask import Flask, jsonify, request
from json import load, dump
from os import getcwd
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)
path = getcwd()

# API useful functions
def database_read():
    with open(path + '/database.json') as database_file:
        data = load(database_file)
    return data

def database_write(data):
    with open(path + '/database.json', 'w') as database_file:
        dump(data, database_file, indent=4)
    return 'successful data!'

def message(code: int = 200, message: str = "successful", custom_data: dict = {}):
    if not custom_data:
        return {'status': code, 'message': message}
    else:
        return {'status': code, 'message': message, "data": custom_data}

# API Routes
@app.route('/', methods=['GET'])
def index_connection():
    return jsonify(message(message='Nice, API is Online!'))

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
    data[data['last_id']+1] = todo_data
    data["last_id"] += 1
    database_write(data=data)
    return jsonify(message(message=f"{str(title)} added successfully!", custom_data=todo_data))

@app.route('/search/<int:id>', methods=['GET'])
def get_todo_by_id(id: int):
    try:
        todo_data = database_read()[str(id)]
        return jsonify(todo_data)
    except KeyError as error:
        print(error)
        return jsonify(message(404, "Todo not found or not exists.",))

if __name__ == '__main__':
    app.run(debug=False, port=9000)
