
import pymongo
import gridfs
import sys

connection = pymongo.MongoClient('127.0.0.1', 27017)
db = connection.test
videos_meta = db.videos_meta


def main():

    grid = gridfs.GridFS(db, 'videos')
    fin = open('/Users/juliocoelho/Temp/IMG_1357.MOV', 'r')

    _id = grid.put(fin)
    fin.close()
    print "id of file is :", _id

    videos_meta.insert_one({'grid_id': _id, "filename": 'IMG_1357.MOV'})


if __name__ == '__main__':
    main()
