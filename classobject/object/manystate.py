# -*- coding: UTF-8 -*-

"""
@File: manystate.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 16:42
"""
class Animal(object):
    def eat(self):
        print("动物会吃")
class Dog(Animal):
    def eat(self):
        print("狗吃骨头")
class Cat(Animal):
    def eat(self):
        print("猫吃鱼")

class Person:
    def eat(self):
        print("重新定义一个类，并具有相同的属性")
#定义一个函数
def fun(obj):
    obj.eat()


if __name__ =='__main__':
    # 调用函数
    fun(Cat())
    fun(Dog())
    fun(Animal())
    # Person不具备继承，但具备eat方法，仍可以调用。不关心对象，只关心行为
    fun(Person())