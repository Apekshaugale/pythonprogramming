#Assignment Examples
'''
Store and Display Name
Create a class Student
 Constructor should take name
 Print the name
# Your Task
# Output: Rahul

class student:
    def __init__(self,name):
        self.name=name
        print(self.name)
s=student('Rahul')

class student:
    def __init__(self,name):
        self.name=name    
s=student('Rahul')
#print(s.name)
student.__init__(s,'Rahul') #blankspace


2. Store Two Values
 Create class Employee
  Take name and salary
 Print both
# Output: Ravi 25000

class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        print(self.name,self.sal)
       # print(self.sal)
e=employee('Ravi',25000)

class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
    def spam(self):
        print(self.name,self.sal)
       # print(self.sal)
e=employee('Ravi',25000)
e.spam()

class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        self.spam()#instance method inside constructor
    def spam(self):
        print(self.name,self.sal)
       # print(self.sal)
e=employee('Ravi',25000)


3.Calculate Square
Constructor takes a number
 Store square in variable
 Print result
# Input: 5
# Output: 25

class square:
    def __init__(self,a):
        self.a=a 
        print(self.a*self.a)
s=square(5)
o/p:25


class square:
    def __init__(self,a):
        self.a=a
        
        print(self.a*self.a)
s=square(int(input('Enter the number: ')))

o/p:
Enter the number: 9
81


4.  Create class Laptop
 Store:
brand
price
RAM
Print like:
HP 50000 16GB
'''
class laptop:
    brand='Dell'
    price=64000
    RAM=16
    
    def __init__(self):
        print(self.brand)#using self
        print(laptop.price)#using classname
        print(self.RAM)
l=laptop()
