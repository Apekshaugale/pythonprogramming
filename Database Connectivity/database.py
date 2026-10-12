import mysql.connector

conn = mysql.connector.connect(host="localhost", username="root",database="Apeksha")

# #to create cursor object and cursor will give object address to execute the query
cur=conn.cursor()

 cur.execute("create database if not exists Apeksha")

 cur.execute("use Apeksha")

cur.execute("create table if not exists pratiksha(name varchar(20),age int(3),bgruop varchar(5))")


 sql="""insert into pratiksha(name,age,bgruop) values(%s,%s,%s)"""



data=[("pritit",22,"A+"),("ranju",24,"B+"),("ramu",35,"o+")]

 cur.executemany(sql,data)

 conn.commit()

 cur.execute("select * from pratiksha")
 rows = cur.fetchall()

 for i in rows:
     print(i)

 conn.close()

