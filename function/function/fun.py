# -*- coding: UTF-8 -*-

"""
@File: fun.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/24 14:39
"""
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

#函数调用
print(fun(10,20,30))#位置传参
lst=[111,222,333]
fun(*lst)#当传递列表时，加一个*

fun(a=100, b=200, c=300)#函数的调用，所以是关键字传参
dic={'a':100,'b':111,'c':333}
fun(**dic)#将字典中的键值对都转换为关键字，使用**

def fun4(a,b,*,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
#调用fun4函数
#fun4(10,20,30,40)  #位置实参传递
fun4(a=10, b=20, c=30, d=40) #关键字实参传递
fun4(10, 20, c=30, d=40) #前两个参数采用位置实参传递，*之后采用关键字实参传递