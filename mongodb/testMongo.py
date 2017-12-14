#! python 3
## test python to link the mongo db

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.test

collection = db.long
'''
findone = collection.find_one()
print(findone)

count = collection.count()
print(count)


cur = collection.find()
for doc in cur:
    print(doc)

print(collection.count())
collection.insert({'a':1})
print(collection.count())


flagrow = coll.find_one({'flag':'mssqlstartid'})

startId = int(flagrow['value'])

print(startId)
'''

te = db.long.find_one({'yxq':1})

if(not te):
    print('y')

print(te)