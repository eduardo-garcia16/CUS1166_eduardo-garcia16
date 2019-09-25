from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name = student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    class_roster = [("John Green", "A+", "Sophomore"), ("Samantha Blue", "A", "Junior"), ("Kevin Red", "A", "Freshman"), ("Lulu Yellow", "B", "Senior"), ("Chris Black", "C", "Junior"), ("Tom White", "D-", "Sophomore"), ("Joe Moe", "A", "Freshman")]
    return render_template("roster.html", grade_view = grade_view, class_roster = class_roster)
