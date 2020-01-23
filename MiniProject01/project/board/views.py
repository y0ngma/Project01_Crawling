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
        # MM=['01','02','03','04','05','06','07','08','09']
        # for i in range(10, 13, 1):
        #     MM.append(str(i))

        # MM = [int(i) for i in range(1,13)]
        DD = [int(i) for i in range(1,32)]
        SS = [int(i) for i in range(0,24)]
        RK = [int(i) for i in range(1,21)]

        GN = ["10대","20대","30대","40대","50대이상"]

        print("AA")
        a = ["0","1","2","3"]
        print(a)
        b = ["0","1","2","3","4","5","6","7","8","9"]
        serial= [i+j for i in a for j in b]
        MM = serial[1:13]
        # DD = serial[1:32]
        # SS = serial[:24]
        # RK = [str(i) for i in range(1,21)]
    
        # 필터값 설정. 받아온 get name값 담기
        rk1  = int(request.GET.get('rank', 1))
        rk2  = int(request.GET.get('rank2', 1))

        gn1  = request.GET.get('gene', '30대') #10+20+30+40+50?
        gn1  = "%" +gn1+ "%"

        yy1  = str(request.GET.get('year', 2019))
        yy2  = str(request.GET.get('year2', 2020))

        dd1  = str(request.GET.get('day', "1"))
        if len(dd1) < 2 :
            dd1 = "0" + dd1

        dd2  = str(request.GET.get('day2', "1"))
        if len(dd2) < 2  :
            dd2 = "0" + dd2

        ss1  = str(request.GET.get('time', "1"))
        if len(ss1) < 2  :
            ss1 = "0" + ss1

        ss2  = str(request.GET.get('time2', "1"))
        if len(ss2) < 2  :
            ss2 = "0" + ss2

        mm1  = str(request.GET.get('month', "01"))
        mm2  = str(request.GET.get('month2', "01"))
        
        filters=[gn1,int(yy1+mm1+dd1+ss1),int(yy2+mm2+dd2+ss2),rk1,rk2]
   
    # 필터링 시작점
        sql = '''
        SELECT WORD,COUNT(*) FROM (
            SELECT WORD 
            FROM BOARD_BOARD1 
            WHERE 
                GENE LIKE %s AND
                TO_NUMBER(
                    YEAR||LPAD(MONTH,2,0)||LPAD(DAY,2,0)||LPAD(TIME,2,0)
                    ) >= %s AND
                TO_NUMBER(
                    YEAR||LPAD(MONTH,2,0)||LPAD(DAY,2,0)||LPAD(TIME,2,0)
                    ) <= %s AND
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
            "DD":DD,"SS":SS,"RK":RK,'filtered':filtered})
   

@csrf_exempt
def list(request): # 검색어 최초검색된 날짜, 최종일
    # w=request.GET.get('search', "")
    sql="""
        SELECT YEAR, MONTH, DAY, TIME FROM BOARD_BOARD1
        WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO <= 1000)
           
        ORDER BY YEAR, MONTH, DAY, TIME ASC
        """
    cursor.execute(sql)
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