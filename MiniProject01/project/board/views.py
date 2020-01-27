from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from.models import board1
from.models import Table1
from django.db.models import Sum, Max, Min, Count, Avg
import pandas as pd
import random
import matplotlib.pyplot as plt
import io
import base64
from matplotlib import font_manager, rc
# Create your views here.
# from.models import board1
cursor=connection.cursor()


@csrf_exempt
def new(request):
    return render(request, "board/new.html")

@csrf_exempt

def test(request):
     if request.method=='GET':
        w = request.GET.get('search', "")
        #주소get한게 없을때
        if w == "":
            li=[]
            for i in range(0,5000,1):
                NOs = str(random.randrange(1,900000))
                li.append(NOs)

            #Distinct : 중복제거 (데이터에 저장된 단어들 중복제거한거 보여주겠다. )
            sql="""
                    SELECT WORD FROM BOARD_BOARD1
                    WHERE NO = %s 
            """
            
            result=[]
            for i in li : 
                num = []
                num.append(i)
                cursor.execute(sql, num)
                data1=cursor.fetchone()
                result.append(data1)
            print(result)
            return render(request, "board/test.html",{"data":result})


def search1(request):
     if request.method=='GET':
        w = request.GET.get('search', "")
        #주소get한게 없을때
        if w == "":
            li=[]
            for i in range(0,50,1):
                NOs = str(random.randrange(1,900000))
                li.append(NOs)

            #Distinct : 중복제거 (데이터에 저장된 단어들 중복제거한거 보여주겠다. )
            sql="""
                    SELECT DISTINCT WORD FROM BOARD_BOARD1
                    WHERE NO = %s 
            """
            
            result=[]
            for i in li : 
                num = []
                num.append(i)
                cursor.execute(sql, num)
                data1=cursor.fetchone()
                result.append(data1)
                return render(request, "board/search1.html",{"data":result})
            
    


def list1(request):
    w=request.GET.get('search', "")
    print(w)
    return render(request, "board/list1.html")

@csrf_exempt
def service1(request):
    if request.method=='GET':
        w = request.GET.get('search', "")
        #주소get한게 없을때
        if w == "":
            li=[]
            for i in range(0,50,1):
                NOs = str(random.randrange(1,900000))
                li.append(NOs)

            #Distinct : 중복제거 (데이터에 저장된 단어들 중복제거한거 보여주겠다. )
            sql="""
                    SELECT DISTINCT WORD FROM BOARD_BOARD1
                    WHERE NO = %s 
            """
            
            result=[]
            for i in li : 
                num = []
                num.append(i)
                cursor.execute(sql, num)
                data1=cursor.fetchone()
                result.append(data1)

            dataw=list(Table1.objects.all())
            print("@@",dataw)
            return render(request, 'board/service1.html',{"data":result,"abs":dataw})            
        #주소 get 한게 있을 때 
        else:
            #처음 나온날 검색
            str1='%'+ w +'%'
            sql="""
                SELECT * FROM(
                    SELECT WORD, YEAR, MONTH, DAY, TIME, ROW_NUMBER() OVER (PARTITION BY WORD ORDER BY YEAR, MONTH, DAY, TIME ASC) AS ROWN
                    FROM BOARD_BOARD1
                    WHERE WORD LIKE %s ) T1
                WHERE ROWN=1
            """            
            cursor.execute(sql, [str1])
            data1=cursor.fetchall()
            print(data1)
            #data1=data[0]
            #data2=data[len(data)-1]
            #print(data1)

            # 마지막으로 검색된 날
            sql="""
                SELECT* FROM(
                SELECT WORD, YEAR, MONTH, DAY, TIME, ROW_NUMBER() OVER (PARTITION BY WORD ORDER BY YEAR, MONTH, DAY, TIME DESC) AS ROWN1
                FROM BOARD_BOARD1
                WHERE WORD LIKE %s) T2
                WHERE ROWN1=1
            """
            cursor.execute(sql,[str1])
            data2=cursor.fetchall()
            print(data2)
            li=[]
            for i in range(len(data1)):
                li.append((data1[i],data2[i]))

            dataw=Table1.objects.values("no","title","content","writer")

            return render(request, 'board/service1.html',{"li":li,"abs":dataw})  #{{data.YEAR}}
    elif request.method=='POST':
    
        arr=[request.POST['title'],request.POST['content'],request.POST['writer']]
        print(arr)
        sql="""
            INSERT INTO BOARD_TABLE1(TITLE, CONTENT, WRITER)
            VALUES(%s, %s, %s)
        """
        cursor.execute(sql, arr)
        return redirect("/board/service1")

@csrf_exempt
def service2(request):
    if request.method=='GET':
        key =request.GET.get('search1', "")
        age =request.GET.get('age1', "")

        key3=request.GET.get('search2', "")
        age1=request.GET.get('age2', "")

        key4=request.GET.get('search3', "")
        age2=request.GET.get('age3', "")
        if key == "":###0개일때
            li=[]
            for i in range(0,10,1):
                NO1 = str(random.randrange(1,900000))
                li.append(NO1)

            sql="""
                    SELECT WORD FROM BOARD_BOARD1
                    WHERE NO = %s """
            result=[]
            for i in li : 
                num = []
                num.append(i)
                cursor.execute(sql, num)
                data1=cursor.fetchone()
                result.append(data1)
            print(result)
            # cursor.execute(sql, [li])
            # print(2)
            # data1=cursor.fetchone()
            # print(data1)
            return render(request, 'board/service2.html',{"data":result})            
        else:###1개일때
            if key3=="":
                sql="""
                    SELECT WORD, YEAR, MONTH, DAY, TIME, RANK, GENE FROM BOARD_BOARD1
                    WHERE WORD=%s AND GENE=%s
                    ORDER BY YEAR, MONTH, DAY, TIME ASC
                """

                cursor.execute(sql, [key,age])
                data=cursor.fetchall()

                data1 = []
                data2 = []
                for tmp in data:
                    data1.append( str(tmp[1])+"-"+str(tmp[2])+"-"+str(tmp[3])+"-"+str(tmp[4]) )
                    data2.append(21-tmp[5])
                
                print(data)
                #print(data1)
                # data1=data[0]
                # data2=data[len(data)-1]
                # print(data1)
                return render(request, 'board/service2.html',{"date":data, "data1":data1, "data2":data2, "key":key})  #{{data.YEAR}}
            else:### 2개일때
                if key3=="":
                    sql="""
                        SELECT WORD, YEAR, MONTH, DAY, TIME, RANK FROM BOARD_BOARD1
                        WHERE WORD=%s AND GENE=%s
                        ORDER BY YEAR, MONTH, DAY, TIME ASC
                    """

                    cursor.execute(sql, [key,age])
                    data=cursor.fetchall()

                    cursor.execute(sql, [key3,age1])
                    adddata=cursor.fetchall()
                    data1 = []
                    data2 = []
                    data3 = []
                    data4 = []
                    for tmp in data:
                        data1.append( str(tmp[1])+"-"+str(tmp[2])+"-"+str(tmp[3])+"-"+str(tmp[4]) )
                        data2.append(tmp[5])
                    for tmp in adddata:
                        data3.append( str(tmp[1])+"-"+str(tmp[2])+"-"+str(tmp[3])+"-"+str(tmp[4]) )
                        data4.append(tmp[5])
                    
                    print(data)
                    #print(data1)
                    # data1=data[0]
                    # data2=data[len(data)-1]
                    # print(data1)
                    return render(request, 'board/service2.html',{"date":data, "data1":data1, "data2":data2, "data3":data3, "data4":data4, "key":key, "key1":key3})  #{{data.YEAR}}
                else:#3개일때
                    
                    sql="""
                        SELECT WORD, YEAR, MONTH, DAY, TIME, RANK FROM BOARD_BOARD1
                        WHERE WORD=%s AND GENE=%s
                        ORDER BY YEAR, MONTH, DAY, TIME ASC
                    """

                    cursor.execute(sql, [key,age])
                    data=cursor.fetchall()
                    cursor.execute(sql, [key3,age1])
                    adddata=cursor.fetchall()
                    cursor.execute(sql, [key4,age2])
                    add1data=cursor.fetchall()

                    data1 = []
                    data2 = []
                    data3 = []
                    data4 = []
                    data5 = []
                    data6 = []
                    for tmp in data:
                        data1.append( str(tmp[1])+"-"+str(tmp[2])+"-"+str(tmp[3])+"-"+str(tmp[4]) )
                        data2.append(tmp[5])
                    for tmp in adddata:
                        data3.append( str(tmp[1])+"-"+str(tmp[2])+"-"+str(tmp[3])+"-"+str(tmp[4]) )
                        data4.append(tmp[5])
                    for tmp in add1data:
                        data5.append( str(tmp[1])+"-"+str(tmp[2])+"-"+str(tmp[3])+"-"+str(tmp[4]) )
                        data6.append(tmp[5])
                        
                    
                    print(data)
                    #print(data1)
                    # data1=data[0]
                    # data2=data[len(data)-1]
                    # print(data1)
                    return render(request, 'board/service2.html',{"date":data, "data1":data1, "data2":data2, "data3":data3, "data4":data4, "data5":data5, "data6":data6,"key":key, "key1":key3,"key2":key4})  #{{data.YEAR}}

@csrf_exempt
def test(request):
    if request.method=='GET':
   
        return render(request, 'board/test.html')

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
    
    # 스크립트용 
        word1=list()
        ranking1=list()
        word2=list()
        ranking2=list()
        word3=list()
        ranking3=list()
        word4=list()
        ranking4=list()
        word5=list()
        ranking5=list()
        word1.append(filtered[0][0])
        ranking1.append(filtered[0][1])
        
        word2.append(filtered[1][0])
        ranking2.append(filtered[1][1])
        
        word3.append(filtered[2][0])
        ranking3.append(filtered[2][1])
        
        word4.append(filtered[3][0])
        ranking4.append(filtered[3][1])
        
        word5.append(filtered[4][0])
        ranking5.append(filtered[4][1])
        
        return render(request,'board/service3.html',{'GN':GN,'MM':MM,\
            "DD":DD,"SS":SS,"RK":RK,'filtered':filtered,\
            "word1":word1,"rank1":ranking1,"word2":word2,"rank2":ranking2,\
            "word3":word3,"rank3":ranking3,"word4":word4,"rank4":ranking4,\
            "word5":word5,"rank5":ranking5})
   

@csrf_exempt
def service4(request): # 검색어 최초검색된 날짜, 최종일
    if request.method == 'GET':
        w=request.GET.get('search', "")
        sql="""
            SELECT YEAR, MONTH, DAY, TIME FROM BOARD_BOARD1
            WHERE NO IN (SELECT NO FROM BOARD_BOARD1 WHERE NO <= 1000)AND
                WORD = %s
            ORDER BY YEAR, MONTH, DAY, TIME ASC
            """
        cursor.execute(sql)
        data=cursor.fetchall()
        time1=data[0]
        time2=data[-1]
    
        return render(request,'board/service4.html',{'start':time1,'end':time2})
  