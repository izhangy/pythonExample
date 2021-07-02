# -*- coding: UTF-8 -*-
"""
@File: insert.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 14:04
"""

import mysql.connector
mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    passwd= '123456',
    database= 'python_connect'
)
mycursor = mydb.cursor()

# sql = 'INSERT INTO customers (name, address) values (%s, %s)'
# # val = ("John", "wall street 32")#插入一行
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652')
# ]#插入多行
# # mycursor.execute(sql, val)#插入一行
# mycursor.executemany(sql, val)#插入多行
# mydb.commit()#提交

# print(mycursor.rowcount, "record inserted")#记录插入多少行数据
# print("1 record inserted, ID:", mycursor.lastrowid)#返回插入数据的最后一行的id

sql = 'INSERT INTO products (id,name) values (%s, %s)'
# val = ("John", "wall street 32")#插入一行
val = [
    ('154','Chocolate Heaven'),
    ('155','Tasty Lemons'),
    ('156','Vanilla Dreams')
]#插入多行
# mycursor.execute(sql, val)#插入一行
mycursor.executemany(sql, val)#插入多行
mydb.commit()#提交