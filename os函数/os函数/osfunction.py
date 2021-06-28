# -*- coding: UTF-8 -*-

"""
@File: osfunction.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/28 9:15
"""
#os模块与系统文件相关的模块
import os
# os.system('notepad.exe')#打开记事本
# os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQScLauncher.exe')#打开QQ软件
#getcwd()打开当前的工作目录
print(os.getcwd())

#listidr显示所有目录
lst=os.listdir('../os函数')
print(lst)
#mkdir创建一个文件目录
# os.mkdir('mkdir')
#创建多级目录
# os.makedirs('a/b/c')
#rmdir删除目录
# os.rmdir('mkdir')
#removedirs删除多级目录
# os.removedirs('a/b/c')
#chdir设置目录为工作目录
os.chdir('C:\\Users\\darly\\PycharmProjects\\pythonExample\\os函数')
print(os.getcwd())