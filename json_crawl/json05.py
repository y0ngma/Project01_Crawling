import requests
import json
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database('db1') 
table   = db.get_collection('exam10') 

url     = "http://ihongss.com/json/exam10.json"
str1    = requests.get(url).text 
data1   = json.loads(str1)
'''
{
    'ret' : 'y', 
    'data':
        [
            {'id': 'id1', 'name': '가나다1', 'age': 31, 'score': 
                {
                'math': 50, 'eng': 90, 'kor': 69
                }
            }, 
            {'id': 'id2', 'name': '가나다2', 'age': 32, 'score': 
            {'math': 90, 'eng': 68, 'kor': 80}}, {'id': 'id3', 'name': '가나다3', 'age': 33, 'score': 
            {'math': 70, 'eng': 76, 'kor': 60}}, {'id': 'id4', 'name': '가나다4', 'age': 34, 'score': {'math': 80, 'eng': 79, 'kor': 50}}, {'id': 'id5', 'name': '가나다5', 'age': 35, 'score':
            {'math': 80, 'eng':78, 'kor': 90}}
        ]
}
'''
'''
{
    ret: "y",
    data: [
            {},
            {},
            {},
            {},
            {}
        ]
}
'''
# ret = "y"

# if data1["ret"] =="y":
print(data1)
print("="*50)
print(data1["data"])
for one in data1["data"]: # {'id': 'id1', 'name': '가나다1', 'age': 31, 'score': {'math': 50, 'eng': 90, 'kor': 69}}
    dict1 = dict()

    dict1["id"] = one["id"]
    dict1["name"] = one["name"]
    dict1["age"] = one["age"]
    dict1["math"] = one["score"]["math"]
    dict1["kor"] = one["score"]["kor"]
    table.insert_one(dict1)
# else:
#     print("wrong ret")