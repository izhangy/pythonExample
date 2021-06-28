# -*- coding: UTF-8 -*-

"""
@File: init_new.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 17:22
"""
#119课，有时间再听一遍
class Person(object):
    #新建一个对象
    def __new__(cls, *args, **kwargs):
        print("__new__被调用执行， cls的id为{0}".format(id(cls)))
        obj = super().__new__(cls)
        print("创建对象的id为{0}".format(id(obj)))
        return obj

#初始化对象
    def __init__(self, name, age):
        print('__init__被调用了，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age

print("object这个类对象的id为：{0}".format(id(object)))
print("Person这个类的对象为id：{0}".format(id(Person)))

#创建Person类的实例对象
p1 = Person('zhangsan', 20)
print("p1这个Person类的实例对象的id；{0}".format(id(p1)))
