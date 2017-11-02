
import sys
import datetime
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)


def using_upsert():

    print "upsert, reporting for duty"

    db = connection.test
    things = db.things

    try:
        things.drop()

        things.update_one({'thing': 'apple'}, {
                          '$set': {'color': 'red'}}, upsert=True)
        things.update_many({'thing': 'banana'}, {
                           '$set': {'color': 'yellow'}}, upsert=True)
        things.replace_one({'thing': 'pear'}, {
                           'color': 'green'}, upsert=True)

        apple = things.find_one({'thing': 'apple'})
        print "apple:", apple
        banana = things.find_one({'thing': 'banana'})
        print "banana:", banana
        pear = things.find_one({'thing': 'pear'})
        print "pear:", pear

    except Exception as e:
        print "Unexpected error:", type(e), e


using_upsert()
