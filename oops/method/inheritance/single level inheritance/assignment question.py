#-------------------------Assignment Questions----------------------------------
'''
1.Create a class Employee with attributes name and salary.
Create a child class Manager that prints both values.

class Employee:
    def Name(self):
         self.name='Sneha'
         self.salary=45000
class Manager(Employee):
    def Info(self):
        
        print(self.name)
        print(self.salary)
m=Manager()
m.Name()
m.Info()

class Employee:
    def Name(self):
         self.name='Sneha'
         self.salary=45000
class Manager(Employee):
    def Info(self):
        super().Name()
        print(self.name)
        print(self.salary)
m=Manager()
m.Info()

class Employee:
    def Name(self):
         self.name='Sneha'
         self.salary=45000
class Manager(Employee):
    def __init__(self):
        super().Name()
        print(self.name)
        print(self.salary)
m=Manager()

class Employee:
    def __init__(self):
         self.name='Sneha'
         self.salary=45000
class Manager(Employee):
    def __init__(self):
        super().__init__()
        print(self.name)
        print(self.salary)
m=Manager()



class Employee:
    def __init__(self):
         self.name='Sneha'
         self.salary=45000
class Manager(Employee):
    def __init__(self):
        Employee.__init__(self)
        print(self.name)
        print(self.salary)
m=Manager()



3.Create a class Person with a constructor.
Create a child class Student and use super() to initialize parent data.

class Person:
    def __init__(self):
        print('Constructor class1')
class Student(Person):
    def __init__(self):
        super().__init__()
        print('Constructor class 2')
s=Student()

o/p:
Constructor class1
Constructor class 2


4.Create a class Vehicle with method start().
Override this method in child class Bike.

'''
class Vehicle:
    def start(self):
        print('Bike')
class Bike(Vehicle):
    def start(self):
        
        print('Honda')
b=Bike()
b.start()

class Vehicle:
    def start(self):
        print('Bike')
class Bike(Vehicle):
    def start(self):
        super().start()
        print('Honda')
b=Bike()

b.start()
