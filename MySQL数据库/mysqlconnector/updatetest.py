# -*- coding: UTF-8 -*-
"""
@File: updatetest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:48
"""
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="python_connect"
)
mycursor = mydb.cursor()
sql = "update customers set address = %s where id = %s"
val = ("Valley 345", "6")
mycursor.execute(sql, val)
mydb.commit()