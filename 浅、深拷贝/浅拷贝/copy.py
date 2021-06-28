# -*- coding: UTF-8 -*-

"""
@File: copy.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/28 8:49
"""
class CPU:
    pass

class Disk:
    pass

class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk

#（1）变量赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)#发现内存地址是一样的

#浅拷贝：Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝。
#因此，源对象与拷贝对象会引用同一个子对象

#(2)浅拷贝
disk = Disk()#创建一个disk对象
computer = Computer(cpu1, disk) #创建一个计算机类的对象
#浅拷贝
import copy
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

