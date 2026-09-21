'''.clas s Parent:
    def show(self):
        print("Parent method")
        Parent.show1(self)

    def show1(self):
         
        print("Child method")
      
c = Parent()
c.show()
o/p
Parent method
Child method



class Parent:
    def show(self):
        print("Parent method")
        

    def show1(self):
         Parent.show1(self)
        print("Child method")
      
c = Parent()
c.show1()
o/p
Parent method
Child method


class Parent:
    def name1(self,name,age,add,no,loc):
        self.name=name
        self.age=age
        self.add=add
        self.no=no
        self.loc=loc
    def demo(self):
        print(self.name)
        print(self.age)
        print(self.add)
        print(self.no)
        print(self.loc)
p=Parent()
p.name1('neha',23,'pune',65879,798)
p.demo()

class Parent:
    def name1(self,name,age,add,no,loc):
        self.name=name
        self.age=age
        self.add=add
        self.no=no
        self.loc=loc
        #Parent.demo(self)
        p.demo()
    def demo(self):
        print(self.name)
        print(self.age)
        print(self.add)
        print(self.no)
        print(self.loc)
p=Parent()
p.name1('neha',23,'pune',65879,798)


class Parent:
    def name1(self,name,age,add,no,loc):
        self.name=name
        self.age=age
        self.add=add
        self.no=no
        self.loc=loc
    def demo(self):
        print(self.name)
        print(self.age)
        print(self.add)
        print(self.no)
        print(self.loc)
p=Parent()
p.name1('neha',23,'pune',65879,798)
p.demo()
age=34
p.demo()


class Parent:
    name='Rohit'
    age=23
    loc='pune'
    def demo(self):
        print(f'My name is {self.name}\n'
              f'my age is {self.age}\n'
              f'my location is {self.loc}')
p=Parent()
p.demo()
p.name='Rani'
p.demo()
Parent.demo(p)

class Parent:
    name='Rohit'
    
    loc='pune'
    def demo(self):
        self.age=24
        print(f'My name is {self.name}\n'
              f'my age is {self.age}\n'
              f'my location is {self.loc}')
        
p=Parent()
p.demo()
p.name='Rani'
p.age=44
p.demo()

class Greeting :
    def say(self,name):
        print(name)
g=Greeting()
g.say('helo')
Greeting.say(g,'rsamu')


class Animal:
    spcies ='Dog'
    def sound(self):
        print(self.spcies)#access using object 
a=Animal()
a.sound()
Animal.sound(a)
a.spcies='cat'
a.sound()
Animal.spcies='Mouse'
Animal.sound(a)
o/p:
Dog
Dog
cat
cat

class Animal:
    spcies ='Dog'
    def sound(self):
        print(Animal.spcies)#access using class name and modification using object won't affect
a=Animal()
a.sound()
Animal.sound(a)
a.spcies='cat'
a.sound()
Animal.spcies='Mouse'
Animal.sound(a)
o/p:
Dog
Dog
Dog
Mouse


class Employee:
    def sal(self):
        self.sal=3000
        print(self.sal)
    def sal1(self):
        inc=500
        self.sal+=inc
        print(self.sal)
    def sal2(self):
        dec=200
        self.sal-=dec
        print(self.sal)
e=Employee()
e.sal()
e.sal1()
e.sal2()

class Employee:
    def sal(self,sal):
       print(f'monthly salary is Rs{sal},with 1000 OT total sal is RS{sal+1000}')
 
e=Employee()
e.sal(200)

class Amazon:
    pname="watch"
    price=2456
    cname='amith'
    def order(self):
        print(self.pname)
    def delivery(self):
        
        print(self.price)
        print(self.cname)
a=Amazon()
a.order()
a.delivery()
o/p:
watch
2456
amith


class Amazon:
    def order(self,name,price,add):
        self.name=name
        self.price=price
        self.add=add
    def delivery(self):
        print(self.name)
        print(self.price)
        print(self.add)
a=Amazon()
a.order('rohan',6475,'pune')
a.delivery()

class Qsp:
    rating=1
    sub='sql'
    def mock(self):
        print(self.rating)
        print(self.sub)
q=Qsp()
q.mock()
q.rating=2
Qsp.sub='selenium'
q.mock()
o/p:
1
sql
2
selenium

class Qsp:
    rating=1
    sub='sql'
    def mock(self):
        print(Qsp.rating)
        print(Qsp.sub)
q=Qsp()
q.mock()
q.rating=2
Qsp.sub='selenium'
q.mock()
o/p:
1
sql
1
selenium

6.	BANK CLASS
Question:
WAP TO CREATE A CLASS NAME AS A BANK
Create a class Bank:
Create account (name, balance)
Deposit money
Withdraw money
Display balance


class Bank:
    def account (self,name, balance):
        self.name=name
        self.bal=balance
        print(self.name)
        print(self.bal)
    def deposite(self,money):
        self.money=money
        self.bal+=self.money       
        print(self.bal)
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        self.bal-=self.withdraw
        print(self.bal)
b=Bank()
b.account('sbi',5000)
b.deposite(500)
b.withdraw(500)

8.MOBILE CLASS
Question:
Create a class Mobile:
Store brand & price
Update price
Display details

class Mobile:
    def brand(self,brand,price):
        self.brand=brand
        self.price=price
        print(self.brand)
        print(self.price)
    def brand1(self,Updateprice):
        self.price+=Updateprice    
        print(self.price)
   
m=Mobile()
m.brand('hello',5000)
m.brand1(1000)
        

class Mobile:
    @classmethod
    def add(cls):
        print('First class')
m=Mobile()
m.add()
Mobile.add()

class School:
    name='Abc'
    @classmethod
    def display(cls):
        print(cls.name)
s=School()
s.display()
School.name='xyz' #modifiction using classname only works
s.display()


class School:
    @classmethod
    def teach(cls,name,tstd,teacher):
        cls.name=name
        cls.tstd=tstd
        cls.teacher=teacher
        
    @classmethod
    def teacher1(cls):
        print(cls.name)
s=School()
s.teach('abc',45,'rohini')
s.teacher1()


class School:
    @classmethod
    def teach(cls):
        cls.name='ABCD'
        cls.tstd=60
        cls.teacher='Rohit'
        s.teacher1()
    @classmethod
    def teacher1(cls):
        print(School.name)
s=School()

#s.teacher1()

s.teach()
School.name='XYX'
s.teacher1()


class School:
    @classmethod
    def teach(cls,name,tstd,teacher):
        cls.name=name
        cls.tstd=tstd
        cls.teacher=teacher
       
    @classmethod
    def teacher1(cls,tostd):
        cls.tostd=tostd
        cls.tstd+=cls.tostd
        print(School.name)
        print(School.tstd)
s=School()
s.teach('Hello',56,'Rohan')
s.teacher1(20)



class Math:
    @staticmethod
    def add():
        a=30
        b=30
        print(a+b)

    @staticmethod
    def sub(c,d):
        print(c*d)
#Math.add()

#Math.sub(5,4)
m=Math()
m.add()
Math.a=40#modification is not occured
m.add()
#m.sub(5,6)

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
s=Student('Prince',23)
s.display()


class Animal:
    def __init__(self):
        print('Welcome to poem')
    def sound(self):
        print('Dog is barking')
a=Animal()
a.sound()




class Student:
    def __init__(self):
        self.name = "Prabhu"

s1 = Student()
print(s1.name)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Anu", 20)
print(s1.name, s1.age)


class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        print(self.brand)
        print(self.price)
m=Mobile("Samsung", 20000)
o/p:
Samsung 20000


class Student:
    def __init__(self, name):
        self.name = name
        Student.greet(self)
    def greet(self):
        print("Hello", self.name)
s1 = Student("Rahul")
#s1.greet()

o/p:
Hello Rahul


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show(self):
        print(self.name, "has", self.balance)
b1 = Bank("Ravi", 5000)
b1.show()
o/p:Ravi has 5000


class Student:
    college = "ABC College"   # class variable
    def __init__(self, name):
        self.name = name      # instance variable
s1 = Student("Ram")
s2 = Student("Anu")
print(s1.name, s1.college)
print(s2.name, s2.college)

o/p:
Ram ABC College
Anu ABC College


#method overloading
class Sample:
    def  add(self,a):
        print('Addition')
        print(a)
    def add(self,a=0,b=0):
        print('Addition 2')
        print(a+b)
s=Sample()
s.add(5)

'''

