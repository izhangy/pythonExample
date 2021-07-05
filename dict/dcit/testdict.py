# -*- coding: UTF-8 -*-
"""
@File: testdict.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 14:12
"""
alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x-position: " + str(alien_0['x_position']))

#向右移动
if alien_0['speed'] == 'slow':
    x_increment =1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x-position: "+str(alien_0['x_position']))

#类似对象的键值对
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("Sarah's favorite language is " + favorite_languages.get('sarah').title() +".")