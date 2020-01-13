# pip install cx_oracle
import cx_Oracle as oci

# 접속하기(아이디/암호@서버주소:포트번호/SID) 
    # 한글은 ,encoding='utf-8')
    # 아래 주소는 계속 살아있는 서울서버?!
conn = oci.connect('user7/1234@1.234.5.158:32764/xe', encoding='utf-8')
print(conn) # 확인

# 커서생성
cursor = conn.cursor()

# SELECT
sql = 'SELECT * FROM MEMBER'
cursor.execute(sql)
data = cursor.fetchall() #[(), (), ()]
print(data)

sql = '''
    INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    VALUES(:1, :2, :3, :4, SYSDATE)
    '''
arr = ['a12', 'a1', '홍길동', 33]
cursor.execute(sql, arr)
conn.commit()