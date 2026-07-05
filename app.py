from flask import Flask, render_template
from flask_migrate import Migrate

from models import Student, Course, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/students")
def students():
    students = Student.query.all()
    return render_template("students.html", students=students)


@app.route("/courses")
def courses():
    courses = Course.query.all()
    return render_template("courses.html", courses=courses)


@app.route("/")
def index():
    return "Flask app is running"


def seed_data():
    if Course.query.count() == 0:
        web = Course(name="Web Development")
        python = Course(name="Python")
        db.session.add_all([web, python])
        db.session.commit()

    if Student.query.count() == 0:
        web = Course.query.filter_by(name="Web Development").first()
        python = Course.query.filter_by(name="Python").first()
        students = [
            Student(name="Gloria", age=22, email="gloria@example.com", course=web),
            Student(name="Brian", age=24, email="brian@example.com", course=python),
            Student(name="Faith", age=20, email="faith@example.com", course=web),
        ]
        db.session.add_all(students)
        db.session.commit()


@app.cli.command("seed")
def seed_command():
    with app.app_context():
        seed_data()
        print("Seeded sample students and courses")


if __name__ == "__main__":
    with app.app_context():
        seed_data()
    app.run(debug=True)
