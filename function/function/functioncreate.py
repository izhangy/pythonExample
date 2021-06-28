# -*- coding: UTF-8 -*-

"""
@File: functioncreate.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 11:01
"""
#函数的创建
"""
函数是执行特定任何以完成特定功能的一段代码
def 函数名([输入函数]):
        函数体
        [return xxx]
"""
def calc(a, b):     #a, b    形参
    c=a+b
    return  c
result = calc(10, 20)  #实参，按位置顺序传参
print(result)

res=calc(b=10, a=20) #按关键字进行传参
print(res)