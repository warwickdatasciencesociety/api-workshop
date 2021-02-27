# import libraries necessary for the app to work
from flask import Flask, request, jsonify, render_template
import json

with open('grades.json') as file:
    data = json.load(file)

# configure flask
app = Flask(__name__)

# the root page, which returns JSONified hello world message
@app.route('/')
def index():
    return jsonify(success=True, message="Hello, World!")

# a useful function for getting the next id in a table - we will see that SQL
# can do this for us
def get_next_id(json):
    current_highest = max([x['id'] for x in json])
    return current_highest + 1

# your whole-data endpoints - GET will get all the data in the given JSON object, and
# POST will add to the specified JSON object
@app.route('/api/<obj>', methods=['GET', 'POST'])
def table_crud(obj):
    if request.method == 'POST':
        pass # TODO collect fields from POST request, add data to JSON object

    # else, it is a get request
    pass # TODO get all data from the given JSON object and return them

# your data-specific endpoints - GET will get the data from JSON object with given id, PUT will change
# whatever values are passed, DELETE will delete the data with id iden
@app.route('/api/<obj>/<iden>', methods=['GET', 'PUT', 'DELETE'])
def record_crud(obj, iden):
    if request.method == 'PUT':
        pass # TODO retrieve the selected data, update any fields specified

    if request.method == 'DELETE':
        pass # TODO delete the selected data

    # else, it is a GET request
    pass # TODO get data with specified id and return

# only run the app if it is being called directly
# this prevents it running e.g. if being erroneously imported
if __name__ == "__main__":
    app.run(debug=True)
