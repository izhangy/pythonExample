# -*- coding: UTF-8 -*-

"""
@File: __add__.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 17:09
"""
class Student:
    def __init__(self, name):
        self.name = name
    def __add__(self, other):#若想让两个对象相加，必须定义次方法
        return self.name + other.name

stu1 = Student('zhang')
stu2 = Student('li')
s = stu1 + stu2  #实现两个对象的加法运算
print(s)
