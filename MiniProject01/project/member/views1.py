# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# ### DB 연결
# from django.db import connection 
# cursor = connection.cursor()  
#     # 모델거치지 않고 sql-DB 바로 연결시 connection필요
#     # cursor 사용
# from matplotlib import font_manager, rc # 한글폰트 적용

# def index(request):
#     if request.method == 'GET':
#         return render(request, 'member/index.html')
    
# def join(request):
#     if request.method == 'GET':
#         return render(request, 'member/join.html')
#     elif request.method == 'POST':
#         id = request.POST['id']
#         pw = request.POST['pw']
#         na = request.POST['name']
#         ag = request.POST['age']
#         ge = request.POST['gen']

#         ar = [id, pw, na, ag, ge] # list로 만듬     
#     # sql용
#         # sql ='''
#         #     INSERT INTO MEMBER(ID,PW,NAME,AGE,GENDER,JOINDATE)
#         #     VALUES (%s, %s, %s, %s,%s, date('now'))
#         #     '''   
#     # oracle용
#         sql ='''
#             INSERT INTO MEMBER(ID,PW,NAME,AGE,GENDER,JOINDATE)
#             VALUES (%s, %s, %s, %s, $s, SYSDATE)
#             '''
#         cursor.execute(sql, ar) # 위 sql 에 ar리스트를 순서대로 넣어라.그래서 서로 동일순. 
#             # 다만, 회원가입html에서 입력순이랑 ar순서 무관. 액셀이 아니기 때문에 값을 지정해줘야 찾아가게된다.
#         return redirect('/member/index')

# def login(request):
#     if request.method == 'GET':
#         print('loginGET')
#         return render(request, 'member/login.html')
#     elif request.method == 'POST':
#         print('loginPOST')
#         ar = [request.POST['id'], request.POST['pw']]
#         sql = '''
#         SELECT ID, NAME
#         FROM MEMBER
#         WHERE ID=%s AND PW=%s
#         '''
#             # *은 모두 가져오기. 가져올 때 순서대로
#             # SELECT*FROM MEMBER WHERE ID=%s AND PW=%s
#         cursor.execute(sql, ar)
#         data = cursor.fetchone()
#         print(type(data))
#         print(data)

#         if data:
#             request.session['userid']   =data[0]
#             request.session['username'] =data[1]
#             for key, value in request.session.items():
#                 print('키값은{} 이고 밸류는{}이다'.format(key, value))
#             return redirect('/member/index')
#             # 세션. 
#             # 암호는 가져오면 보안에 취약.
#         print('로그인실패')
#         return redirect('/member/index')

# def logout(request):
#     if request.method == 'GET' or request.method== 'POST':
#         del request.session['userid']
#         del request.session['username']
#         return redirect('/member/index')

# def delete(request):
#     if request.method == 'GET'or request.method== 'POST':
#         ar = [request.session['userid']]
#         sql = 'DELETE FROM MEMBER WHERE ID=%s'
#         cursor.execute(sql, ar)
#         return redirect('/member/logout')

# def list(request): 
#     # sql 쓴 이유 :
#         # 데이터가 먼저냐 화면이 먼저냐?
#         # GET을 쓰지 않은 이유
#         # ID 기준으로 오름차순으로 가져오자
#     sql = 'SELECT*FROM MEMBER ORDER BY ID ASC'
#     cursor.execute(sql) # 
#         # cursor는 sql 실행하기위한 단위
#         # connection.execute를 사용해도 되지만 아직 세부단위 설정되지 않음
#     data = cursor.fetchall() # sql문 실행의 결과값 가져와라
#     print(type(data)) # 리스트
#     print(data)
#         # [(, , , ,column렬의 수 만큼 ), (row 행의 수 만큼)]
#         # list.html으로 넘어갈때
#         # list 변수에 data값을, title변수에 회원목록 문자로 해서 넘긴다.
#         # 단 title키의 값은 하나뿐이라 list.html에서 {{title}}가능하고
#         # list키의 값은 회원수만큼이므로 for문 사용했음
#     sql = 'SELECT*FROM MEMBER1 ORDER BY ID ASC' # vip맴버리스트 취합
#     cursor.execute(sql)
#     data2 = cursor.fetchall()
#     print(type(data)) # 리스트
#     print(data) 
#     return render(request, 'member/list.html', {'list':data, 'list2':data2, 'title':'회원목록'})


# def member(request):
#     if request.method == 'GET':
#         return redirect('/member/list')