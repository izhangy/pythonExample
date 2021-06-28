# -*- coding: UTF-8 -*-

"""
@File: parameterdefine.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 14:17
"""
#函数定义时，给形参设置默认值，只有与默认值不符合的时候才需要传递
def fun(a, b=10):
    print(a, b)

#函数调用
fun(100)#b会输出默认值10；100赋值给a
fun(20, 30)