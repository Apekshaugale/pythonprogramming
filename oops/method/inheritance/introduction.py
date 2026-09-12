'''class Dad:   
   cash=100000
   def villa(self): #parent class method
       print('Dads villa')
class child(Dad):
    def home(self): #child class method
        bike='BMW'
        print("Dad's gift")
print(dir(Dad))
print(dir(Dad))
#d=child()
#d.villa()
#d.home()
#print(d.cash)

'''

'''
class Dad:
    cash=100000
    def villa(self):
        print("Dad's villa")

class Child(Dad):
    bike_name="Bmw"
    def Home(self):
        self.cash=900
        print(http://self.cash)
        print("Dad's Gift")

'''


'''
print(dir(Dad))
print()
print(dir(Child))
'''
'''

d=Child()
print(d.cash)
d.villa()
d.Home()
'''

'''
class Dad:
    def spam(self):
        print("spam method")

class Child(Dad):
    def spam(self):
        # Dad.spam(self)
        super().spam()
        print("child method")
c=Child()
c.spam()
'''

'''
class A:
    def student_data(self,name,age):
        self.name=name
        self.age=age
        print(f'student Name is {self.name}\n'
              f'student age is {self.age}')

class B(A):
    def student_data(self,sub,usn):
        self.sub=sub
        self.usn=usn
        # super().student_data("XYZ",24)
        A.student_data(self,"ABC",17)
        print(f'subject Name is {self.sub}\n'
              f'student USN number is {self.usn}')

b=B()
b.student_data("Python","P1234")
'''

'''

class A:
    def student_data(self,name,age):
        self.name=name
        self.age=age
        print(f'student Name is {http://self.name}\n'
              f'student age is {self.age}')

class B(A):
    def student_data(self,name,age,sub,usn):
        self.sub=sub
        self.usn=usn
        A.student_data(self,name,age)
        # super().student_data(name,age)
        print(f'subject Name is {self.sub}\n'
              f'student USN number is {self.usn}')

b=B()
b.student_data("AB",24,"Excel","P1234")
'''
'''
class Test:
    def __init__(self):
        print("C1")

class Data(Test):
    def __init__(self):
        super().__init__()
        Test.__init__(self)
        print("C2")
d=Data()
'''





'''
class Student:
defstudent_data(self,name,sub):
       self.name=name
       self.sub=sub
       print(f'StudentName is {self.name}')
       print(f'SUbject Name is {self.sub}')


class Information(Student):
defstudent_data(self,clg_name,marks):
       super().student_data(name="XYZ",sub="SQL")
       self.clg=clg_name
       self.marks=marks
       print(f'CLG Name is {self.clg}')
       print(f'Total Marks is {self.marks}')


i=Information()
i.student_data("PYSPIDERS",99)





Assignment Questions

1.Create a class Employee with attributes name and salary.
Create a child class Manager that prints both values.
2.Create a class Bank with attribute balance.
 Create a child class SavingsAccount with methods:
deposit()
withdraw() 


3.Create a class Person with a constructor.
Create a child class Student and use super() to initialize parent data.



4.Create a class Vehicle with method start().
Override this method in child class Bike.


'''



