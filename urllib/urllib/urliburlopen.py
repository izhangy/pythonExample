# -*- coding: UTF-8 -*-
"""
@File: urliburlopen.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 17:07
"""
#write()抓取网页到本地
from urllib.request import urlopen
import urllib
from urllib import  request
myUrl  = urlopen("https://www.baidu.com")
f = open("baidu_test.html", "wb")
content = myUrl.read()
f.write(content)
f.close()

#编码与解码
#urllib.request.quote()编码
#urllib.request.unquote()解码
encode_url = urllib.request.quote("http://www.runoob.com")#编码
print(encode_url)
unencode_rul = urllib.request.unquote(encode_url)#解码
print(unencode_rul)