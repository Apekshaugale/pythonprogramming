inheritance Practice Questions
1. Single-Level Inheritance

Q1. Vehicle → Car
Create a class Vehicle with attributes brand and speed, and a method vehicle_info().
Create a child class Car that inherits from Vehicle. Add the attribute fuel_type
and create a method car_info() to display all details.

class Vehical:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def  vehicle_info(self):
        print(f'The Vehical brand is {self.brand} and speed is {self.speed}')
        
class Car(Vehical):
    def __init__(self,brand,speed,fuel_type):
        super().__init__(brand,speed)
        self.fuel_type=fuel_type
        
    def car_info(self):
         super().vehicle_info()
         print(f'The Vehical fuel type  is {self.fuel_type} ')
c=Car("mahindra",500,'CNG')
c.car_info()

o/p:
The Vehical brand is mahindra and speed is 500
The Vehical fuel type  is CNG 

