import mysql.connector

conn=mysql.connector.connect(host="localhost",user='root',password='')

cur=conn.cursor()

cur.execute('Create database if not exists Ram')
 
cur.execute("""Use Ram""")

cur.execute("""Create table if not exists hello(hname varchar(20),age int ,class varchar(15))""")

sql="""insert into hello(hname,age,class) values(%s,%s,%s)"""

data=[('namu',23,"A"),('tupu',34,"B"),('rohini',30,"d")]

cur.executemany(sql,data)

conn.commit()
cur.execute("SELECT * FROM hello")
res = cur.fetchall()


for i in res:
  print(i)
conn.close()