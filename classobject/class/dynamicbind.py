# -*- coding: UTF-8 -*-

"""
@File: dynamicbind.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 16:16
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + "在吃")
stu1 = Student('zhangsan', 20)
stu2 = Student('lisi', 30)

#动态绑定方法
stu1.eat()
stu2.eat()
#为stu1单独绑定一个show方法
def show():
    print('定义在类之外的，称为函数')
stu1.show = show()
stu1.show