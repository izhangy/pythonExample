# -*- coding: UTF-8 -*-
"""
@File: pets.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/2 16:56
"""
#传递实参,位置实参
def describe_pet(animal_type, pet_name):
    print("\n I have a ", animal_type, ".")
    print("my", animal_type, "'s name is "+ pet_name.title() + ".")
describe_pet('hamster', 'harry')
#调用函数多次
describe_pet('dog', 'willie')