'''class School:
    
    def __init__(self):
        self.name='Apeksha Ugale'
        self.Sname='S.B.High.School'
        self.marks='91.60%'
    def school_info(self):
        super().__init__()
        print(f'My name is {self.name}\n'
              f'My School name is {self.Sname}\n'
              f'My 10th percentage is {self.marks} ')
        
class Twelth(School):
    
        def __init__(self):
            self.Cname='S.B.High.School And Jr Science College'
            self.marks='81.83%'

        def college_info(self):
            super().__init__()
            super().school_info()
            print(f'My College name is {self.Cname}\n'
              f'My 12th percentage is {self.marks} ')

class Degree(Twelth):

    def __init__(self):
        self.Dclgname='PRMCEAM'
        self.cgpa='8.4'
    def Degree_info(self):
        super().__init__()
        super().college_info()
        print(f'My Degree College name is {self.Dclgname}\n'
              f'My Degree CGPA is {self.cgpa} ')
t=Degree()
t.Degree_info()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class School:
    def __init__(self,name,Sname,marks):
        self.name=name
        self.Sname=Sname
        self.marks=marks
    def school_info(self):
        print(f'My name is {self.name}\n'
              f'My School name is {self.Sname}\n'
              f'My 10th percentage is {self.marks} ')
        
class Twelth(School):  
        def __init__(self,name,Sname,marks,Cname,marks1):
            super().__init__(name,Sname,marks)
            self.Cname=Cname
            self.marks1=marks1
        def college_info(self):         
            super().school_info()
            print(f'My College name is {self.Cname}\n'
              f'My 12th percentage is {self.marks} ')

class Degree(Twelth):
    def __init__(self,name,Sname,marks,Cname,marks1,Dclgname,cgpa):
        super().__init__(name,Sname,marks,Cname,marks1)
        self.Dclgname=Dclgname
        self.cgpa=cgpa
    def Degree_info(self):
        super().college_info()#method overriding
        print(f'My Degree College name is {self.Dclgname}\n'
              f'My Degree CGPA is {self.cgpa} ')
t=Degree("Apeksha","SBHIGH school","91.60%","S.B.High.School And Jr Science College","81.83% ","PRMCEAM","8.4")
t.Degree_info()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
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
        

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
2. Multilevel Inheritance   
Create a Python program using multilevel inheritance:
BankAccount = store holder name and balance.
SavingAccount = add interest rate and calculate interest.
SeniorSavingAccount = add age and give 1% extra interest
if age >= 60.
class 

class BankAccount:
    def __init__(self,name,balance):
        self.n=name
        self.balance=balance
    def person_info(self):
         #super().__init__()
         print(f"Person name is {self.n}\n"
               f"The account balance is {self.balance}")      
class SavingAccount(BankAccount):
    def __init__(self,name,balance,int_rate):
        super().__init__(name,balance)
        self.int_rate=int_rate
        self.calculate_interest=self.balance*self.int_rate
    def account_info(self):
        super().person_info()
        print(self.calculate_interest)
class SeniorSavingAccount(SavingAccount):
#(self,name,balance,int_rate,age):
    def demo(self,name,balance,int_rate,age):
       # super().__init__(name, balance, int_rate)
        self.age=age
        if self.age>60:
            self.calculate_interest=self.calculate_interest*0.1
            price=self.balance+self.calculate_interest
            print(price)
        else:
            print(self.calculate_interest)
s=SeniorSavingAccount("Apeksha",50000,0.2)
s.account_info()      
s.demo("Apeksha",50000,0.2,65)       
    

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
3. Multiple Inheritance   
Create a Python program using multiple inheritance.
Create a Person class with name, age, and a details() method.
Create a Company class with company name, salary, and a details() method.
Create Employee(Person, Company) that inherits from both classes.
Display employee and company details using the Employee object.

class Person:
    def  __init__(self,name, age):
        self.name=name
        self.age=age
    def demo(self):
        
        print(f'The name of Person is {self.name} and age is {self.age}')
class Company:       
    def __init__(self,cname, salary):
        self.cname=cname#'Qspider'
        self.salary=salary#50000
    def  show(self):
        
        print(f'The company name is {self.cname} and salary is {self.salary}')
        
class Employee(Person, Company):
    def __init__(self,name, age,cname, salary):
        super().__init__(name, age)
        Company.__init__(self,cname, salary)
        #super().__init__(cname, salary)
        Person.demo(self)
        #e.demo()#why not executed 
        #Company.show(self)#working
        super().show()
 # def details(self):
  #      Person.demo(self)
   #     Company.show(self)

e=Employee("Apeksha",24,'Qspider',50000)       
#e.details()      


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
4. Hierarchical Inheritance   
Create a Company class with company name.
Create Employee and Manager classes that inherit from Company.
Employee should store employee name and ID. Manager should store manager name and department.
Display the details of both objects.
'''
class Company:
    def __init__(self,cname):
        self.cname=cname
    def cinfo(self):
        print(f'The company name is {self.cname}')
class Employee(Company):
    def emp_info(self,cname,name,ID):
        super().__init__(cname)
        self.name=name
        self.ID=ID
    def einfo(self):
        super().cinfo()
        print(f'The Employee name is {self.name} and employee id is {self.ID}')
class Manager(Company):
    def emp_info(self,cname,mname,dept):
        super().__init__(cname)
        self.mname=mname
        self.dept=dept
    def minfo(self):
        super().cinfo()
        print(f'The Manager name is {self.mname} and department  is {self.dept}')
e=Employee('Qspider')
m=Manager('Qspider')
e.emp_info('Qspider','Rushi','E14')
m.emp_info('Qspider','Ramu','DA')
e.einfo()
m.minfo()


class Company:
    def __init__(self,cname):
        self.cname=cname
    def cinfo(self):
        print(f'The company name is {self.cname}')
class Employee(Company):
    def __init__(self,cname,name,ID):
        super().__init__(cname)
        self.name=name
        self.ID=ID
    def einfo(self):
        super().cinfo()
        print(f'The Employee name is {self.name} and employee id is {self.ID}')
class Manager(Company):
    def __init__(self,cname,mname,dept):
        super().__init__(cname)
        self.mname=mname
        self.dept=dept
    def minfo(self):
        super().cinfo()
        print(f'The Manager name is {self.mname} and department  is {self.dept}')
e=Employee('Qspider','Rushi','E14')
m=Manager('JQspider','Ramu','DA')
e.einfo()
m.minfo()
'''
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
5.

Objective:
Create a simple library management system to manage books and track which books are borrowed or available in a library.

Classes and Inheritance Structure:
Parent Class: Book
Child Class: BorrowedBook
Explanation:
    
Parent Class (Book):

The Book class will represent the general attributes of a book.
It will contain attributes such as:
title: The title of the book
author: The author of the book
isbn: ISBN number for identification
available: Boolean attribute to check if the book is available
Methods in the Book class could include:
get_details(): Displays the details of the book.
mark_unavailable(): Marks the book as not available.
mark_available(): Marks the book as available.

Child Class (BorrowedBook):

The BorrowedBook class inherits from the Book class.
This class will handle information specific to books that are borrowed.
Additional attributes can be added here such as:
borrower_name: Name of the person who borrowed the book.
due_date: The date when the book is due for return.
Methods in the BorrowedBook class could include:
borrow(): Takes borrower details and marks the book as borrowed.
return_book(): Returns the book, marks it as available, and removes borrower details. 


class Book:
    def __init__(self):
        self.title='Atomic Habbit'
        self.author='James Clear'
        self.isbn=1234567231456
        #self.status='Available'
        
    def get_details(self):
        super().__init__()
        print(f'My book name is {self.title}\n'
              f'Book author is {self.author} and ISBN number is {self.isbn}')
        
    def mark_unavailable(self,status):
        self.status=status
        if self.status=="Not Available":
            print('True')
        else:
                print('False')
        
    def mark_available(self,statuss):
        self.status=statuss
        if self.status=="Available":
            print('True')
        else:
                print('False')
         
#b=Book()
#b.mark_available("Available")

class BorrowedBook(Book):
     def borrow(self):
         self.borrower_name='Apeksha'
         self.due_date='12.Jan.2026'
         self.status='Borrowed'
     def return_book(self):
        super().__init__()
        print(f'My book name is {self.title}\n'
              f'Book author is {self.author} and ISBN number is {self.status}')
b=BorrowedBook()
b.mark_available("Available")
b.return_book()

'''
'''
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def get_details(self):
        print(f'My book name is {self.title}\n'
              f'Book author is {self.author} and ISBN number is {self.isbn}')
    def mark_unavailable(self, status):
        self.status = status
        if self.status == "Not Available":
            print('True')
        else:
            print('False')
    def mark_available(self, status):
        self.status = status
        if self.status == "Available":
            print('True')
        else:
            print('False')
class BorrowedBook(Book):
    def __init__(self, title, author, isbn, borrower_name, due_date, status):
        # Call parent constructor
        super().__init__(title, author, isbn)
        self.borrower_name = borrower_name
        self.due_date = due_date
        self.status = status
    def borrow(self):
        print("Book is borrowed")
    def return_book(self):
        self.get_details()
       
        print(f'The borrower name is {self.borrower_name}\n'
              f'Book Due date is {self.due_date} and status is {self.status}')
b = BorrowedBook('Atomic Habit','James Clear',47678978456,'Apeksha','12.Jan.2026','Borrowe')

#b.get_details()
b.mark_available("Not Available")
b.borrow()
b.return_book()
'''
