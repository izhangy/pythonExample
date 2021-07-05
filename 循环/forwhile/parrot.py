# -*- coding: UTF-8 -*-
"""
@File: parrot.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 16:04
"""
prompt = "\n Tell me something, and I will repeat it back to you"
prompt += "\n Enter 'quit' to end the program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)