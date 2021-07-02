# -*- coding: UTF-8 -*-
"""
@File: urlrequest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 16:42
"""
import urllib
from urllib import  request
from urllib import error
"""
urllib.request定义了一些打开URL的函数和类，包含授权验证、重定向、浏览器cookies等
urllib.request可以模拟浏览器的一个请求发起过程
可以使用urllib.request的urlopen方法来打开一个URL，语法如下：
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context-None)

url:	url地址

data:	发送到服务器的其他数据对象，默认为None

timeout：设置访问超时时间

cafile和capath：cafile为CA证书，capath为CA证书的路径，使用HTTPS需要用到

~~cadefault：~~弃用

context：ssl.SSLContext类型，用来指定SSL设置
"""
from urllib.request import urlopen
myUrl = urlopen("https://www.baidu.com")
# print(myUrl.read())#读取页面全部内容
# print(myUrl.read(30))#读取一定内容
# print(myUrl.readline())#读取一行内容
lines = myUrl.readlines()#读取文件的全部内容，他会把读取的内容赋值给一个列表变量
for line in lines:
    print(line)

#getcode()函数获取页面状态码
myUrl1 = urllib.request.urlopen("https://www.baidu.com")
print(myUrl1.getcode())
try:
    myUrl2 = urllib.request.urlopen("https://www.runoob.com/no.html")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(404)