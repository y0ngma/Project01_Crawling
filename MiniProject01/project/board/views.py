from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection 
cursor = connection.cursor()
from .models import board1

@csrf_exempt
def service3(request):
    if request.method == 'GET':
    # html에서 dropdown 메뉴에서 보내줄 get name값 리스트    
        GN = ["10대","20대","30대","40대","50대이상"]
        MM = [i for i in range(1,13)]
        DD = [i for i in range(1,32)]
        SS = [i for i in range(0,24)]
    # 필터값 설정. 받아온 get name값 담기
        gn1  = request.GET.get('gene', '10대')
        gn1  = "%" +gn1+ "%"
        yy1  = request.GET.get('year', 2019)
        yy2  = request.GET.get('year', 2019)
        mm1  = request.GET.get('month', 7)
        mm2  = request.GET.get('month', 7)
        dd1  = request.GET.get('day', 1)
        dd2  = request.GET.get('day', 1)
        ss1  = request.GET.get('time', 4)
        ss2  = request.GET.get('time', 5)
        rk1  = request.GET.get('rank', 1)
        rk2  = request.GET.get('rank', 1)
    # 필터링 시작점
        filters = [gn1,yy1,yy2,mm1,mm2,dd1,dd2,ss1,ss2,rk1,rk2]
        print("=====================필터1===========",filters)
        sql = '''
        SELECT WORD FROM BOARD_BOARD1
        WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO < 10000) AND
            GENE LIKE %s AND 
            (YEAR  >= %s AND YEAR  <= %s) AND
            (MONTH >= %s AND MONTH <= %s) AND
            (DAY   >= %s AND DAY   <= %s) AND 
            (TIME  >= %s AND TIME  <= %s) AND 
            (RANK  >= %s AND RANK  <= %s)
        '''
        cursor.execute(sql, filters)
        filtered = cursor.fetchall()
        print("=====================필터된 값=============",filtered)
        
    # 카운터
        sql = '''
            SELECT WORD,COUNT(*) FROM (
                SELECT WORD FROM BOARD_BOARD1
                WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO <= 10000) 
                AND RANK = 1   
                )
            GROUP BY WORD
            ORDER BY COUNT(*) DESC
            '''
        cursor.execute(sql)
        data2 = cursor.fetchall()
        print(type(data2))
        print("========================",data2)

        return render(request,'board/service3.html',{'GN':GN,'MM':MM,\
            "DD":DD,"SS":SS,'filtered':filtered,"filters":filters,'ctwd':data2})
   


@csrf_exempt
def list(request): 
    
    w=request.GET.get('search', "")
    sql="""
        SELECT YEAR, MONTH, DAY, TIME FROM BOARD_BOARD1
        WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO <= 1000) 
        ORDER BY YEAR, MONTH, DAY, TIME ASC
        """
    cursor.execute(sql)
    data=cursor.fetchall()
    time1=data[0]
    time2=data[-1]
    print(time1, time2)

    sql = '''
        SELECT WORD,COUNT(*) FROM (
            SELECT WORD FROM BOARD_BOARD1
            WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO <= 1000) 
            AND RANK = 1   
            )
        GROUP BY WORD
        ORDER BY COUNT(*) DESC
        '''
    cursor.execute(sql)
    data2 = cursor.fetchall()
    print(type(data2))
    print(data2)


    return render(request,'board/list.html',{'start':time1, 'end':time2, 'ctwd':data2})
       

@csrf_exempt
def service4(request):
    if request.method == 'GET':
        
        data = '키워드'

        return render(request, 'board/service4.html', {'word':data})        
        # return redirect('/board/service4') 