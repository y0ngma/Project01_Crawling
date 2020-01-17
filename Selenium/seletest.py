# 이미지 크롤링
from selenium import webdriver
import urllib.request
import time
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(os.path.join(BASE_DIR))

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome('./chromedriver.exe', 
    options=options)

url= "https://datalab.naver.com/keyword/realtimeList.naver?datetime=2018-12-01T23%3A00%3A00"
driver.get(url)

# by 클래스명. by 태그
time.sleep(1) 
#<span class="time_txt _title_hms">23:00</span>
tag = driver.find_element_by_css_selector('.time_txt _title_hms')

print(tag.text)

    # BS
    # print(tmp.find("a").text) # -> 가나다
    # <a href='#', id='aaa'>가나다< /a>
    
# for tmp in tag:
#     print(tmp.text.split("\n")) 

# # image_view_0 copy-selector
# img = driver.find_element_by_css_selector("#image_view_0")
# print(img)

# time.sleep(1)
# file = img.get_attribute('src') # 찾은 태그 중 src값
# urllib.request.urlretrieve(file, "/download/a2.png")
