# import libraries necessary for the app to work
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from werkzeug.security import safe_str_cmp

# configure flask so that it will connect to the database, and can be hosted
# locally
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grades.db'
app.config['SERCET_KEY'] = 'super-secret'
app.config['JWT_SECRET_KEY'] = 'also-secret'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_REFRESH_COOKIE_PATH'] = '/token/refresh'
# do not set this config variable in a production environment!
app.config['JWT_COOKIE_CSRF_PROTECT'] = False

# configure the database and authentication managers
db = SQLAlchemy(app)
jwt = JWTManager(app)

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
@jwt_required()
def basic_crud(table):
    if request.method == 'POST':
        if table == 'student':
            entry = Student(
                f_name=request.form['f_name'],
                l_name=request.form['l_name']
            )
        elif table == 'course':
            entry = Course(
                c_name=request.form['c_name']
            )
        elif table == 'grade':
            entry = Grade(
                s_id=request.form['s_id'],
                c_id=request.form['c_id'],
                grade=request.form['grade']
            )
        else:
            return f'Table {table} does not exist'

        try:
            db.session.add(entry)
            db.session.commit()
            return jsonify(success=True)
        except Exception as e:
            return jsonify(success=False, message=str(e))
    if table == 'student':
        returnVal = Student.query.all()
    elif table == 'course':
        returnVal = Course.query.all()
    elif table == 'grade':
        returnVal = Grade.query.all()
    else:
        return f'Table {table} does not exist'

    # else (not required due to complete returns above)
    return jsonify(success=True, message=str([x.__dict__  for x in returnVal]))

# your record-specific endpoints - GET will get the record, PUT will change
# whatever values are passed, DELETE will delete the record
@app.route('/api/<table>/<iden>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def basic_crud_id(table, iden):
    if table == 'student':
        record = Student.query.get_or_404(iden)
    elif table == 'course':
        record = Course.query.get_or_404(iden)
    elif table == 'grade':
        record = Grade.query.get_or_404(iden)
    else:
        return f'Table {table} does not exist'

    if request.method == 'PUT':
        if table == 'student':
            if 'f_name' in request.form:
                record.f_name = request.form['f_name']
            if 'l_name' in request.form:
                record.l_name = request.form['l_name']

        elif table == 'course':
            if 'c_name' in request.form:
                record.c_name = request.form['c_name']

        elif table == 'grade':
            if 's_id' in request.form:
                record.s_id = request.form['s_id']
            if 'c_id' in request.form:
                record.c_id = request.form['c_id']
            if 'grade' in request.form:
                record.grade = request.form['grade']

        else:
            return f'Table {table} does not exist'

        try:
            db.session.commit()
            return jsonify(success=True)
        except Exception as e:
            return jsonify(success=False, message=str(e))

    if request.method == 'DELETE':
        try:
            db.session.delete(record)
            db.session.commit()
            return jsonify(success=True)
        except Exception as e:
            return jsonify(success=False, message=str(e))

    return jsonify(success=True, message=str(record.__dict__))

# provide an interface to enter a new grade - this should link with an API
# call above
@app.route('/newgrades')
@jwt_required()
def new_grade():
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('new.html', students=students, courses=courses)

# the default mechanism for getting authentication to access the API
@app.route('/token/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        entered_uname = request.form['u_name']
        entered_upass = request.form['u_pass']
        user = User.query.filter_by(u_name=entered_uname).first()
        if user and safe_str_cmp(user.u_pass.encode('utf-8'), entered_upass.encode('utf-8')):
                access_token = create_access_token(identity=entered_uname)
                refresh_token = create_refresh_token(identity=entered_uname)
                response = jsonify(login=True, success=True, access_token=access_token, refresh_token=refresh_token)
                set_access_cookies(response, access_token)
                set_refresh_cookies(response, access_token)
                return response, 200
        else:
            error = "Invalid Credentials. Please try again."
            return jsonify(success=False, message=str(error))
    return render_template('login.html')

# only run the app if it is being called directly
# this prevents it running e.g. if being erroneously imported
if __name__ == "__main__":
    app.run(debug=True)
