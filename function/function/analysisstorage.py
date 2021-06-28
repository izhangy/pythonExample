# -*- coding: UTF-8 -*-

"""
@File: analysisstorage.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 11:23
"""
def fun(arg1, arg2):
    print('arg1=', arg1)
    print('arg2=', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1=', arg1)
    print('arg2=', arg2)

 #程序从这开始运行
n1 = 11
n2 = [22, 34, 22]
print(n1)
print(n2)
print('------调用函数后---------')
fun(n1, n2)
print('调用函数后n1的值', n1)
print('调用函数后n2的值',n2)

