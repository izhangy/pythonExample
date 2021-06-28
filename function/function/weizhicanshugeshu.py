# -*- coding: UTF-8 -*-

"""
@File: weizhicanshugeshu.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 14:30
"""
#可变的位置参数，输出一个元组
def fun(*args):
    print(args)
fun(10)
fun(10, 30)
fun(10,20,30,40)

#可变的关键字形参，输出一个字典
def fun1(**args):
    print(args)

fun1(a=1)
fun1(a=1, b=2, c=3)

def fun2(*args, **arg):
    pass
#在一个函数的定义过程中，既有关键字形参，也有个数可变的位置形参。要求个数可变字形参放在关键字可变的位置之前
