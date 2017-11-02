
import json
import urllib2
import pymongo

connection = pymongo.MongoClient('127.0.0.1', 27017)

db = connection.reddit
stories = db.stories

stories.drop()

reddit_page = urllib2.urlopen('https://www.reddit.com/r/technology/.json')

parsed = json.loads(reddit_page.read())

for item in parsed['data']['children']:
    stories.insert_one(item['data'])
