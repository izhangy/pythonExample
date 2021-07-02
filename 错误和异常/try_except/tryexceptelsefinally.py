# -*- coding: UTF-8 -*-
"""
@File: tryexceptelsefinally.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 15:24
"""
"""
try-finally语句：try-finally语句无论是否发生异常都将执行最后的代码

try:

except:

else:

finally:    
"""
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")