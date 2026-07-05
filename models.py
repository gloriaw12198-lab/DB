from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship("Student", backref="course", lazy=True)

    def __repr__(self):
        return f"{self.name}"


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"))

    def __repr__(self):
        return f"{self.name}"
