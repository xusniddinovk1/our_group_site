from django.db import connection
from contextlib import closing


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_subjects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT * FROM students_subject""")
        subjects = dict_fetchall(cursor)
        return subjects


def get_teachers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT students_teacher.id, students_teacher.first_name, students_teacher.last_name, 
                        students_teacher.phone_number, students_subject.name as subject_name FROM students_teacher
                        LEFT JOIN students_subject ON students_teacher.subject_id = students_subject.id""")
        teachers = dict_fetchall(cursor)
        return teachers


def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT students_student.id, students_student.first_name, students_student.phone_number, 
                        students_student.image as image FROM students_student""")
        students = dict_fetchall(cursor)
        return students


def get_failed_credits():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT students_studentsubjectfailure.id, students_student.first_name, students_student.last_name,
                        students_subject.name, students_studentsubjectfailure.failed_credits FROM students_studentsubjectfailure LEFT JOIN 
                        students_student ON students_studentsubjectfailure.student_id = students_student.id LEFT JOIN 
                        students_subject ON students_studentsubjectfailure.subject_id = students_subject.id""")
        failed_credits = dict_fetchall(cursor)
        return failed_credits
