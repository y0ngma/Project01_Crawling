from bs4 import BeautifulSoup
import requests
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20170714"
str1= requests.get(url)
    # print(str1.text)

# HTML 문서 검색
# soup.find_all -> 여러개
# soup.find     -> 첫번째것 3개
# soup.select   -> 여러개

soup = BeautifulSoup(str1.text, 'html.parser')
    # <div class = 'tit3'>< />과 같이 id: xx지정한값만 가져오기
all_div_tit3 = soup.find_all('div', {"class":"tit3"}) 
    # soup.select
print(all_div_tit3)
    '''
    <div class="tit3">
        <a href="/movie/bi/mi/basic.nhn?code=135874" title="스파이더맨: 홈커밍">스파이더맨: 홈커밍</a>
    </div>
    '''

for tmp in all_div_tit3:
    print(tmp.find("a").text) # -> 가나다
        # <a href='#', id='aaa'>가나다< /a>
    print(tmp.find("a").attrs) # {'href':'#', 'title':'영화제목'}
        # <a id="알고싶은값1" id="알고싶은값2">가나다</a>
        '''
        {href="/movie/bi/mi/basic.nhn?code=135874" 
        title="스파이더맨: 홈커밍"}
        '''
