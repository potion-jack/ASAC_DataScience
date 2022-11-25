from mysql.connector import connect


def insertStudent(name,age,birth):
    try:
        sql = "insert into student values(%s,%s,%s)"
        conn = connect(host='localhost',
                    user='root',
                    password='6569',
                    db='flaskdb',charset='utf8',
                    auth_plugin='mysql_native_password')
        cur = conn.cursor()
        cur.execute(sql,(name,age,birth))
        conn.commit()
        conn.close()
        print('추가성공')
    except Exception as err:
        print( '실패',err)
    
"""
from mysql.connector import connect

try:
    sql = "insert into student values('홍길동',20,'1999-11-12')"
    conn = connect(host='localhost',
                   user='root',
                   password='6569',
                   db='flaskdb',charset='utf8',
                   auth_plugin='mysql_native_password')
    cur = conn.cursor()
    cur.execute( sql )
    conn.commit()
    conn.close()
    print('추가성공')
except Exception as err:
    print( '실패',err)

"""