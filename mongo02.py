
import pymongo
import cx_Oracle as oci

conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor = conn_o.cursor()

conn_m = pymongo.MongoClient('192.168.99.100', 32766)
db = conn_m.get_database('db1')
coll   = db.get_collection('p20200115')
    # dict1   = {"id":"a", "name":"Abc", "age":31}
    # coll.insert_one(dict1)
    # dict2   = {"id":"b", "name":"aBc", "age":32}
    # coll.insert_one(dict2)
    # dict3   = {"id":"c", "name":"abC", "age":33}
    # coll.insert_one(dict3)

# SELECT*FROM p20200115 WHERE ID="a"
data1   = coll.find({}, {'_id':False})
for tmp in data1:
    print(tmp)
    sql='''
    INSERT INTO TABLE1(NO, ID, NAME, AGE)
    VALUES(SEQ_TABLE1_NO.nextval, :id, :name, :age)
    '''
    cursor.execute(sql, tmp)
    conn_o.commit()

conn_o.close() # 오라클 연결 끊기
conn_m.close() # 몽고 연결끊기

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

# SELECT * FROM TABLE WHERE ID='a' OR NAME='b'
data8  = coll.find({'$or':[{"id":'a'},{"name":'b'}]})

#SELECT * FROM p202001015 id=a or name in (b)
data9 = coll.find({'$or':[{"id":'a'},{'name':{'$in':['b']}} ] }) 
for tmp in data9:
    print(tmp)