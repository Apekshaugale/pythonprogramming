# import sqlite3
# conn=sqlite3.connect("database.db")
# cur=conn.cursor()  #foe giving address to the database
# cur.execute("""Create table if not exists premium_14(name varchar(20),age int,address varchar(20))""")
# cur.execute("Delete from premium_14")
# cur.execute(""" insert into premium_14 values("Navenn",26,"Banglore")""")
# cur.execute(""" insert into premium_14 values("Nita",25,"India")""")
# cur.execute(""" insert into premium_14 values("Priti",23,"Pune")""")
# res=cur.execute("""select *from premium_14""")
# print(res.fetchall())
# conn.commit()
# conn.close()


import mysql.connector
#for connecting to mysql
conn=mysql.connector.connect(host="localhost",user="root", password="Apeksha@2401",database="mydb")#for connecting to mysql

cur=conn.cursor()  #for giving address to the database

#to create database and table in mysql
cur.execute("Create  database if not exists database_name")
cur.execute("use database_name")
cur.execute("""Create table if not exists tablename (name varchar(20),age int,address varchar(20))""")
cur.execute("Delete from tablename")
sql_queies = """ insert into tablename values(%s,%s,%s)"""
data=[("Navenn", 26, "Banglore"), ("Nita", 25, "India"), ("Priti", 23, "Pune")]
cur.executemany(sql_queies,data)
conn.commit()
res=cur.execute("""select *from tablename""")
print(res.fetchall())
conn.commit()
conn.close()

# import sqlite3

# print("SQLite version:", sqlite3.sqlite_version)

