from flask import Flask, request
from src.flaskapi.data_manager import DataManager
import json
import hashlib

hash = hashlib.md5("random".encode('utf-8')).hexdigest()
print(hash)
dm = DataManager()

app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome Touseef"


@app.route('/get20/<column_name>')
def get_first_20_rows(column_name):
    return dm.get_first_20_rows(column_name)


@app.route('/data-airlines/<name>')
def get_airline_data(name):
    return dm.get_airline_data_by_name(name)


@app.route('/update-code/<apikey>', methods=['PUT'])
def update_airline_code(apikey):
    if apikey != hash:
        return "Invalid API key", 400
    str_data = request.data.decode('utf-8')
    print("str_data = " + str_data)
    print(type(str_data))
    json_data = json.loads(str_data)

    if len(json_data['old_code']) != 2 or len(json_data['new_code']) != 2:
        return "The airline code should exactly be 2 letters code", 400
    return dm.update_airline_code(json_data['old_code'], json_data['new_code'])


if __name__ == "__main__":
    app.run(debug=False)
