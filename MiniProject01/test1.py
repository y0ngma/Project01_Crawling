from selenium import webdriver
import time


import pymongo
import cx_Oracle as oci

import requests
import json


options=webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)

conn=pymongo.MongoClient('192.168.99.100',32766)
db=conn.get_database("team") 
coll=db.get_collection("p20200116") #collection생성


for m in ['01','02']:
    #if (m=='01' or m=='03' or m=='05' or m=='07' or m=='08' or m=='10' or m=='12'):
        for d in ['01','02','03','04']:
            a=10
            y=2019
            h=12
            print(a,y,m,d,h)
            url="https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime={}-{}-{}T{}%3A00%3A00&where=main".format(a,y,m,d,h)
           
            print(url)
            driver.get(url)
            time.sleep(3)
            
            tag=driver.find_element_by_class_name('ranking_box').find_elements_by_tag_name('li')
            
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
    