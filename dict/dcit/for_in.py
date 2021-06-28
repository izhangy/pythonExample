# -*- coding: UTF-8 -*-

"""
@File: for_in.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 20:14
"""
scores={'zhangsan':100, 'lihua':21, 'lisi':3, 1:1}
#item只会输出键
for item in scores:
    print(item, scores.get(item))