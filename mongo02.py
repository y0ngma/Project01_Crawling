import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database('db1')
coll   = db.get_collection('p20200115')

# dict1   = {"id":"a", "name":"abc", "age":31}
# coll.insert_one(dict1)

# SELECT*FROM p20200115 WHERE ID="a"
data1   = coll.find()

# SELECT*FROM p20200115 WHERE ID="a"
data2   = coll.find({'id':'a'})

# SELECT ID, NAME FROM p20200115 WHERE ID='a'
data3   = coll.find({'id':'a'}, {'id':1, 'name':1})

# SELECT*FROM TABLE WHERE age>10
data4   = coll.find({'age':{"$gt":10}})

# SELECT*FROM TABLE ORDER BY name ASC('', 1)/DESC('',-1)
data5   = coll.find().sort('name', 1)
for tmp in data5:
    print(tmp)

# SELECT*FROM TABLE WHERE age>10 AND age<=30
data6   = coll.find({"age":{"$gt":10, "$lte":30}})

# SELECT COUNT(*) FROM TABLE
data7   = coll.find().count()
print(data7) # 반복문 x, 딕셔너리 아님

# SELECT*FROM TABLE WHERE ID='a' OR NAME='b'
data6   = coll.find({"$or":[{"id":'a', "name":'b'}]})


