# -*- coding: UTF-8 -*-

"""
@File: pratice.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/28 9:55
"""
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)