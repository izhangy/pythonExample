# -*- coding: UTF-8 -*-

"""
@File: manynum.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 14:09
"""
#函数返回多个值时，结果为元组
def fun(num):
    odd = [] #定义两个列表，odd存入偶数，even存入奇数
    even = []
    for i in num:
        if i%2:#0是false，其他为true
            odd.append(i)
        else:
            even.append(i)
    return odd, even

lst = [10, 30, 12, 32, 23, 31, 28,89]
print(fun(lst))

#函数如果没有返回值，可以没有return
#函数的返回值，如果是1个，直接返回类型
#函数的返回值，如果是多个返回的结果为元组