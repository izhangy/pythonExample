# -*- coding: UTF-8 -*-
"""
@File: createmysql.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 12:04
"""
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    auth_plugin = "mysql_native_password"
)
#创建数据库
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE python_connect")

#检查数据库是否存在
mycursor = mydb.cursor()
mycursor.execute("show databases")

for x in mycursor:
    print(x)


#连接数据库
mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "123456",
    database= "python_connect"
)