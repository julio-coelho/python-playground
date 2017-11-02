
import sys
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)


def insert():

    print "insert one, reporting for duty"

    db = connection.school
    people = db.people

    richard = {
        'name': 'Richard Kreuter',
        'company': '10gen',
        'interest': [
            'horsing',
            'skydiving',
            'fencing'
        ]
    }

    andrew = {
        '_id': 'erlichson',
        'name': 'Andrew Erlichson',
        'company': '10gen',
        'interest': [
            'runnig',
            'cycling',
            'photography'
        ]
    }

    try:
        people.insert_one(richard)
        people.insert_one(andrew)
    except Exception as e:
        print "Unexpected error:", type(e), e

    print richard
    print andrew


insert()
