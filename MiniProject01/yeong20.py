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
