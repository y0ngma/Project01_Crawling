# 로그인 이후 페이지 들어가서 크롤링 하기
# https://chromedriver.chromium.org/downloads
from selenium import webdriver # pip install selenium
options     = webdriver.ChromeOptions()
    # options.add_argument('headless') # 화면 출력 안되게
options.add_argument("window-size=1920x1080")

driver      = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
            
driver.get("http://ihongss.com/webboard")

# 원하는 페이지 -F12- Copy-copy selector
driver.find_element_by_name("email").send_keys('20191216') 
driver.find_element_by_name("pw").send_keys('20191216')
    # by_name("html의 name값").send_keys(원하는값)
driver.find_element_by_css_selector('#form1 > div:nth-child(4) > input').click() 
    # by_css_selector('#포함!! copy selector한값').click()  

# xpath


driver.get("http://daum.net") # 1st로그인 이후의 페이지
html    = driver.page_source
soup    = BeautifulSoup(html, 'html_parser')
