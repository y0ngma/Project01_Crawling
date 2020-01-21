from django.db import connection
import pymongo
import cx_Oracle as oci

###########오라클 연결##############
conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor = conn_o.cursor()
############몽고 연결###############
conn_m=pymongo.MongoClient('192.168.99.100',32766)#몽고 연결
db=conn_m.get_database('team') 
coll=db.get_collection('ppp')

data1 = coll.find({}, {'_id':False}) # 빼고자 하는 컬럼'_id' 

for tmp in data1:
    print(type(tmp), tmp)

    sql='''
        INSERT INTO BOARD_BOARD1(GENE, RANK, WORD, YEAR, MONTH, DAY, TIME)
        VALUES(:age, :rank, :word, :year, :month, :day, :time)
    '''
    cursor.execute(sql, tmp)
    conn_o.commit()
print('oracle db 추가 완료')


conn_m.close()       
conn_o.close() # 오라