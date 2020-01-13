# 파일명 : json01.py
import json
import cx_Oracle as oci

conn = oci.connect('user7/1234@1.234.5.158:32764/xe', encoding='utf-8')
cursor = conn.cursor()

file1   = open('./resources/exam02.json', encoding='utf-8')
data1   = json.load(file1) # {"ID", "aaa", "PW":"34"}
print(type(data1))

sql = '''
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:ID, :PW, :NAME, :AGE, SYSDATE)
    '''
cursor.execute(sql, data1)
conn.commit()

print(data1)
print(data1["ID"])
print(type(data1))