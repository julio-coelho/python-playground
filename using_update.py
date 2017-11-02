
import sys
import datetime
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)


def add_review_date_using_update_one(student_id):

    print "update one, reporting for duty"

    db = connection.students
    grades = db.grades

    try:

        filter = {'student_id': student_id, 'type': 'homework'}

        score = grades.find_one(filter)
        print "before:", score

        recoded_id = score['_id']
        result = grades.update_one({'_id': recoded_id}, {
                                   '$set': {'review_date': datetime.datetime.utcnow()}})
        print "num_matched:", result.matched_count

        score = grades.find_one(filter)
        print "after:", score

    except Exception as e:
        print "Unexpected error:", type(e), e


def add_review_date_using_update_many():

    print "update many, reporting for duty"

    db = connection.students
    grades = db.grades

    try:
        result = grades.update_many({}, {
            '$set': {'review_date': datetime.datetime.utcnow()}})
        print "num_matched:", result.matched_count
    except Exception as e:
        print "Unexpected error:", type(e), e


# add_review_date_using_update_one(1)
add_review_date_using_update_many()
