# 파일명 : json01.py
import requests
import json
import cx_Oracle as oci

conn = oci.connect('user7/1234@1.234.5.158:32764/xe', encoding='utf-8')
cursor = conn.cursor()

url     = "http://ihongss.com/json/exam2.json"
str1    = requests.get(url).text # 0101.. 문자열로 오므로 json타입이 아니다. 변환 필요.
data1   = json.loads(str1) # (file에서 읽을때는 load) str->dict은 loads

# sql = '''
#     INSERT INTO MEMBER(ID, PW, NAME, AGE, JOINDATE)
#     VALUES(:id, '1', :name, :age, SYSDATE)
# '''

print(data1)
for i in data1: # ret, ret1
    for tmp in data1[i]: # ret[0]..ret[len(i)]
        print(tmp)


# cursor.execute(sql, )
# cursor.commit()
