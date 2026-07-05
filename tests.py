import unittest

from app import app, db
from models import Course, Student


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_student_course_relationship(self):
        with app.app_context():
            course = Course(name='Web Development')
            student = Student(name='Gloria', age=22, course=course)
            db.session.add_all([course, student])
            db.session.commit()

            saved_student = Student.query.first()
            self.assertEqual(saved_student.course.name, 'Web Development')

    def test_students_page_renders_data(self):
        with app.app_context():
            course = Course(name='Python')
            student = Student(name='Brian', age=24, course=course)
            db.session.add_all([course, student])
            db.session.commit()

        response = self.client.get('/students')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Brian', response.data)


if __name__ == '__main__':
    unittest.main()
