## 서버 구동방법
    # ``` $ python manage.py migrate```
    # ``` $ python manage.py runserver```
    # 끄는방법은 다음과 같다.
    # ``` $ docker stop oracle12c
    # ``` $ docker-machine stop```
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
### DB 연결
from django.db import connection 
cursor = connection.cursor()  
    # 모델거치지 않고 sql-DB 바로 연결시 connection필요
    # cursor 사용

from django.contrib.auth.models import User
from django.contrib.auth import authenticate as auth1
from django.contrib.auth import login as login1
from django.contrib.auth import logout as logout1
    # django에서 제공하는 User 사용
from .models import board1 # models.py파일의 Table2클래스
from django.db.models import Sum, Max, Min, Count, Avg
import pandas as pd
import matplotlib.pyplot as plt
import io # byte로 변환
import base64 #byte를 base64로 변경
from matplotlib import font_manager, rc # 한글폰트 적용