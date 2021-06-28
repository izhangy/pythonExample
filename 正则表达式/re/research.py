# -*- coding: UTF-8 -*-

"""
@File: research.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 23:02
"""
"""
扫描整个字符串并返回第一个成功的匹配
re.search(pattern,string,flag=0)

re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
而re.search匹配整个字符串，直到找到一个匹配。
"""
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print
    "match --> matchObj.group() : ", matchObj.group()
else:
    print
    "No match!!"

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print
    "search --> searchObj.group() : ", matchObj.group()
else:
    print
    "No match!!"