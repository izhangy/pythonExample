# -*- coding: UTF-8 -*-

"""
@File: JustCounter.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 17:54
"""

"""
类属性与方法
类的私有属性：
__private_attrs:不能在类的外部被使用，或直接访问。在类内部的方法中使用时：self.__private_attrs

类的方法：
在类的内部，使用def关键字可以定义为一个方法，与一般函数定义不同，类方法必须包含参数self且为第一个参数
类的私有方法
__private_method:两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用self.__private_method
"""

class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount +=1
        self.publicCount += 1
        print(self.__secretCount)
counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)#实例不能访问私有变量
#若要访问私有类，可以使用object._className__attrName(对象名._类名__私有属性名)访问属性
justCounter = JustCounter()
print(justCounter._JustCounter__secretCount)

"""
#单下划线、双下划线、头尾双下划线说明
_foo:以单划线开头，表示protected类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于from module import *
__foo__:定义的是特殊方法，一般是系统定义名字，类似__init__()
__foo:双下划线的表示的是私有类的变量，只能允许这个类本身进行访问
"""
