# -*- coding: UTF-8 -*-

"""
@File: object.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 15:02
"""
#Python中一切皆对象
#创建类的语法
class Student:   #对象命名规范：首字符大写，其余小写
    native_place = '吉林'  #类属性，直接写在类里的变量，成为类属性
    def __init__(self, name, age):  #name, age为实例属性，初始化方法
        self.name = name
        self.age = age


    #实例方法
    def info(self):
        print('我的名字叫', self.name, '年龄是',self.age)

    #定义在类之外的，称为函数。定义在类之内的称为方法
    def eat(self):
        print('学生',self.name, "在吃饭.......")

    # 类方法
    #类的组成：类属性、实例方法、静态方法、类方法
    @classmethod
    def cm(cls):
        print('类方法，使用classmethod方法修饰。称为类方法')
    #静态方法
    @staticmethod
    def sm():
        print('使用了staticmethod修饰，称为静态方法。静态方法中不允许写self')
#类属性的使用方式
print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('lisi', 30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='天津'
print(stu2.native_place)
Student.cm()
Student.sm()
Student.eat(stu1)