# -*- coding: UTF-8 -*-
"""
@File: city.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 16:28
"""
prompt = "\nplease enter the name of city"
prompt +="\n enter 'quit' when you are finished."

active = True
while active:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("i'd love to go to" ,  city.title() , "!")

#continue
