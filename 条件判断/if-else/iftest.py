# -*- coding: UTF-8 -*-
"""
@File: iftest.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 11:11
"""
available_topping = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
add_list = []
for requested_topping in requested_toppings:
    if requested_topping in available_topping:
        add_list.append(requested_topping)
        print("Adding "  + requested_topping + ".")
    else:
        print("sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
print(requested_toppings)
print(add_list)