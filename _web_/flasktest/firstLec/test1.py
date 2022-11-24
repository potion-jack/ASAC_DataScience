# pip install mysql-connector-python

from mysql.connector import  pooling



pool= pooling.MySQLConnectionPool(pool_name = "mypool",pool_reset_session=True,
                              pool_size = 3, host='localhost',port='3306',
                              database='sqldb',user='root', password='1234')

con = pool.get_connection()
c = con.cursor()
c.execute('insert into student values(%s,%s,%s)',('이순신',50,'1989-05-12'))
con.commit()
print( c.rowcount)
c.close()
con.close()