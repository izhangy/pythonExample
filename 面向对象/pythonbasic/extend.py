# -*- coding: UTF-8 -*-

"""
@File: extend.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 17:21
"""
"""
类的继承
语法
class   派生类名(基类名)
    ...
"""

"""    
python中继承的特点：
    -如果在子类中需要父类的构造方法就需要显式的调用父类的构造方法，或者不重写父类的构造方法。
    -在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于类中调用普通函数时并不需要带上self参数
    -python总是首先查找对应类型的方法，如果不能在派生类中找到对应的方法，它才开始到基类中逐个查找
"""
"""
如果在继承元组中列一个以上的类，那么它就被称为”多重继承“
class SubClassName(ParentClass1[,ParentClass2,...]):
    ...
"""

class Parent:
    parentAttr = 100
    def __init__(self):
        print("调用父类构造函数")

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("父类属性", Parent.parentAttr)

class Children(Parent): #定义子类
    def __init__(self):
        print("调用子类构造方法")

    def childMethod(self):
        print("调用子类方法")

c = Children()  #实例化子类
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

"""
还可以继承多个类
class A:
    ...
class B:
    ...
class C(A,B):#继承A，B
    ...
"""

#方法重写，如果父类方法的功能无法满足需求，可以在子类