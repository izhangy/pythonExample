# -*- coding: UTF-8 -*-
"""
@File: sorttest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:36
"""
import mysql.connector
mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "123456",
    database= "python_connect"
)
mycursor = mydb.cursor()#对数据库进行操作
sql = "select * from customers order by name"
#desc倒序
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)