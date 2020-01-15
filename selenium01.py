# `pip install selenium`
from selenium import webdriver
options     = webdriver.ChromeOptions()
# options.add_argument('headless') # 화면 출력 안되게
options.add_argument("window-size=1920x1080")

driver      = webdriver.Chrome('./Project01_Crawling/chromedriver.exe', chrome_options=options)
            
driver.get("http://ihongss.com")