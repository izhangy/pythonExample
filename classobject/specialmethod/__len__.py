# -*- coding: UTF-8 -*-

"""
@File: __len__.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 17:15
"""

class Student:
    def __init__(self, name):
        self.name = name
    def __len__(self):#定义类的长度
        return len(self.name)
#输出对象的长度
lst = [11,22,33,44]
print(len(lst))
print(lst.__len__())
stu1 = Student('jackd')
print(len(stu1))