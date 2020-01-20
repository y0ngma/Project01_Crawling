from selenium import webdriver
import time
import pymongo
import cx_Oracle as oci
import requests
import json
import pymongo
import time
from datetime import date

options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)

conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database('team') 
print('*')
coll=db.get_collection('ppp') #collection생성
print('#')
conf=db.get_collection('conf')

if not conf.find_one():
    dict1=dict()
    dict1['date']='2020.01.01'
    conf.insert_one(dict1)

date1=conf.find_one()['date']
print(date1)
year=str(date1[0:4])
mon=str(date1[5:7])
day=str(date1[8:])
"""
yesterday = date.fromtimestamp(time.time() - 60*60*24)
dty = yesterday.strftime('%Y.%m.%d')
today=date.today()
dt=today.strftime('%Y.%m.%d')
"""
while True:
    date1=conf.find_one()['date']
    print(date1)
    year=str(date1[0:4])
    mon=str(date1[5:7])
    day=str(date1[8:10])
    for h in range(0,24,1):
        for age in ['10','20','30','40','50']:
            url='https://datalab.naver.com/keyword/realtimeList.naver?age={:s}s&datetime={:4s}-{:2s}-{:2s}T{:0>2d}%3A00%3A00'.format(age,year,mon,day,h)
            driver.get(url)
            time.sleep(2)
            tag=driver.find_elements_by_class_name('item_box')
            
            for j in tag:
                li=j.text.split('\n')
                #print(li)
                dic=dict()
                dic['age']=age
                dic['rank']=li[0]
                dic['word']=li[1]
                dt=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a[3]/span[1]').text
                year=dt[0:4]
                month=dt[5:7]
                day=dt[8:10]
                dic['year']=year
                dic['month']=month
                dic['day']=day
                dic['hour']=h
                coll.insert_one(dic)
            print(age)           
        print('한살더')        
    print('한시간더')
        
    driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a[2]').click()

    date1=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a[3]/span[1]')
    date1=date1.text[0:10]
    print(date1)
    dd=conf.find_one()['date']
    if date1==dd:
        break
    k=conf.find_one()['_id']
    conf.update_one({"_id":k}, {"$set":{"date":date1}})
    dd=conf.find_one()['date']
    print(dd)

conn.close()

from selenium import webdriver
import time
import pymongo
import requests
import json
import cx_Oracle as oci
###########오라클 연결##############
conn_o = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')
cursor = conn_o.cursor()
############몽고 연결###############
conn_m=pymongo.MongoClient('192.168.99.100',32766)#몽고 연결
db=conn_m.get_database('team') 
coll=db.get_collection('all')
conf=db.get_collection('conf')

if not conf.find_one():
    dict1=dict()
    dict1['date']='2019.01.01'
    conf.insert_one(dict1)


######웹을 불러서 값얻어내기#######################

options=webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 
driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)
# 1,시작 11월30일 00시

# d 1w


# 시작 [1일 증가,[ 옆으로 한칸, 저장, 1시간증가, 옆으로 한칸 저장]]
for m in range(1,7,1):
    for d in range (1,32,1):
        for h in range(0,24,1):
            url="https://datalab.naver.com/keyword/realtimeList.naver?datetime=2019-{:0>2d}-{:0>2d}T{:0>2d}%3A00%3A00".format(m,d,h)


            ###########################################################################################################################
            driver.get(url)
            time.sleep(1)
            # 2, 1일 증가
            try:
                driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/a[2]/span').click()#옆으로 한칸 클릭(50대이상 보이게)
                day=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/a[3]/span[1]')#날짜 변수
                time1=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/a[3]/span[1]')
                yyyy=day.text[0:4]
                mm=day.text[5:7]
                dd=day.text[8:10]
                time2=time1.text[0:2]
                dbname=yyyy+'-'+mm+'-'+dd
                

                # coll=db.get_collection(dbname)#db이름 설정

                tag=driver.find_elements_by_class_name('rank_inner')
                
                list_all=list()
                for i in tag:
                    li = i.text.split('\n')
                    list_all.append(li)
                list_start10=list_all[1:6]

                # print(list_start10)
                for tmp in range(0,5,1):
                    a=list_start10[tmp]
                    for tmp1 in range(1,len(a),1):
                        dict1=dict()
                        dict1["age"]=a[0]
                        b=a[tmp1].split()
                        dict1["rank"]=b[0]
                        dict1["word"]="".join(b[1:])
                        dict1['year']=yyyy
                        dict1['month']=mm
                        dict1['day']=dd
                        dict1['time']=time2
                        coll.insert_one(dict1)

                
                print(dbname,time2,'완료')
                # data1 = coll.find({}, {'_id':False})

                # for tmp in data1:
                #     # print(tmp)
                #     sql='''
                #     INSERT INTO TEAM(NO, AGE, RANK, WORD, YEAR, MONTH, DAY, TIME)
                #     VALUES(SEQ_TEAM_NO.nextval, :age, :rank, :word, :year, :month, :day, :time)
                #     '''


                    # cursor.execute(sql, tmp)
                    # conn_o.commit()
                # print('oracle db 추가 완료')


            except:
                pass           
        date1=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/a[3]/span[1]')
        date1=date1.text[0:10]
        dd=conf.find_one()['date']
        k=conf.find_one()['_id']
        conf.update_one({"_id":k}, {"$set":{"date":date1}})
        dd=conf.find_one()['date']
        

conn_m.close()       
conn_o.close() # 오라클 연결 끊기
