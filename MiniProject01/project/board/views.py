from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection 
cursor = connection.cursor()
from .models import board1

@csrf_exempt
def service3(request):
    if request.method == 'GET':
        try:
            yr = request.GET.get('year', 2020)

            print(type(yr), yr)        
            sql = '''
                SELECT
                    RANK,WORD,YEAR,MONTH
                FROM 
                    BOARD_BOARD1
                WHERE
                    RANK = 1 AND YEAR = %s AND NO < 101
            '''
            cursor.execute(sql, yr)
            data = cursor.fetchall()

        except Exception as e:
            print( '================error===')
            data = '에러'
        return render(request, 'board/service3.html', {'yrwd':data})

@csrf_exempt
def service4(request):
    if request.method == 'GET':
        
        data = '키워드'

        return render(request, 'board/service4.html', {'word':data})        
        # return redirect('/board/service4') 
   
@csrf_exempt
def list(request): 
    sql = 'SELECT RANK FROM BOARD_BOARD1 WHERE NO <40 GROUP BY RANK'
    cursor.execute(sql)
    data = cursor.fetchall()
    print(type(data))
    print(data)
        # [(, , , ,column렬의 수 만큼 ), (row 행의 수 만큼)]
        # list.html으로 넘어갈때
        # list 변수에 data값을, title변수에 회원목록 문자로 해서 넘긴다.
        # 단 title키의 값은 하나뿐이라 list.html에서 {{title}}가능하고
        # list키의 값은 회원수만큼이므로 for문 사용했음
    
    # sql = 'SELECT WORD FROM BOARD_BOARD1 WHERE RANK=1'
    sql = 'SELECT DAY FROM BOARD_BOARD1 WHERE NO <40'
    cursor.execute(sql)
    data2 = cursor.fetchall()
    print(type(data2))
    print(data2)

    return render(request, 'board/list.html', {'tuple':data, 'list':data2})

