from selenium import webdriver
import time


import pymongo
import cx_Oracle as oci

import requests
import json
import pymongo


options=webdriver.ChromeOptions()
options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)

conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database('team') 
coll=db.get_collection('p20200117') #collection생성


for d in range (28,31,1):
    for h in range(0,24,1):
        for age in ['10','20','30','40','50']:
            url='https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime=2019-11-{:0>2d}T{:0>2d}%3A00%3A00'.format(age,d,h)
            driver.get(url)
            time.sleep(3)
            tag=driver.find_elements_by_class_name('item_box')
            #day=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a[3]/span[1]')
            for i in tag:
                li=i.text.split('\n')
                print(li) 
                ##for tmp in range(1, len(li),1):
                dic=dict()
                #dic['day']=day.text
                dic['age']=age
                dic['rank']=li[0]
                dic['word']=li[1]
                dic['year']='2019'
                dic['month']='11'
                dic['day']=d
                dic['hour']=h
                coll.insert_one(dic)
"""
for d in range (1,32,1):
    for h in range(0,24,1):
        for age in ['10','20','30','40','50']:
            url='https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime=2019-12-{:0>2d}T{:0>2d}%3A00%3A00'.format(age,d,h)
            driver.get(url)
            time.sleep(3)
            tag=driver.find_elements_by_class_name('item_box')
            day=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/div/div/div/div[1]/a[3]/span[1]')
            for i in tag:
                li=i.text.split('\n')

                for tmp in range(1, len(li),1):
                    dic=dict()
                    #dic['day']=day.text
                    dic['age']=li[0]
                    dic['rank']=tmp
                    dic['word']=li[tmp]
                    dic['year']='2019'
                    dic['month']='12'
                    dic['day']=d
                    coll.insert_one(dic)

"""
"""
list1 = ['1', '2', '3']
str1 = ''.join(list1)

UPDATE 테이블명 SET name=na변수값 WHERE id='id'
coll1.update_one({"id":id}, {"$set":{"name":na}})



"""
conn.close()