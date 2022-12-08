# import pymysql
from mysql.connector import connect

# STEP 2: MySQL Connection 연결
con = connect(host='localhost', user='root', password='1234',
                       db='sqldb', charset='utf8') # 한글처리 (charset = 'utf8')
 
# STEP 3: Connection 으로부터 Cursor 생성
cur = con.cursor()
 
# STEP 4: SQL문 실행 및 Fetch
sql = "insert into student values(%s,%s,%s)"
cur.execute(sql, ('이순신',50,'1989-03-12'))
con.commit()
print( cur.rowcount)
# sql = "select * from student"
# cur.execute(sql)
# # 데이타 Fetch
# rows = cur.fetchall()
# print(rows)     # 전체 rows

# STEP 5: DB 연결 종료
con.close()