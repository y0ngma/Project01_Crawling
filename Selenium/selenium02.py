# 스크립트 페이지에서 크롤링 하기
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('headless')

options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', 
    options=options)

driver.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

time.sleep(3) # 3초 스크립트 정보가져오도록 기다리기
tag = driver.find_element_by_class_name('rank_top1000_list') \
    .find_elements_by_tag_name("li")
    # print(tmp.find("a").text) # -> 가나다
    # <a href='#', id='aaa'>가나다< /a>
for tmp in tag:
    print(tmp.text.split("\n")) 
