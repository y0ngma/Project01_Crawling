from selenium import webdriver
import time
import pymongo
import cx_Oracle as oci
import requests
import json
import pymongo

conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database('CS_YH_team') 
options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 
driver=webdriver.Chrome('./chromedriver.exe', chrome_options=options)
<<<<<<< HEAD
url="https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-12-01T00%3A00%3A00"
driver.get(url)

# 2018-12-01 ~ 2019-11-28
# 매시간 00, 01, ... -> 23
# 23시일때 크롤링 
# 시간정보 00시로 초기화    
# 다음날 클릭

day=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/a[3]/span[1]')
    # 날짜정보xxxx-xx-xx로 만들기
tmp1 = day.text[:-5]
tmp2 = tmp1.split('.')
dbtitle = '-'.join(tmp2)
print(dbtitle)
coll=db.get_collection(dbtitle)

time.sleep(1) 
    # 화면바뀔때마다 클릭 전 시간주기
tag=driver.find_elements_by_class_name('rank_inner')
    # rank_inner 이름의 요소들 모두 담아

for i in tag:
    li=i.text.split('\n')
    # print(li)
    # print(len(li))
    # print('=========')
    
    for tmp in range(1, len(li),1):
        dic=dict()
        wordtmp =list()
        wordvalue = str()

        dic['age']=li[0]
        dic['rank']=tmp

        wordtmp = li[tmp].split(' ') #list
        wordvalue =' '.join(wordtmp[1:])
        dic['word']=wordvalue
        print(dic['word'])
        # print(dic)
        coll.insert_one(dic)
conn.close()

# 조장 지시 사항
# 테이블명 날짜로 xxxx-xx-xx
# 검색어 컬럼에 순위빼서 넣기
# 전체순위 빼고 50대 까지
# 다음날 순위 
# 다음 날짜 클릭
driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/a[2]').click()
