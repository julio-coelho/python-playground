
import sys
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection.school
students = db.students


def main():

    filter = {'scores.type': 'homework'}

    try:
        cursor = students.find(filter)

        for doc in cursor:
            unset_bottom_homework_score(doc)

    except Exception as e:
        print "Unexpected error:", type(e), e


def unset_bottom_homework_score(doc):

    homework_score = 100.0
    for score in doc['scores']:
        if score['type'] == 'homework':
            if score['score'] < homework_score:
                homework_score = score['score']

    filter = {'_id': doc['_id']}
    pull = {'$pull': {'scores': {'type': 'homework', 'score': homework_score}}}

    students.update_one(filter, pull)


if __name__ == '__main__':
    main()
