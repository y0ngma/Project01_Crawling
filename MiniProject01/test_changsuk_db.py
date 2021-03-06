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
    for d in range (26,32,1):
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
                print(dbname,time2,'**************정지*****************')
                break:            

conn_m.close()       
conn_o.close() # 오라클 연결 끊기
