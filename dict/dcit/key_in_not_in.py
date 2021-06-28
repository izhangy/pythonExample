# -*- coding: UTF-8 -*-

"""
@File: key_in_not_in.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 19:53
"""
#判断key是否存在，in   not in
scores={'zhangsan':100, 'lisi':200, 'wangwu':120}
print('zhangsan' in scores)#判断键zhangsan是否存在
print('zhangsan' not in scores)
scores['lihua']=89#新增一个键值lihua：89
print(scores)
scores['lihua']=90#修改键lihua的值
print(scores)
