from bs4 import BeautifulSoup
import requests
'''
<div class="tit3">
    <a href="/movie/bi/mi/basic.nhn?code=135874" title="스파이더맨: 홈커밍">스파이더맨: 홈커밍</a>
</div>
'''

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str1= requests.get(url)
print(str1.text)

soupj = BeautifulSoup(str1.text, 'html.parser')

all_div_tit3 = soup.find_all('div', {"class":"tit3"})
for tmp in all_div_tit3:
    # <a href='#', id='aaa'>가나다< /a>
    print(tmp.find("a").text) # 가나다
    print(tmp.find("a").attrs) # {'href':'#', 'id':'aaa'}
    
