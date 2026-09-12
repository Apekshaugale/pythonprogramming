#-------------------------Assignment Questions----------------------------------
'''
1.Create a class Employee with attributes name and salary.
Create a child class Manager that prints both values.
'''
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
'''2.Create a class Bank with attribute balance.
 Create a child class SavingsAccount with methods:
deposit()
withdraw() 


3.Create a class Person with a constructor.
Create a child class Student and use super() to initialize parent data.



4.Create a class Vehicle with method start().
Override this method in child class Bike.

'''

