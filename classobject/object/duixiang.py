# -*- coding: UTF-8 -*-

"""
@File: duixiang.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 16:33
"""
from classobject.object.manystate import  Person
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age = age

    def __str__(self):
        return "my name is {0}, {1} years".format(self.name, self.age)
#object类是所有类的父类，因此所有类都有object类的属性和方法
#内置函数dir()可以查看指定对象所有属性
#__str__()方法用于返回一个对于“对象的描述”
stu = Student("张三", 20)
Person.eat(stu)
print(dir(stu))
print(stu)#默认调用__str__()方法
