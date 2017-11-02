
import pymongo
import sys

connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection.reddit
stories = db.stories


def find():

    print "find, reporting for duty"

    query = {'title': {'$regex': 'apple|google', '$options': 'i'}}
    projection = {'title': 1, '_id': 0}

    try:
        cursor = stories.find(query, projection)
    except Exception as e:
        print "Unexpected error", type(e), e

    for doc in cursor:
        print doc


find()
