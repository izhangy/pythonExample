# -*- coding: UTF-8 -*-

"""
@File: zuoyongyu.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 14:52
"""

name='zhang'
print(name)
def fun2():
    print(name)
fun2()

def fun3():
    global age  #局部变量变为全局变量，加global
    age = 20
    print(age)
fun3()
print(age)
