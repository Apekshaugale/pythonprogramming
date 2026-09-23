'''Inheritance Practice Questions
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


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q2. Animal → Dog
Create a class Animal with a method sound() that prints "Animal makes a sound".
Create a child class Dog that overrides the sound() method and prints "Dog barks".
Demonstrate method overriding.

class Animal:
    
    def sound(self) :
        print( "Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
d=Dog()
d.sound()

o/p:
Animal makes a sound
Dog barks


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Multilevel Inheritance

Q3. Student → CollegeStudent → EngineeringStudent
Create a class Student with name and age. Create a class CollegeStudent
that inherits from Student and adds college_name and percentage.
Create a class EngineeringStudent that inherits from CollegeStudent
and adds branch and cgpa. Use super() to initialize the attributes and display all details.

class Student:
    def student(self,name,age):
          self.name=name
          self.age=age
    def info(self):
        print(f'The name of student is {self.name} and age is {self.age}')
class CollegeStudent(Student):
    def cstudent(self,name,age,cname,percentage):
       super().student(name,age)
       self.cname=cname
       self.percentage=percentage
    def info (self):
        super().info()
        print(f'The College name of student is {self.cname} and percentage is {self.percentage}')
class EngineeringStudent(CollegeStudent):
    def estudent(self,name,age,cname,percentage,branch,cgpa):
        super().cstudent(name,age,cname,percentage)
        self.branch=branch
        self.cgpa=cgpa

    def info(self):
        super().info()
        print(f'The branch is {self.branch} and cgpa is {self.cgpa}')
e=EngineeringStudent()
e.student("Shree",23)
e.cstudent("Shree",23,"PRMCEAM",93)
e.estudent("Shree",23,"PRMCEAM",93,"CSE",8)
e.info()
o/p:
The name of student is Shree and age is 23
The College name of student is PRMCEAM and percentage is 93
The branch is CSE and cgpa is 8

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q4. Product → Electronics → Mobile
Create a class Product with product_name and price. Create a class Electronics
that inherits from Product and adds warranty. Create a class Mobile that inherits
from Electronics and adds ram and storage. Use constructor chaining
and display all details.

class Product:
     def __init__(self,product_name,price):
         self.product_name=product_name
         self.price=price
     def  pinfo(self):
        print(f'The Product name is {self.product_name} and price is {self.price}')        
class Electronics(Product):
     def __init__(self,product_name,price,adds_warranty):
         super().__init__(product_name,price)
         self.adds_warranty=adds_warranty
     def einfo(self):
        super().pinfo()
        print(f'The adds_warranty is {self.adds_warranty}')

class Mobile(Electronics):
    def __init__(self,product_name,price,adds_warranty,ram ,storage):
        super().__init__(product_name,price,adds_warranty)
        self.ram=ram
        self.storage=storage
    def minfo(self):
        super().einfo()
        print(f'The ram is {self.ram} and storage is {self.storage}')
m=Mobile('Samsung',59000,"1year","8gb","1TB")
m.minfo()

o/p:
The Product name is Samsung and price is 59000
The adds_warranty is 1year
The ram is 8gb and storage is 1TB

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q5. BankAccount → SavingAccount → SeniorSavingAccount
Create a class BankAccount to store account holder name and balance.
Create a class SavingAccount that adds an interest rate and calculates interest.
Create a class SeniorSavingAccount that adds age and gives 1% extra interest
if the age is greater than or equal to 60. Display the final interest.

class BankAccount:
    def __init__(self,hname,balance):
        self.hname=hname
        self.balance=balance
    def demo(self):
        print(f'The holder name is {self.hname} and balance is {self.balance}')
        

class SavingAccount(BankAccount):
    def __init__(self,hname,balance, interest):
        super().__init__(hname,balance)
        self.interest=interest
        self.calculate=self.balance*self.interest
    def demo(self):
        super().demo()
        print(f'The interest rate is {self.interest}')
        print(f'The calculated interest is {self.calculate} ')
#s=SavingAccount("RAmu",50000,0.1)
#s.demo()
class SeniorSavingAccount(SavingAccount):
    def __init__(self,hname,balance, interest,age):
        super().__init__(hname,balance, interest)
        self.age=age
    def demo(self):
        super().demo()
        if self.age>=60:
             self.calculate=self.balance+(self.balance*0.1)
             print(f'The  person age is greater than 60 then they gets total amount is {self.calculate}')
        else:
           print(f"Age is less than 60")
s=SeniorSavingAccount("Ramu",50000,0.1,65)
s.demo()

o/p:
The holder name is Ramu and balance is 50000
The interest rate is 0.1
The calculated interest is 5000.0 
The  person age is greater than 60 then they gets total amount is 55000.0


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

3. Multiple Inheritance

Q6. Person + Company → Employee
Create a class Person with name, age, and a method person_info().
Create a class Company with company_name, salary, and a method company_info().
Create an Employee class that inherits from both Person and Company.
Display all details using the Employee object.


class Person:
    def __init__(self,name, age):
        self.name=name
        self.age=age
        
    def person_info(self):
        print(f'The name of person is {self.name} and age is {self.age}')
        
class Company:
    def __init__(self,cname,salary ):
        self.cname=cname
        self.salary=salary
        
    def company_info(self):
        print(f'The name of Company is {self.cname} and salary  is {self.salary}')
        
class Employee(Person,Company):
    def __init__(self,name,age,cname,salary):
        super().__init__(name,age)
        Company.__init__(self,cname,salary)
        
    def employee_info(self):
        Person.person_info(self)
        Company.company_info(self)
e=Employee("Ramu",50,"qspder",50000)        
e.employee_info()
o/p:
The name of person is Ramu and age is 50
The name of Company is qspder and salary  is 50000

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q7. Student + Sports → Result
Create a class Student with student_name and roll_number. Create a class Sports with
sport_name and score. Create a class Result that inherits from both
Student and Sports. Display student and sports details using the Result object.
'''

'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q8. Father + Mother → Child
Create a class Father with father_name and father_occupation. Create a class Mother with mother_name
and mother_occupation.Create a class Child that inherits from both Father and Mother.
Display the details of both parents using the Child object.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

4. Hierarchical Inheritance

Q9. Company → Employee and Manager
Create a class Company with company_name and a method company_info().
Create two child classes Employee and Manager that inherit from Company.
Employee should store employee name and employee ID.
Manager should store manager name and department. Display the details of both objects.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q10. Vehicle → Car and Bike
Create a class Vehicle with brand and model. Create two child classes Car and Bike that inherit from Vehicle.
Car should store the number of doors, and Bike should store engine CC.
Create objects of both classes and display their complete details.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


'''

'''
using encapsulation concept account number, pin, and user details pass karna hai user details withdraw dep
methods inherotance use in current and saving acc and pol use we have to use display main class bank
class saving class current it should use all the opps concept except abstraction'''

