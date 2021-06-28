# -*- coding: UTF-8 -*-

"""
@File: in.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 9:43
"""
s = {10, 20, 30, 40}
print(10 in s)
print(80 not in s)

#集合新增元素,一次添加一个元素
s.add(80)
print(s)
s.update({200, 300, 400})#一次添加多个元素
print(s)
"""
删除元素
"""
s.remove(200)#不存在抛异常
print(s)
s.discard(100)#不存在不抛异常
print(s)
s.pop()#一次删除任意元素
print(s)

