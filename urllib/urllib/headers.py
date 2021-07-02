# -*- coding: UTF-8 -*-
"""
@File: headers.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 17:12
"""
#模拟头部信息
#urllib.request.Request
"""
语法：
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
url:    url地址
data:   发送到服务器的其他数据对象，默认为None
headers：HTTP请求的头部信息，字典格式
origin_req_host：请求的主机地址，ip或域名
unverifiable：很少用整个参数，用于设置网页是否需要验证，默认为False
method：请求方法：GET、POST、DELETE、PUT等
"""
import urllib.request
import urllib.parse

url = "https://weibo.com/?s=" #搜索页面
keyword = '河南大学'
key_code = urllib.request.quote(keyword) #对请求进行编码
url_all = url+key_code
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'} #头部信息
request = urllib.request.Request(url_all, headers=header)
response = urllib.request.urlopen(request).read()

fh = open("./urllib_test_weibo.html", "wb")#将文件写入到当前目录中
fh.write(response)
fh.close()
