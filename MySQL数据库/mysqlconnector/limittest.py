# -*- coding: UTF-8 -*-
"""
@File: limittest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:53
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="python_connect"
)
mycursor=mydb.cursor()
# sql="select * from customers limit 5"#查询前五个
sql = "select * from customers limit 5 offset 2"#从位置3开始，返回5条记录，或者写成         limit 2,5
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)