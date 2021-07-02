# -*- coding: UTF-8 -*-
"""
@File: selectwhere.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:25
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="python_connect"
)
mycursor = mydb.cursor()
# sql = "select * from customers where address = 'Apple st 652'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

"""
通配符：
%way  --表示查询way开头的记录
%way% --表示包含way的记录
way% --表示以way结尾的记录
"""
sql1 = "select * from customers where address like '%Low%'"
mycursor.execute(sql1)
myresult1 = mycursor.fetchall()
for x in myresult1:
    print(x)

#防止sql注入，使用占位符%s转义查询
sql2 = "select * from customers where address=%s"
adr = ("Lowstreet 4",)
mycursor.execute(sql2, adr)
myresult2 = mycursor.fetchall()
for x in myresult2:
    print(x)