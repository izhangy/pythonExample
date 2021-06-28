# -*- coding: UTF-8 -*-

"""
@File: test.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 9:56
"""
import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
while True:
    c, addr = s.accept()  # 建立客户端连接
    print( '连接地址：', addr)
    str='欢迎访问菜鸟教程！'
    c.send(str.encode())

    c.close()  # 关闭连接