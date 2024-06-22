from flask import Flask
from flask import jsonify
from json import load, dump
from os import getcwd

app = Flask(__name__)
path = getcwd()

@app.route('/')
def index_connection():
    return jsonify({'status': '200', 'message': 'Nice, API is Online!'})

@app.route('/getall')
def get_all_todo():
    with open(path + '/database.json') as database_file:
        content = load(database_file)
    return jsonify(database_file.keys())

if __name__ == '__main__': app.run(debug=True, port=8080)
