"""Python Hello World for MongoDB."""

import pymongo

# connect to database
connection = pymongo.MongoClient('127.0.0.1', 27017)

db = connection.test

# handle to names collection
names = db.names

item = names.find_one()

print item['name']
