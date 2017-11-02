
import pymongo


def get_next_sequence_number(name):

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    db = connection.test
    counters = db.counters

    try:
        counter = counters.find_one_and_update(filter={'type': name},
                                               update={'$inc': {'value': 1}},
                                               upsert=True,
                                               return_document=pymongo.ReturnDocument.AFTER)
    except Exception as e:
        print "Unexpected error:", type(e), e

    return counter['value']


print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
print get_next_sequence_number('uid')
