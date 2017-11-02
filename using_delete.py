
import sys
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)


def remove_student(student_id):

    print "delete one, reporting for duty"

    db = connection.students
    grades = db.grades

    try:

        filter = {'student_id': student_id}
        # result = grades.delete_one(filter)
        result = grades.delete_many(filter)

        print "docs affected:", result.deleted_count

    except Exception as e:
        print "Unexpected error:", type(e), e


def find_student(student_id):

    print "find one, reporting for duty"

    db = connection.students
    grades = db.grades

    try:
        filter = {'student_id': student_id}
        cursor = grades.find(filter)

        for doc in cursor:
            print doc

    except Exception as e:
        print "Unexpected error:", type(e), e


remove_student(3)
find_student(3)
