# -*- coding: UTF-8 -*-

"""
@File: quzhi.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 19:48
"""
scores = {'zhangsan':100, 'lisi':90, 'lihua':112}
#取值方式，使用[]
print(scores['zhangsan'])
#第二种方式，使用get()方法
print(scores.get('zhangsan', 'lisi'))
print(scores.get("bucunzai"))
