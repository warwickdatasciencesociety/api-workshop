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

# your whole-table endpoints - GET will get all fields in the given table, and
# POST will add a new record
@app.route('/api/<table>', methods=['GET', 'POST'])
def basic_crud(table):
    if request.method == 'POST':
        pass # TODO collect fields from POST request, add record to database

    # else, it is a get request
    return jsonify(success=True, message=data[table]) # TODO get all record from the given table and return them

# your record-specific endpoints - GET will get the record, PUT will change
# whatever values are passed, DELETE will delete the record with id iden
@app.route('/api/<table>/<iden>', methods=['GET', 'PUT', 'DELETE'])
def basic_crud_id(table, iden):
    if request.method == 'PUT':
        pass # TODO retrieve the selected record, update any fields specified

    if request.method == 'DELETE':
        pass # TODO delete the selected record

    # else, it is a GET request
    pass # TODO get record with specified id and return

# provide an interface to enter a new grade - this should link with an API
# call above
@app.route('/newgrades')
def new_grade():
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('new.html', students=students, courses=courses)

# only run the app if it is being called directly
# this prevents it running e.g. if being erroneously imported
if __name__ == "__main__":
    app.run(debug=True)
