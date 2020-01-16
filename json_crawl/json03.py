import requests
import json
import cx_Oracle as oci

conn = oci.connect('user7/1234@1.234.5.158:32764/xe', encoding='utf-8')
cursor = conn.cursor()

url     = "http://ihongss.com/json/exam3.json"
str1    = requests.get(url).text 
data1   = json.loads(str1)
# data1 -> {ret:[{}, {}, {}, {}], ret1:[{}, {}, {}, {}]}
ret = data1['ret'] # [{}, {}, {}, {}]

for tmp in ret: # 4번 수행
    print(tmp) # {'id': 'a2001', 'name': '123', 'age': 34}
    sql = '''
    INSERT INTO MEMBER(ID, PW, NAME, AGE, JOINDATE)
    VALUES(:id, 'itsPW', :name, :age, SYSDATE)
'''
    cursor.execute(sql, tmp)
conn.commit()
