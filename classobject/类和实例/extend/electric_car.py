# -*- coding: UTF-8 -*-
"""
@File: electric_car.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/7/5 23:38
"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descritive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("this car has " +  str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        #初始化父类属性
        super().__init__(make, model, year)#super 帮助Python将父类和子类关联起来

my_tesla = ElectricCar('tesla', 'model Y', 2020)
print(my_tesla.get_descritive_name())
