# 파일명 : json01.py
import json

# 파일 읽기
file1   = open('./resources/exam01.json')
# str to dict 변경
data1   = json.load(file1)

print(data1)
print(data1["ID"])
print(type(data1))