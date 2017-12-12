
import sys
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection.final7

def main():

    try:
        cursor = db.images.find()

        for doc in cursor:
            if not exists_in_album(doc['_id']):
                print "orphan photo: ", doc['_id'] 
                db.images.delete_one({'_id': doc['_id']})
    except Exception as e:
        print "Unexpected error:", type(e), e


def exists_in_album(image_id):

    try:
        filter = {'images': image_id}
        album = db.albums.find_one(filter)

        return album is not None

    except Exception as e:
        print "Unexpected error:", type(e), e

if __name__ == '__main__':
    main()
