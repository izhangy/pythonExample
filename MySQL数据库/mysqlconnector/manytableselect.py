# -*- coding: UTF-8 -*-
"""
@File: manytableselect.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 15:04
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="python_connect"
)
mycursor=mydb.cursor()
sql = "select users.name as user, products.name as pro from users inner join products on users.fav = products.id"
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)