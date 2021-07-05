# -*- coding: UTF-8 -*-
"""
@File: dictdict.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 15:22
"""
#在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    }
}
for username, user_info in users.items():
    print("username: ", username)
    print("user_info: ", user_info)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("full name: ", full_name.title())
    print("location: ", location.title())

