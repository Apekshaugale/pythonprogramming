1. Single Level Inheritance   
Create a class Vehicle with a method start(). Override this method in
the child class Bike.
Demonstrate single-level inheritance.

class Vehicle:
    def start(self):
        print('Parent class ')
class Bike(Vehicle):
    def start(self):
        super().start()#super function
        print('Child class')
b=Bike()
b.start()

class Vehicle:
    def start(self):
        print('Parent class ')
class Bike(Vehicle):
    def start(self):
        Vehicle.start(self)#class name
        print('Child class')
b=Bike()
b.start()
