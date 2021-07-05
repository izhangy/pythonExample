# -*- coding: UTF-8 -*-
"""
@File: dictlist.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 15:04
"""
#在字典中存储列表
pizza = {
    'crust' : 'thick',
    'toppings':['mushrooms', 'extra cheese']
}
for topping in pizza['toppings']:
    print("\t", topping)

favorite_languages = {
    'jen': ['python'],
    'sarah': ['c'],
    'edward': ['ruby','c', 'java'],
    'phil': ['python', 'c', 'java']
}
for name, languages in favorite_languages.items():
    print(name.title())
    for language in languages:
        print(language.title())