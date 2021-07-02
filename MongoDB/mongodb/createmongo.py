# -*- coding: UTF-8 -*-
"""
@File: createmongo.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 16:45
"""
import pymongo

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["mydatabase"]
# print(myclient.list_database_names())

#检查数据库db是否存在
# dblist = myclient.list_database_names()
# if 'mydatabase' in dblist:
#     print("the mydatabase exists")

# mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"name": "John", "address":"Highway 37"}
x = mycol.insert_one(mydict)