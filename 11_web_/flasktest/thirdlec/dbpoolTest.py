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

# con = pool.get_connection()
# c = con.cursor()
# c.execute('insert into student values(%s,%s,%s)',('이순신',50,'1989-05-12'))
# con.commit()
# print(c.rowcount)
# c.close()
# con.close()


# con = pool.get_connection()
# c = con.cursor()
# # c.execute('select * from student')
# # c.fetchall()
# c.callproc('selectProc')
# for result in c.stored_results():
#     print(result.fetchall())
#     print('-----')
# con.close()

con = pool.get_connection()
c = con.cursor()
c.callproc('insertproc',('myproc',22,'1993-03-12'))
print(c.rowcount)
con.close()