# -*- coding: UTF-8 -*-

"""
@File: selftest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 16:56
"""
#self代表类的实例，而非类
#类的方法与普通函数只有一个特别的区别：他们必须有一个二外的第一个参数名称self
class selftest:
    def prt(self):
        print(self)
        print(self.__class__)
t = selftest()
t.prt()