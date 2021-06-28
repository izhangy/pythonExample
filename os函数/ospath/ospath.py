# -*- coding: UTF-8 -*-

"""
@File: ospath.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/28 9:32
"""
import os.path
#abspath(path)输出文件的绝对路径
print(os.path.abspath('ospath.py'))#輸出絕對路徑
#exists(path),判断文件是否存在
print(os.path.exists('ospath.py'))
# join(path,name)将目录与目录或者文件名拼接起来
# print(os.path.join('E:\\工作日志\\5.融合中控', 'ospath.py'))
#splitext()分离文件和扩展名
print(os.path.splitext('ospath.py'))
#split()拆分文件路径
print(os.path.split('E:\\工作日志\\5.融合中控\\ospath.py'))
#basename(path) 从一个目录中提取文件名
print(os.path.basename('E:\\工作日志\\5.融合中控\\ospath.py'))
#dirname(path)  从一个路径中提取文件路径，不包括文件名
print(os.path.dirname('E:\\工作日志\\5.融合中控\\ospath.py'))
#isdir(path)用于判断是否为路径
print(os.path.isdir('E:\\工作日志\\5.融合中控\\ospath.py'))
