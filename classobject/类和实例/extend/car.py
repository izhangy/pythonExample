# -*- coding: UTF-8 -*-
"""
@File: car.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/5 9:16
"""

"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4l', 2016)
print(my_new_car.get_descriptive_name())
"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.make
        return long_name

    #获取汽车里程
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
# my_new_car = Car('audi', 'a4l', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23#修改属性的值
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()



