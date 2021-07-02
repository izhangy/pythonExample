# -*- coding: UTF-8 -*-
"""
@File: test.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 17:30
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
