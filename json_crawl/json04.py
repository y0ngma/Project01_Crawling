import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database('db1') 
table   = db.get_collection('exam4') 

url     = "http://ihongss.com/json/exam4.json"
str1    = requests.get(url).text 
data1   = json.loads(str1)
print(data1)
'''
[
    {'name': 'AAA', 'species': 'cat', 
    'foods': {
        'likes': ['tuna', 'catnip'], 
        'dislikes': ['ham', 'zucchini']
        }
    },
    {'name': 'BBB', 'species': 'dog', 'foods': {'likes': ['bones', 'carrots'], 'dislikes': ['tuna']}},
    {'name': 'CCC', 'species': 'cat', 'foods': {'likes': ['mice'], 'dislikes': ['cookies']}}
]
'''
# insert_one({})
# insert_many([{},{},{}])
for tmp in data1:
    print(tmp['name'])
    print(tmp['species'])
    print(tmp['foods']['likes'][0]) #{:[], :[]}
    print(tmp['foods']['likes'][0]) #{:[], :[]}
    dict1 = dict()
    dict1['name']     =  tmp['foods']
    dict1['species']  =  tmp['foods']
    dict1['likes']    =  tmp['foods']['likes'][0]
    dict1['dislikes'] =  tmp['foods']['dislikes'][0]

    table.insert_one(dict1)

conn.close()