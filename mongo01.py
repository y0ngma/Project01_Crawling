# pip install pymongo
import requests
import json
import pymongo

# 1. 접속
conn = pymongo.MongoClient('192.168.99.100', 32766)
# 2. db 연결
db = conn.get_database('db1') # database 있으면 가져오고, 없으면 만들고
# 3. 테이블 연결
table   = db.get_collection('exam4') #Collection 있으면 가져오고, 없으면 만들고

# 4. 테이블에 데이터 삽입
dict1 = {"id": "a", "age": 23}
table.insert_one(dict1) 
    # 데이터가 먼저 있어야 db가 만들어짐
    # 추가부분 주석처리

data1 = table.find()
for tmp in data1:
    print(tmp)
    print(type(tmp))
conn.close()
print(conn)
# 수행할때마다 테이블이 생성되는 이유는 몽고디비에서 자동으로 기본키를 생성.