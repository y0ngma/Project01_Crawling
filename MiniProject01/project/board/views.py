from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection 
cursor = connection.cursor()
from .models import board1

def content1(request):
    if request.method == 'GET':
        yr = request.GET.get('year', 2020)
        print(type(yr), yr)        
        sql = '''
            SELECT
                RANK,WORD,YEAR
            FROM 
                BOARD_BOARD1
            WHERE
                YEAR = %s
        '''
        cursor.execute(sql, yr)
        data = cursor.fetchone()

        return render(request, 'board/content1.html', {'yrwd':data})

def content(request):
    if request.method == 'GET':
        no = request.GET.get('no', 0)
        print(type(no), no)
        if no == 0:
            return redirect('/board/list') # <a href 와 같음 
    # 세션을 이용, 새로고침에 의한 조회수 증가 방지법  
        # list함수로 부터 
        if request.session['hit'] == 1:
            sql = '''
                UPDATE BOARD_TABLE1 
                SET HIT = HIT+1
                WHERE NO = %s
            '''
            cursor.execute(sql, [no])
            request.session['hit'] = 0 # # 글 번호가 일치하는것만 가져오니까 1개
    # 이전글/다음글 
        # NVL이용 없을때 디폴트값 0 주기
        sql = '''
            SELECT NVL(MAX(NO), 0) 
            FROM BOARD_TABLE1
            WHERE NO < %s
        '''
        cursor.execute(sql, [no])
        prv = cursor.fetchone() 
        sql = '''
            SELECT NVL(MIN(NO), 0) 
            FROM BOARD_TABLE1
            WHERE NO > %s
        '''
        cursor.execute(sql, [no])
        nxt = cursor.fetchone() 
        # 첫글/마지막글의 번호 가져오기
        sql = '''
            SELECT MAX(NO)
            FROM BOARD_TABLE1
        '''
        cursor.execute(sql)
        last = cursor.fetchone() 
        sql = '''
            SELECT MIN(NO)
            FROM BOARD_TABLE1
        '''
        cursor.execute(sql)
        first = cursor.fetchone() 
    # 내용 가져오기
        sql = '''
            SELECT
                NO, TITLE, CONTENT, WRITER, HIT, 
                TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'), IMG
            FROM 
                BOARD_TABLE1
            WHERE
                NO = %s
        '''
        cursor.execute(sql, [no])
        data = cursor.fetchone()  #(89,)
        print('가져온 데이터는 =>', data)
    #    
        if data[6] : # BLOB형식으로 DB에 첨부된 사진등이있을때
            img = data[6].read() # byte배열을 img에 넣음
            img64 = b64encode(img).decode('utf-8')
        else : # 없을때 '사진없음' 이라는 이미지를 표시
            file=open('./static/img/default.jpg', 'rb')
            img = file.read()
            img64 = b64encode(img).decode('utf-8')
        print('data:{} img64:{}\n last:{}{}\n last[0]:{}{}\n str(last):{} '\
            .format(type(data),type(img64),last,type(last),last[0],type(last[0]),str(last[0])))
        return render(request, 'board/content.html', 
            {'one':data, 'image':img64, 'prv':prv[0], 
            'nxt':nxt[0], 'first':str(first[0]), 'last':str(last[0])    }   )

def write(request):
    if request.method == "GET":
        return render(request, 'board/write.html')
    elif request.method == "POST":
        return redirect('/board/list')

@csrf_exempt
def list(request):
    if request.method == 'GET':
        request.session['hit'] = 1
        writer = request.GET.get('writer', None)

        txt  = request.GET.get('txt', '')
        page = int(request.GET.get('page', 1))

        sql=""
        if writer != None:
            arr = [writer, page*10-10+1, page*10]
            sqlz = """
                SELECT 
                    NO, TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'),
                    ROW_NUMBER() OVER (ORDER BY NO DESC) ROWN
                FROM 
                    BOARD_TABLE1 
                WHERE
                    writer=%s"""

            sql = "SELECT COUNT(*) FROM (" + sqlz +")"
            cursor.execute(sql,[writer])
            
            cnt = cursor.fetchone()[0]
                # cnt = Table1.objects.all().count() # 같은결과
            tot = (cnt-1)//10+1
            sql = """
                SELECT * FROM(
                    SELECT 
                        NO, TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'),
                        ROW_NUMBER() OVER (ORDER BY NO DESC) ROWN
                    FROM 
                        BOARD_TABLE1 
                    WHERE
                        writer=%s
                    )
                WHERE ROWN BETWEEN %s AND %s
            """
            cursor.execute(sql,arr)
        else:    
            arr = [page*10-10+1, page*10]
            sqlz = "BOARD_TABLE1"

            sql = "SELECT COUNT(*) FROM (" + sqlz +")"
            cursor.execute(sql)
            
            cnt = cursor.fetchone()[0]
                # cnt = Table1.objects.all().count() # 같은결과
            tot = (cnt-1)//10+1
            sql = """
                SELECT * FROM(
                    SELECT 
                        NO, TITLE, WRITER, HIT, TO_CHAR(REGDATE, 'YYYY-MM-DD HH:MI:SS'),
                        ROW_NUMBER() OVER (ORDER BY NO DESC) ROWN
                    FROM 
                        BOARD_TABLE1 
                    )
                WHERE ROWN BETWEEN %s AND %s
            """
            cursor.execute(sql, arr)
        data = cursor.fetchall()

        # sql = "SELECT COUNT(*) FROM BOARD_TABLE1"
        # sql = "SELECT COUNT(*) FROM (" + sqlz +")"
        # cursor.execute(sql)
        # print(len(data))
        
        # cnt = cursor.fetchone()[0]
        #     # cnt = Table1.objects.all().count() # 같은결과
        # tot = (cnt-1)//10+1
        
        return render(request, 'board/list.html', {"list":data, "writer":writer
            , 'pages':range(1, tot+1)})