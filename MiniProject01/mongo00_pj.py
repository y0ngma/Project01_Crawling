
##영재
from selenium import webdriver
import time


import pymongo
import cx_Oracle as oci

import requests
import json

conn=pymongo.MongoClient('192.168.99.100',32766)

db=conn.get_database("2019")  

table=db.get_collection("12")

conn=oci.connect('admin/1234@192.168.99.100:32764/xe', encoding='utf-8')

cursor=conn.cursor()




options=webdriver.ChromeOptions()
options.add_argument('headless')  #크롬이 실행은 되지만 안보임(백그라운드에서 돌아간다.)

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
#냅다 정보를 긁어오는게 아니라 창을 열어서 정보를 긁어온다. 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver=webdriver.Chrome('./chromedriver.exe',chrome_options=options)

for i in range(10,51,10):
    #for j in [10,19]:
        driver.get("https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime=2020-01-14T12%3A56%3A00#none".format(i))
        print('=================',i,'================')
        time.sleep(3)
        ########방법1################################
        tag1=driver.find_element_by_class_name('item_num')
        tag2=driver.find_element_by_class_name('item_title')
        #######방법2#################################
        # tag=driver.find_elements_by_tag_name("span")


        for tmp in range(0,len(tag1),1):
            print(tmp.text.split("\n"))
            

            
            
###준호###
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', 
    options=options)

driver.get("https://datalab.naver.com/keyword/realtimeList.naver?age={}s&datetime=2020-01-14T12%3A56%3A00#none")

time.sleep(3)



tag = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[2]/div[2]/div') \
    .find_elements_by_tag_name("li")


#tag = driver.find_element_by_class_name('list_wrap.typeRealtime').find_elements_by_tag_name("li")

for tmp in tag:
    print(tmp.text.split("\n"))
