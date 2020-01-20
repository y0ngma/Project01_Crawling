from django.shortcuts import render, redirect
from django.http import HttpResponse
### DB 연결
from django.db import connection 
cursor = connection.cursor()  
    # 모델거치지 않고 sql-DB 바로 연결시 connection필요
    # cursor 사용

def index(request):
    if request.method == 'GET':
        return render(request, 'member/index.html')

def join(request):
    if request.method == 'GET':
        return render(request, 'member/join.html')