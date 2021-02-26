# import libraries necessary for the app to work
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

# configure flask so that it will connect to the database, and can be hosted
# locally
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grades.db'

# configure the database and authentication managers
db = SQLAlchemy(app)

# here we have formalised the database fields and views into Python objects
# this will make it easier to deal with database-related operations in Flask
class Student(db.Model):
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(20), nullable=False)
    l_name = db.Column(db.String(20), nullable=False)

class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(20), nullable=False)

class Grade(db.Model):
    __tablename__ = "grade"
    id = db.Column(db.Integer, primary_key=True)
    s_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    c_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    grade = db.Column(db.Integer, nullable=False)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    u_name = db.Column(db.String(20), nullable=False)
    u_pass = db.Column(db.String(20), nullable=False)

# the root page, which returns JSONified hello world message
@app.route('/')
def index():
    return jsonify(success=True, message="Hello, World!")

# if you're experiencing issues with connecting to the database, go to this
# route to check whether or not it works
@app.route('/dbtest')
def dbtest():
    try:
        db.session.query("1").from_statement(text("SELECT 1")).all()
        return jsonify(success=True, message="It works")
    except Exception as e:
        return jsonify(success=False, message=str(e))

# your whole-table endpoints - GET will get all fields in the given table, and
# POST will add a new record
@app.route('/api/<table>', methods=['GET', 'POST'])
def basic_crud(table):
    if request.method == 'POST':
        pass # TODO collect fields from POST request, add record to database

    # else, it is a get request
    pass # TODO get all record from the given table and return them

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
