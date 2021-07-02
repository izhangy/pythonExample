# -*- coding: UTF-8 -*-

"""
@File: viewdict.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 20:06
"""
scores={'zhangsan':"100", 'lihua':21, 'lisi':3}
#获取所有的key，生成一个列表，可以将所有的key存入一个列表中
keys=scores.keys()
print(keys)
print(list(keys))
#获取所有的value
values=scores.values()
print(values)
#获取字典的键值对
item= scores.items()
print(item)
print(list(item))#列表元素由元组组成的

