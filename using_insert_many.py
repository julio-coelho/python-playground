
import sys
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)


def insert():

    print "insert many, reporting for duty"

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

    people_to_insert = [andrew, richard]

    try:
        people.insert_many(people_to_insert)
    except Exception as e:
        print "Unexpected error:", type(e), e


def print_people():

    db = connection.school
    people = db.people

    try:
        cursor = people.find()
    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc


print "Before the insert_many, here are the people"
print_people()
insert()
print "After the insert_many, here are the people"
print_people()
