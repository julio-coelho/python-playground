
import sys
import datetime
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)


def remove_all_review_dates():

    print "update many, reporting for duty"

    db = connection.students
    grades = db.grades

    try:
        result = grades.update_many({'review_date': {'$exists': True}}, {
                                    '$unset': {'review_date': 1}})
        print "docs affected:", result.matched_count
    except Exception as e:
        print "Unexpected error:", type(e), e


def add_review_date_using_replace_one(student_id):

    print "replace one, reporting for duty"

    db = connection.students
    grades = db.grades

    try:

        filter = {'student_id': student_id, 'type': 'homework'}
        score = grades.find_one(filter)
        print "before:", score

        score['review_date'] = datetime.datetime.utcnow()
        grades.replace_one({'_id': score['_id']}, score)

        score = grades.find_one(filter)
        print "after:", score
    except Exception as e:
        print "Unexpected error:", type(e), e


# remove_all_review_dates()
add_review_date_using_replace_one(1)
