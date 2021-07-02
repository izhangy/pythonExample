# -*- coding: UTF-8 -*-
"""
@File: tryexceptelse.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 15:17
"""
#try/except....else
#else子句在try子句没有发生任何异常的时候执行
#有无异常总会执行try中的语句
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


