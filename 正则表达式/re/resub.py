# -*- coding: UTF-8 -*-

"""
@File: resub.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/22 23:42
"""
"""
检索和替换
re.sub(pattern,rep1,string,count=0,flags=0)
pattern：正则中的模式字符串
rep1：替换的字符串，也可以是一个函数
string：要被查找替换的原始字符串
count：模式匹配后替换的最大次数，默认为0，替换全部
"""
import re
phone = "2004-959-559 # 这是一个国外手机号"
#删除字符串中的注释
num = re.sub(r'#.*$', "", phone)
print("手机号是：", num)

#删除非数字（-）的字符串
#\D匹配一个非数字字符
num = re.sub(r'\D', "", phone)
print("手机号码是：" + num)

#rep1是一个函数
def double(matched):
    value = int(matched.group('value'))
    return str(value*2)

#\d匹配一个数字字符
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
