"""Python find platground"""

import pymongo
import sys

# connect
CONNECTION = pymongo.MongoClient('127.0.0.1', 27017)

# db
DB = CONNECTION.agg
ZIPS = DB.zips


def main():

    print "aggregate, reporting for duty"
    aggregate = []
    aggregate.insert(0, {
        '$group': {
            '_id': {'state': '$state', 'city': '$city'},
            'population': {'$sum': '$pop'}
        }
    })
    aggregate.insert(1, {
        '$sort': {
            '_id.state': 1,
            'population': -1
        }
    })
    aggregate.insert(2, {
        '$group': {
            '_id': '$_id.state',
            'city': {'$first': '$_id.city'},
            'population': {'$first': '$population'}
        }
    })

    try:
        cursor = ZIPS.aggregate(aggregate)
    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        print doc


if __name__ == '__main__':
    main()
