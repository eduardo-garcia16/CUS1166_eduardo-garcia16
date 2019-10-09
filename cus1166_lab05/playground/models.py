from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Define Course model
class Course(db.Model):
    # Map to course table
    __tablename__ = "courses"

    # Specify fields
    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

# Define RegisteredStudent model
class RegisteredStudent(db.Model):
    # Map to registeredstudents table
    __tablename__ = "registeredstudents"

    # Specify fields
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    grade = db.Column(db.Integer, nullable = False)
