import sqlite3, random

# run this if your db gets corrupted!
db = sqlite3.connect('../grades.db')

cursor = db.cursor()

setup_commands = ["DROP TABLE IF EXISTS student",
        "DROP TABLE IF EXISTS course",
        "DROP TABLE IF EXISTS grade",
        "DROP TABLE IF EXISTS user",
        "CREATE TABLE student(id INTEGER PRIMARY KEY, f_name TEXT, l_name TEXT)",
        "CREATE TABLE course(id INTEGER PRIMARY KEY, c_name TEXT)",
        "CREATE TABLE grade(id INTEGER PRIMARY KEY, s_id INTEGER, c_id INTEGER, grade INTEGER, FOREIGN KEY(s_id) REFERENCES student(id), FOREIGN KEY(c_id) REFERENCES course(id))",
        "CREATE TABLE user(id INTEGER PRIMARY KEY, u_name TEXT, u_pass TEXT)"]

students = [("Adela", "Rucks"),
            ("Shawna", "Kellough"),
            ("Anissa", "Mcneilly"),
            ("Kandi", "Fu"),
            ("Amado", "Beebe"),
            ("Paulina", "Schroyer"),
            ("Bobette", "Whited"),
            ("Ethyl", "Padro"),
            ("Alana", "Billy"),
            ("Vivan", "Candler")]

courses = [("Maths",), ("Computer Science",), ("Music",)]

grades = [(random.randint(1, len(students)), random.randint(1, len(courses)), random.randint(0, 100)) for i in range(20)]

for command in setup_commands:
    cursor.execute(command)

for student in students:
    statement = "INSERT INTO student(f_name, l_name) VALUES(?, ?)"
    cursor.execute(statement, student)

for course in courses:
    statement = "INSERT INTO course(c_name) VALUES(?)"
    cursor.execute(statement, course)

for grade in grades:
    statement = "INSERT INTO grade(s_id, c_id, grade) VALUES(?, ?, ?)"
    cursor.execute(statement, grade)

cursor.execute("INSERT INTO user(u_name, u_pass) VALUES(?, ?)", ("admin", "password"))

db.commit()
