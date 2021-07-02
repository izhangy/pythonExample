# -*- coding: UTF-8 -*-
"""
@File: delectrecord.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:42
"""
import mysql.connector
mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "123456",
    database= "python_connect"
)
mycursor = mydb.cursor()
# sql = "delete from customers where address = 'Apple st 652'"
#防注入%s
sql = "delete from customers where address = '%s'"
adr = "Apple st 652"
mycursor.execute(sql, adr)
# mycursor.execute(sql)
mydb.commit()#插入、更新、删除操作都要有commit
print(mycursor.rowcount)#删除记录
