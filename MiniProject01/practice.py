
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

                for tmp in range(1, len(li),1):
                    dic=dict()
                    #dic['day']=day.text
                    dic['age']=age
                    dic['rank']=tmp
                    dic['word']=li[tmp]
                    dic['year']='2019'
                    dic['month']='11'
                    dic['day']=d
                    coll.insert_one(dic)