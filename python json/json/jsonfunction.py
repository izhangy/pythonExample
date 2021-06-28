# -*- coding: UTF-8 -*-

"""
@File: jsonfunction.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 10:27
"""

"""
json.dumps:将Python对象编码成JSON字符串
json.loads：将已编码的JSON字符串解码为Python对象
"""
"""
json.dumps：语法格式

json.dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, 
cls=None, indent=None, separators=None, encoding="utf-8", default=None, sort_keys=False, **kw)
"""
import json

data = [{'a':1, 'b':2, 'c':3}]
data2 = json.dumps(data)
print(data)
print(data2)

data3 = json.dumps({'a':'Run', 'b':7}, sort_keys=True, indent=4, separators=(',',':'))
print(data3)

"""
json.loads
json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
语法
json.loads(s[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
"""
