# -*- coding: UTF-8 -*-

"""
@File: Employee.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 16:43
"""

"""
使用class语句创建一个新类，class之后为类的名称，并以冒号结尾
class   className:
        '类的帮助信息'       #类文档字符串
        class_suite             #实体。由成员、方法、数据属性组成
"""
#实例
class Employee:
    '所有员工的基类'
    empCount=0

#empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或者外部类使用Employee.empCount访问
#第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或者初始化方法，当创建了这个类的实例时就会调用该方法
#self代表类的实例，self在定义类的方法时是必须有的，在调用时不必传入相应的参数
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)

#创建实例对象
#Python语言实例化对象中没有new，类的实例化类似函数的调用方式
"创建Employee类的对象"
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 50000)

#访问属性
#可以使用 . 来访问对象的属性。
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

#添加属性
emp1.age = 7
#修改属性，只需再次调用
emp1.age = 8

"""
使用以下函数访问属性：
    -getattr(obj, name[,default]):访问对象的属性
    -hasattr(obj, name):检查是否存在一个属性
    -setattr(obj, name, value):设置一个属性。如果属性不存在会创建
    -delattr(obj,name):删除属性
"""
hasattr(emp1,'age')#如果age存在，返回true
getattr(emp1,'age')#获取age的属性值
setattr(emp1,'age',8)#添加属性age

"""
python内置类属性
__dict__:类的属性(包含一个字典，由类的数据属性组成)
__doc__:类的文档字符串
__name__:类名
__module__:类定义所在的模块(类的全名是'__main__.className', 如果类位于一个导入模块mymod中，那么className.__module__等于mymod)
__bases__:类的所有父类构成元素(包含了一个由所有父类组成的元组)
"""
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)