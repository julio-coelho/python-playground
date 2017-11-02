"""Python find platground"""

import pymongo
import sys

# connect
CONNECTION = pymongo.MongoClient('127.0.0.1', 27017)

# db
DB = CONNECTION.students
GRADES = DB.grades


def find():

    print "find, reporting for duty"
    query = {'type': 'exam', 'score': {'$gt': 50, '$lt': 70}}
    projection = {'student_id': 1, 'score': 1, '_id': 0}

    try:
        cursor = GRADES.find(query, projection)
    except Exception as e:
        print "Unexpected error:", type(e), e

    sanity = 0
    for doc in cursor:
        print doc
        sanity += 1
        if sanity > 10:
            break


def find_one():

    print "find one, reporting for duty"
    query = {'student_id': 10}

    try:
        doc = GRADES.find_one(query)
    except Exception as e:
        print "Unexpected error: ", type(e), e

    print doc


find()
