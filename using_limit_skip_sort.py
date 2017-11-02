
import sys
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection.students
grades = db.grades


def find():

    print 'find, reporting for duty'

    query = {}

    try:
        cursor = grades.find(query)
        cursor = cursor.limit(10)
        cursor.sort([('score', pymongo.DESCENDING),
                     ('student_id', pymongo.ASCENDING)])
    except Exception as e:
        print "Unexpected error", sys.exc_info()[0]

    for doc in cursor:
        print doc


find()
