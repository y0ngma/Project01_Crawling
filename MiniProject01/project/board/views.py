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
        MM = [int(i) for i in range(1,13)]
        DD = [int(i) for i in range(1,32)]
        SS = [int(i) for i in range(0,24)]
        RK = [int(i) for i in range(1,21)]
    
    # 필터값 설정. 받아온 get name값 담기
        rk1  = int(request.GET.get('rank', 1))
        rk2  = int(request.GET.get('rank2', 1))
        gn1  = request.GET.get('gene', '10대') #10+20+30+40+50?
        gn1  = "%" +gn1+ "%"
        yy1  = str(request.GET.get('year', 2019))
        yy2  = str(request.GET.get('year2', 2019))
        mm1  = str(request.GET.get('month', 7))
        mm2  = str(request.GET.get('month2', 7))
        dd1  = str(request.GET.get('day', 1))
        dd2  = str(request.GET.get('day2', 1))
        ss1  = str(request.GET.get('time', 4))
        ss2  = str(request.GET.get('time2', 5))

        filters=[gn1,int(yy1+mm1+dd1+ss1),int(yy2+mm2+dd2+ss2),rk1,rk2]
    # 필터링 시작점
        sql = '''
        SELECT WORD,COUNT(*) FROM (
                SELECT WORD 
                FROM BOARD_BOARD1 
                WHERE 
                    GENE LIKE %s AND
                    TO_NUMBER(YEAR||MONTH||DAY||TIME) >= %s AND
                    TO_NUMBER(YEAR||MONTH||DAY||TIME) <= %s AND
                    RANK >= %s AND RANK <= %s
                )
            GROUP BY WORD
            ORDER BY COUNT(*) DESC
        '''
        cursor.execute(sql, filters)
        filtered = cursor.fetchall()
        print("=====================필터된 값=======",filtered)
        print("=====================필터1===========",filters)
        return render(request,'board/service3.html',{'GN':GN,'MM':MM,\
            "DD":DD,"SS":SS,"RK":RK,'filtered':filtered,\
                "filters":filters})
   

@csrf_exempt
def list(request): # 검색어 최초검색된 날짜, 최종일
    w=request.GET.get('search', "")
    sql="""
        SELECT YEAR, MONTH, DAY, TIME FROM BOARD_BOARD1
        WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO <= 1000)AND
            WORD LIKE %s
        ORDER BY YEAR, MONTH, DAY, TIME ASC
        """
    cursor.execute(sql, [w])
    data=cursor.fetchall()
    time1=data[0]
    time2=data[-1]
    
    return render(request,'board/list.html',{'start':time1,'end':time2})
       
@csrf_exempt
def service4(request):
    if request.method == 'GET':
        
        data = '키워드'

        return render(request, 'board/service4.html', {'word':data})        
        # return redirect('/board/service4') 