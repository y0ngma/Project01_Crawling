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
        a = list('0123')
        b = list('0123456789')
        serial= [i+j for i in a for j in b]
        MM = serial[1:13]
        # DD = serial[1:32]
        # SS = serial[:24]
    
    # 필터값 설정. 받아온 get name값 담기
        rk1  = int(request.GET.get('rank', 1))
        rk2  = int(request.GET.get('rank2', 1))

        gn1  = request.GET.get('gene', '10대') #10+20+30+40+50?
        gn1  = "%" +gn1+ "%"

        yy1  = str(request.GET.get('year', 2019))
        yy2  = str(request.GET.get('year2', 2020))
        mm1  = str(request.GET.get('month', "01"))
        mm2  = str(request.GET.get('month2', "01"))

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
            "DD":DD,"SS":SS,"RK":RK,'filtered':filtered,"chart": {'사과1': 500,  '호두': 200,        '블루베리': 666,        '치즈': 54,        '딸기': 120     }})
   