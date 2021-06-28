# -*- coding: UTF-8 -*-

"""
@File: __dict__.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 16:58
"""
class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
class D(A):
    pass
#创建C类的对象
x = C('JCK', 20)  #x是C类的一个实例对象
print(x.__dict__)#实例对象是一个字典
print(C.__dict__)
print(x.__class__)#输出对象所属的类
print(C.__bases__)#C类的父类类型的元素
print(C.__mro__)#类的层次结构
print(A.__subclasses__())#子类的列表