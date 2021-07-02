# -*- coding: UTF-8 -*-
"""
@File: datetimetest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/1 15:41
"""
import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime(2020, 5, 17)
print(x)

try:
    x = datetime.datetime(2018, 11, 1)
    print(x.strftime("%B"))
except:
    print("日期有误")
else:
    print(x)