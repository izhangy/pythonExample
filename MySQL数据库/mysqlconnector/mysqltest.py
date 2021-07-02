# -*- coding: UTF-8 -*-
"""
@File: test.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 11:19
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "123456",
    auth_plugin = 'mysql_native_password'
)
print(mydb)