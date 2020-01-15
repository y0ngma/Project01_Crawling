# `pip install selenium`
from selenium import webdriver
options     = webdriver.ChromeOptions()
# options.add_argument('headless') # 화면 출력 안되게
options.add_argument("window-size=1920x1080")

driver      = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
            
driver.get("http://ihongss.com/webboard")

driver.find_element_by_name("email").send_keys('20191216') 
driver.find_element_by_name("pw").send_keys('20191216')
    # by_name("html의 name값").send_keys(원하는값)
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click() 
    # by_css_selector('#포함!! copy selector한값').click()  

# 원하는 페이지 -F12- Copy-copy selector

# selector
#form1 > div:nth-child(4) > input
# xpath
# driver.find_element_b