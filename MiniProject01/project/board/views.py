from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection 
cursor = connection.cursor()
from .models import board1

@csrf_exempt
def service3(request):
    if request.method == 'GET':
        # yr = request.GET.get('year', 2020)
        # print(type(yr), yr)        
        # sql = '''
        #     SELECT
        #         RANK,WORD,YEAR
        #     FROM 
        #         BOARD_BOARD1
        #     WHERE
        #         YEAR = %s
        # '''
        # cursor.execute(sql, yr)
        # data = cursor.fetchone()
        print('=====================get===========')
        data = 1
        yrwd = data
        return render(request, 'board/service3.html', {'yrwd':data})
    elif request.method == "POST":
        try :
            print('========업로드=========')
        except Exception as e:
            print('=========에러==========')
        return redirect('/board/service4') 

@csrf_exempt
def service4(request):
    if request.method == 'GET':
        return redirect('/board/service4') 


