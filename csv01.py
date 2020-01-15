import csv
import pymongo

conn = pymongo.MongoClient('192.168.99.100', 32766)
db   = conn.get_database("db1")
coll = db.get_collection("exam1")

f    = open('./resources/exam1.csv', 'r', encoding='utf-8')
rdr  = csv.reader(f)
next(rdr, None) # 컬럼 skip

for line in rdr:
    # print(type(line))
    # print(line)
    dict1          = dict()
    dict1[line[0]] = line
    print(dict1[line[0]])
    print(dict1)
    coll.insert_one(dict1)


# for line in rdr:
#     dict1 = dict()    
#     for idx, val in enumerate(line):
#         dict1[column[idx]] = val

#     coll.insert_one(dict1)
# conn.close()
