



from pymongo import Connection
connection = Connection('dbh36.mongolab.com',27367)
db = connection.soil_test
db.authenticate('soil','nextatmosphere')
collection = db.first_collection


import datetime
post = {"author":"mike","text":"asdasd","date":datetime.datetime.utcnow()}

posts = db.first_collection
posts.insert(post)



new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
                        "title": "MongoDB is fun",
                        "text": "and pretty easy too!",
                                "date": datetime.datetime(2009, 11, 10, 10, 45)}]

import uuid
while 2 > 1:
  post = {"uuid": uuid.uuid4(), "author":"mike","text":"asdasd","date":datetime.datetime.utcnow()}
  posts.insert(post)
