# -*- coding: UTF-8 -*-
"""
@File: createtable.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 12:11
"""

import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    passwd= "123456",
    database= "python_connect"
)
# mycursor = mydb.cursor()
# mycursor.execute("create table customes(name varchar(255), address varchar(255))")

# #设置主键
# mycursor = mydb.cursor()
# mycursor.execute("create table customers (id int auto_increment primary key, name varchar(255), address varchar(255))")

#在现有表上增加主键
# mycursor = mydb.cursor()
# mycursor.execute("alter table customes add column id int auto_increment primary key")


mycursor = mydb.cursor()
mycursor.execute("create table products (id int auto_increment primary key, name varchar(255))")