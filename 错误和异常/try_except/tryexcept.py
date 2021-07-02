# -*- coding: UTF-8 -*-
"""
@File: tryexcept.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 15:00
"""

#异常语句：try/except语句
"""
try:
    执行代码
except:
    发生异常时执行的代码
"""
# while True:
#     try:
#         x = int(input("输入一个数字: "))
#         break
#     except ValueError:
#         print("请输入整数数字")

#一个try语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行
#一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组：例如：except(RuntimeError, TypeError, NameError): pass
#最后一个except子句可以忽略异常的名称，它将被当作通配符使用。可以打印一个错误信息，然后再次把异常抛出
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    #rstrip()去除结尾的空白，lstrip去除开头的空白，strip去除两端的空白
    i = int(s.rstrip())#用于溢出字符串头尾指定的字符或字符序列，只能删除开头或结尾的字符
    with open("myfile.txt") as f:
        for item in f:
            print(item)
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error", sys.exc_info()[0])
    raise
else:
    with open("myfile.txt") as f:
        for item in f:
            print(item)
with open("myfile.txt") as f:
    for item in f:
        print(item)