# 이미지 크롤링
from selenium import webdriver
import urllib.request
import time
import os
from selenium.webdriver.common.keys import Keys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('============== base dir============')
print(os.path.join(BASE_DIR))

options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   
options.add_argument("lang=ko_KR")    
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 

driver = webdriver.Chrome(os.path.join(BASE_DIR,'selenium', 'chromedriver.exe'), options=options)
    #'../하위폴더'

driver.get('https://naver.com')

# 원하는 이미지 검색실행 후 긁어 오기
# 네이버 검색칸에 우클릭 검사<input id="query".. ->copy xpath
driver.find_element_by_xpath('//*[@id="query"]').send_keys('사과')
driver.find_element_by_xpath('//*[@id="query"]').send_keys(Keys.ENTER)

driver.find_element_by_xpath('//*[@id="lnb"]/div/div[1]/ul/li[2]/a/span') \
    .click()
  
link = []  
for i in range(1, 6, 1): 
    try:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[2]/div[2]/div['+ str(i) + ']/a[1]/img') 
    except:
        img = driver.find_element_by_xpath('//*[@id="_sau_imageTab"]/div[1]/div[2]/div['+ str(i) + ']/a[1]/img')   
    #print(img)    
    link.append(img.get_attribute("src"))

print(link)    

#파일명 n0.jpg  n1.jpg, n2.jpg, n3.jpg, n4.jpg
for idx, tmp in enumerate(link):
    urllib.request.urlretrieve(tmp, os.path.join(BASE_DIR,'download', "n"+str(idx)+".jpg" ))
