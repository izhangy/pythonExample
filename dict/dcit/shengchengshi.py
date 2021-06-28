# -*- coding: UTF-8 -*-

"""
@File: shengchengshi.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 20:25
"""
#zip中存在可迭代的对象
items = ['Fruits', 'Books', 'Others']
prices = [91, 92, 93]
d = {item.upper():price for item, price in zip(items, prices)}
print(d)

name='zhangsan'

age=20

print("我是%s，今年%d岁" % (name, age))

#{}

print('我是{0}, 今年{1}岁'.format(name,age))

#f-string

print(f'我是{name},今年{age}岁')