from mysql.connector import connect

def insertStudentsql(name,age,birth):
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
        # print('추가성공')
        return '추가성공'
    except Exception as err:
        # print( '실패',err)
        return '실패:'+err
    
def selectStudent():
    sql = "select * from student"
    conn = connect(host='localhost',
                user='root',
                password='6569',
                db='flaskdb',charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def deleteStudentsql(name):
    try:
        sql = "delete from student where person_name =%s"
        conn = connect(host='localhost',
                    user='root',
                    password='6569',
                    db='flaskdb',charset='utf8',
                    auth_plugin='mysql_native_password')
        cur = conn.cursor()
        
        cur.execute(sql,(name,))
        nrow = cur.rowcount
        conn.commit()
        conn.close()
        return f'삭제 {nrow}'
    except Exception as err:
        return err

