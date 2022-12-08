from mysql.connector import pooling

pool = pooling.MySQLConnectionPool(
    pool_name='mypool',
    pool_reset_session=True,
    pool_size=3,
    host='localhost',
    port='3306',
    database='flaskdb',
    user='root',
    password='6569'
)

def insertStudentPool(name,age,birth):
    con = pool.get_connection()
    c = con.cursor()
    c.execute('insert into student values(%s,%s,%s)',(name,age,birth))
    con.commit()
    nRow = c.rowcount
    con.close()
    return f"추가성공:{nRow}"

"""def selectProcedure():
    con = pool.get_connection()
    c = con.cursor()
    # c.execute('select * from student')
    # c.fetchall()
    c.callproc('selectProc')
    for result in c.stored_results():
        print(result.fetchall())
    con.close()
    return """