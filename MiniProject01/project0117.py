from selenium import webdriver
import time


import pymongo
import cx_Oracle as oci

import requests
import json
import pymongo
######웹을 불러서 값얻어내기#######################
options=webdriver.ChromeOptions()
#options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)
url="https://datalab.naver.com/keyword/realtimeList.naver?age=10s&datetime=2019-01-01T12%3A00%3A00"

driver.get(url)
time.sleep(3)
driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/a[2]/span').click()

tag=driver.find_elements_by_class_name('rank_inner')
day=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[1]/a[3]/span[1]')

print(day.text)
for i in tag:
    #print(i.text.split('\n'))
    pass

conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database('team') 
coll=db.get_collection('p20200117') #collection생성


for i in tag:
    li=i.text.split('\n')
    #print(li)
    #print('=========')
    
    for tmp in range(1, len(li),1):
        dic=dict()
        dic['day']=day.text
        dic['age']=li[0]
        dic['rank']=tmp
        dic['word']=li[tmp]
        coll.insert_one(dic)

conn.close()



"""
for y in ['2019','2018','2017']:
    for m in ['01','02','03','04','05','06','07','08','09','10','11','12']:
        for d in []
""" 
"""
#######본격 정보 모으기#######
for m in ['01','02']:
    #if (m=='01' or m=='03' or m=='05' or m=='07' or m=='08' or m=='10' or m=='12'):
        for d in ['01','02','03','04']:
            a=10
            y=2019
            h=12
            print(a,y,m,d,h)
            url="https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime={}-{}-{}T{}%3A00%3A00".format(a,y,m,d,h)
           
            print(url)
            driver.get(url)
            time.sleep(3)
            
            tag=driver.find_elements_by_class_name('ranking_box').find_elements_by_tag_name('li')
            
            dict0=dict()
            for tmp in tag:
            
                book=tmp.text.split("\n")

                dict0['rank']=book[0]
                dict0['word']=book[1]
                dict0['year']=y
                dict0['month']=m
                dict0['day']=d
                dict0['hour']=h
                dict0['age']=a
                coll.insert_one(dict0)
    #    else:
    #        for i in range(1,31,1):
    #            print("https://datalab.naver.com/keyword/realtimeList.naver?age=20s&datetime=2020-{}-{}T14%3A00%3A00&where=main".format(m, i))

conn.close()
"""