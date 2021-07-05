# -*- coding: UTF-8 -*-
"""
@File: person.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 17:28
"""
#返回字典
"""def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)"""
def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)