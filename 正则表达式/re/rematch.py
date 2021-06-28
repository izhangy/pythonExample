# -*- coding: UTF-8 -*-

"""
@File: rematch.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 22:52
"""
import re

"""
re.match(pattern,string,flags=0)
pattern:匹配的正则表达式
string:匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式。
group(num=0)匹配整个表达式的字符串
groups()返回一个包含所有小组字符串的元组，从1到所含的小组号
"""
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("not match")