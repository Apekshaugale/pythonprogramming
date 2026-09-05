'''6.	BANK CLASS
Question:
WAP TO CREATE A CLASS NAME AS A BANK
Create a class Bank:
Create account (name, balance)
Deposit money
Withdraw money
Display balance


class bank:
    def account(self):
        self.name='hello'
        self.balance=50000
        print(f'The balance is {self.balance}')
    def deposit(self):
        self.dep=6000
        self.balance=self.balance+self.dep
        print(f'The deposit is {self.dep}')
        print(f'The current balance is {self.balance}')
        
    def withdraw(self):
        self.withdraw=500
        self.balance=self.balance-self.withdraw
        print(f'The withdraw amount is {self.withdraw}')
        print(f'The amount after  withdraw is {self.balance}')
        
        
        
b=bank()

b.account()
b.deposit()
b.withdraw()

o/p:
The balance is 50000
The deposit is 6000
The current balance is 56000
The withdraw amount is 500
The amount after  withdraw is 55500



7.	STUDENT CLASS
Question:
Create a class Student:
Store marks
Calculate grade

class student:
    
    def grade(self):
        self.marks=57
        if self.marks>=85:
            print('Grade A')
        elif self.marks>=75:
            print('Grade B')
        elif self.marks>=65:
            print('Grade C')
        elif self.marks>=35:
            print('Grade D')
        else:
            print('Fail')
s=student()
s.grade()
#o/p:Grade D

class student:
    marks=int(input('Enter the marks : '))
    def grade(self):
        marks=self.marks
        if self.marks>=85:
            print('Grade A')
        elif self.marks>=75:
            print('Grade B')
        elif self.marks>=65:
            print('Grade C')
        elif self.marks>=35:
            print('Grade D')
        else:
            print('Fail')
s=student()
s.grade()

o/p:
Enter the marks : 74
Grade C
'''
'''
8.MOBILE CLASS
Question:
Create a class Mobile:
Store brand & price
Update price
Display details

'''
'''
class mobile:
    brand='nothing'
    price=27000
    def update(self):
        print(f'The brand of mobile is {self.brand}')
        print(f'The price of mobile is {self.price}')
    def details(self):
        print(f'The new  brand of mobile is {self.brand}')
        print(f'The new price of mobile is {self.price}')#using object
        
m=mobile()
m.update()
mobile.brand='Samsung'#modification using classname
mobile.price=87000
m.details()


o/p:
The brand of mobile is nothing
The price of mobile is 27000
The new  brand of mobile is Samsung
The new price of mobile is 87000


class mobile:
    brand='nothing'
    price=27000
    def update(self):
        print(f'The brand of mobile is {self.brand}')
        print(f'The price of mobile is {self.price}')
    def details(self):
        print(f'The new  brand of mobile is {self.brand}')
        print(f'The new price of mobile is {self.price}')#using object
        
m=mobile()
m.update()
m.brand='Samsung'#modification using object
m.price=87000
m.details()

o/p:
The brand of mobile is nothing
The price of mobile is 27000
The new  brand of mobile is Samsung
The new price of mobile is 87000


class mobile:
    brand='nothing'
    price=27000
    def update(self):
        print(f'The brand of mobile is {self.brand}')
        print(f'The price of mobile is {self.price}')
    def details(self):
        print(f'The new  brand of mobile is {mobile.brand}')
        print(f'The new price of mobile is {mobile.price}')#we are accessing using classname and modifying using object it won't affects
        
m=mobile()
m.update()
m.brand='Samsung'#object
m.price=87000
m.details()

o/p:
The brand of mobile is nothing
The price of mobile is 27000
The new  brand of mobile is nothing
The new price of mobile is 27000


class mobile:
    brand='nothing'
    price=27000
    def update(self):
        print(f'The brand of mobile is {self.brand}')
        print(f'The price of mobile is {self.price}')
    def details(self):
        print(f'The new  brand of mobile is {mobile.brand}')
        print(f'The new price of mobile is {mobile.price}')
        
m=mobile()
m.update()
m.brand='Samsung'
m.price=87000
mobile.details(m)
o/p:
The brand of mobile is nothing
The price of mobile is 27000
The new  brand of mobile is nothing
The new price of mobile is 27000
'''



'''
10.Create a class Marks
Store marks of 3 subjects
Calculate total and average
class marks:
    m1=80
    m2=40
    m3=50
    def total(self):
        self.marks=self.m1+self.m2+self.m3
        print(f'The total marks is {self.marks}')
    def avg(self):
        self.average=self.marks/3
        print(f'The average marks is {self.average}')
m=marks()
m.total()
m.avg()

o/p:
The total marks is 170
The average marks is 56.666666666666664
'''
class marks:
    m1=int(input('Enter the marks of subject1  : '))
    m2=int(input('Enter the marks of subject2: '))
    m3=int(input('Enter the marks of subject3 : '))
    def total(self):
        self.marks=self.m1+self.m2+self.m3
        print(f'The total marks is {self.marks}')
    def avg(self):
        self.average=self.marks/3
        print(f'The average marks is {self.average}')
m=marks()
m.total()
m.avg()

o/p:
    Enter the marks of subject1  : 48
Enter the marks of subject2: 78
Enter the marks of subject3 : 85
The total marks is 211
The average marks is 70.33333333333333

class marks:
    m1=int(input('Enter the marks of subject1  : '))
    m2=int(input('Enter the marks of subject2: '))
    m3=int(input('Enter the marks of subject3 : '))
    def total(self):
        self.marks=self.m1+self.m2+self.m3
        print(f'The total marks is {self.marks}')
    def avg(self):
        self.average=self.marks/3
        print(f'The average marks is {self.average}')
m=marks()
m.total()
m.avg()
o/p:
Enter the marks of subject1  : 48
Enter the marks of subject2: 78
Enter the marks of subject3 : 85
The total marks is 211
The average marks is 70
