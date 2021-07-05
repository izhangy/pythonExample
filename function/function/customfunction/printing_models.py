# -*- coding: UTF-8 -*-
"""
@File: printing_models.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 17:41
"""
#在函数中修改列表
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("printing current_designs list:" + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\n The following models have benn printed")
    for completed_model in completed_models:
        print(completed_model)


unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_design[:], completed_models)

show_completed_models(completed_models)

