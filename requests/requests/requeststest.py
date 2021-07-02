# -*- coding: UTF-8 -*-
"""
@File: requeststest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/30 17:46
"""
import requests
r = requests.get('https://www.baidu.com')
print(r.status_code)#返回请求状态码
print(r.text)
with open("text.txt", "w", encoding="utf-8") as f:
    f.write(r.text)


