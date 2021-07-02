# -*- coding: UTF-8 -*-
"""
@File: select.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:14
"""

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd = "123456",
    database= "python_connect",
    auth_plugin = 'mysql_native_password'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

myresult = mycursor.fetchone()#返回数据的第一行
print(myresult)