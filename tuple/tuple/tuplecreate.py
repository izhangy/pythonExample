# -*- coding: UTF-8 -*-

"""
@File: tuplecreate.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 9:00
"""
#元组创建的两种方式
#1.直接用小括号
t = ('python', 'hello', 'world', 98)
print(t)
print(type(t))

#2.使用内置函数tuple()
t1 = tuple(('python', 'hello', 90))
print(t1)
#注意：只包含一个元素的元组，要使用','和’小括号
t = (10, )
print(t)
t=(10,[20,30],10)
print(t)
t=(10,{20:30},(10,[20,30],10),30)
print(t, t[1])
print(t,t[2])