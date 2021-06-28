# -*- coding: UTF-8 -*-

"""
@File: guanxi.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 9:56
"""
s1 = {10, 20, 30, 40, 80}
s2 = {20, 30, 10, 40, 80}
print(s1 == s2)
print(s1 != s2)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3}
s3 = {4,5,6}
print(s2.issubset(s1))#s2是否是s1的子集
print(s3.issubset(s1))

print(s1.issuperset(s2))#s1是否是s2的超集
print(s1.issuperset(s3))

print(s1.isdisjoint(s3))#判断s1，与s3是否有交集
print(s2.isdisjoint(s3))
#交集：intersection
print(s1.intersection(s2))
#并集：union   |
print(s1.union(s2))
print(s1 | s2)

#差集：difference   -
print(s1.difference(s2))
print(s1 - s2)

#对称差集：symmetric_difference   ^
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# 集合生成式
s={i*i for i in range(10)}
print(s)