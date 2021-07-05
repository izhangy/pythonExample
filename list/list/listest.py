# -*- coding: UTF-8 -*-
"""
@File: listest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 10:19
"""
motorcycles = ['honda', 'yamaha', 'ducati', 'suzuki']
poped_motorcycle = motorcycles.pop()#pop弹出栈顶元素
print(motorcycles)
print(poped_motorcycle)

last_owned = motorcycles.pop(0)#弹出指定位置的元素
print(last_owned)
motorcycles.remove('ducati')#删除表中确定的元素
print(motorcycles)
#排序：sort，sorted
motorcycles.sort(reverse=True)
print(motorcycles)
sorted(motorcycles).reverse()
print(motorcycles)