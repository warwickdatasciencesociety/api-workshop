from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grades.db'
db = SQLAlchemy(app)

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

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/dbtest')
def dbtest():
    try:
        db.session.query("1").from_statement(text("SELECT 1")).all()
        return jsonify(success=True, message="It works")
    except Exception as e:
        return jsonify(success=False, message=str(e))

@app.route('/api/<table>', methods=['GET', 'POST'])
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

    return jsonify(success=True, message=str([x.__dict__  for x in returnVal]))

@app.route('/api/<table>/<iden>', methods=['GET', 'PUT', 'DELETE'])
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

@app.route('/newgrades')
def new_grade():
    students = Student.query.all()
    courses = Course.query.all()
    return render_template('new.html', students=students, courses=courses)

if __name__ == "__main__":
    app.run(debug=True)
