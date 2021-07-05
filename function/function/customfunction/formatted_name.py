# -*- coding: UTF-8 -*-
"""
@File: formatted_name.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 17:19
"""
"""
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
"""
#可选的实参
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name+' ' + middle_name+ ' ' +last_name
    else:
        full_name = first_name +' ' + last_name
    return full_name.title()
musician =get_formatted_name('jimi', 'hendrix')
print(musician)
musician=get_formatted_name('jimi', 'hooker', 'lee')
print(musician)