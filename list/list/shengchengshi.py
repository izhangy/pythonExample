# -*- coding: UTF-8 -*-
"""
@File: shengchengshi.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 10:46
"""
squares = [value**3 for value in range(1,11)]
print(squares)

#切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])#从第0个元素开始，到第二个元素结束，跟range一样，都是做开右闭区间
print(players[-3:])#输出最后三个，从后往前数三个

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]#复制列表
print(friend_foods)