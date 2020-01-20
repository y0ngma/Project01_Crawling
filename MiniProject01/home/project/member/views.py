from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
# Create your views here.
# from.models import member1


cursor=connection.cursor()
# Create your views here.
#홈페이지
@csrf_exempt
def index(request):
        return render(request, "member/index.html")
#회원가입
@csrf_exempt
def join(request):
    if request.method =='GET':
        return render(request, "member/join.html")
    elif request.method== 'POST':
        id = request.POST['id']# HTML에서 넘어온 값 받기
        pw = request.POST['pw']
        na = request.POST['name']
        ag = request.POST['age']
        gen = request.POST['gen']
                
        ar=[id, pw, na, ag, gen]#4개로 각각 왔는데 리스트로 만들어서 관리하기 편하게 
        #DB에 추가함

        
        sql='''        
        INSERT INTO MEMBER_MEMBER1 (ID,PW,NAME,AGE,GEN,JOINDATE)
        VALUES(%s, %s, %s, %s, %s, SYSDATE)
        '''
        cursor.execute(sql, ar)


        #크롬에서 127.0.0.1:8000/member/index 엔터키를 
        return redirect('/member/index')










#로그인
@csrf_exempt
def login(request):
    if request.method =='GET':
        return render(request, "member/login.html")
    elif request.method== 'POST':
        # HTML에서 넘어온 값 받기    
        ar = [request.POST['id'], request.POST['pw']]
        
        #DB에 추가함 id는 id로 받고 pw는 밑에 pw=%s에 넣는다 그리고 난 후 아이디와 이름을 골라서 화면에뿌려주는것. 로그인
        sql="SELECT * FROM MEMBER_MEMBER1 WHERE ID=%s AND PW=%s"

        cursor.execute(sql, ar)
       
        data=cursor.fetchone()#한줄 가져 오기 아이디가 한개니깐 중복 되면 데이터 베이스가 엉망이란 소리 이므로.
       
        if data:
            request.session['userid']=data[0]
            request.session['username']=data[1]
            return redirect('/member/index')
        return redirect('/member/login')
        
#로그아웃
@csrf_exempt
def logout(request):
    if request.method =='GET' or request.method == 'POST':
        del request.session['userid']
        del request.session['username']
        return redirect('/member/index')

#회원정보 수정
@csrf_exempt
def edit(request):
    if request.method =='GET':
        ar=[request.session['userid']]

        sql = '''
            SELECT * FROM MEMBER_MEMBER1 WHERE ID=%s
        '''

        cursor.execute(sql, ar)
        data=cursor.fetchone()
        
        return render(request, "member/edit.html",{"one":data})

    elif request.method == 'POST':
        ar = [
            request.POST['name'],
            request.POST['age'],
            request.POST['id'],
        ]
        
        sql='''
            UPDATE MEMBER_MEMBER1 SET NAME=%s, AGE=%s
            WHERE ID=%s
        '''
        cursor.execute(sql, ar)

        return redirect("/member/index")

        # HTML에서 넘어온 값 받기  



