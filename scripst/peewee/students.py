#
from peewee import *

db = SqliteDatabase("students.db")


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = CharField(default=0)

    class Meta:
        database = db


students = [
    {"username": "kenneth", "points": 4888},
    {"username": "chalkers", "points": 11912},
    {"username": "dave", "points": 1223245}
]


def add_students():
    for student in students:
        try:
            Student.create(username=student["username"], points=student["points"])
        except IntegrityError:
            student_record = Student.get(username=student["username"])
            student_record.points = student["points"]
            student_record.save()


def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return Student


if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Top student is {0.username}".format(top_student()))
