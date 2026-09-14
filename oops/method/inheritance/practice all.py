
#Single Level Inheritance
'''
Q1. Vehicle–Car
Create a class Vehicle with a method start() that prints "Vehicle started".
Create a child class Car that adds a method music_system() that prints "Music system on".
Create an object of Car and call both methods.

class Vehical :
    def start(self):
        print('Vehical started')
class Car(Vehical):
    def music_system(self):
        print('Music system on')
c=Car()
c.music_system()
c.start()
Vehical.start(c)

o/p:
Music system on
Vehical started
Vehical started

Q2. Class variable inheritance
Create a class Company with a class variable company_name = "TechCorp" and
a method about() that prints the company name.
Create a child class Employee with its own method work() that prints "Employee is working".
Access company_name from a Employee object and call both methods.

class Company:
     company_name = "TechCorp"
     def about(self):
        print(self.company_name)
class Employee(Company):
    def work(self):
        print("Employee is working")
e=Employee()
e.about()
e.work()

o/p:
TechCorp
Employee is working



Q3. Constructor in single-level inheritance
Create a parent class Person with a constructor that takes name and prints "Person created: name".
Create a child class Student (no constructor of its own) and create an object of Student
passing a name — observe what happens and explain why.

class Person:
    def __init__(self,name):
        self.name=name
        print(f'Person created: {self.name}')
class Student(Person):
    def std(self):
         print('std child')
s=Student('Rohit')
s.std()

o/p:
Person created: Rohit
std child


Q4. Overriding + super()
Create a class Shape with a method area() that prints "Area not defined".
Create a child class Circle that overrides area() to print "Area of circle"
but also calls the parent's area() using super() before printing its own message.

class Shape:
    def area(self):
        print("Area not defined")
class Circle(Shape):
    def area(self):
        super().area()
        print("Area of circle")
c=Circle()
c.area()
o/p:
Area not defined
Area of circle

Q5. Bank account (practical)
Create a class Account with attributes acc_no and balance, and a method show_balance().
Create a child class SavingsAccount that adds a method add_interest(rate)
which increases balance
by the given rate % and prints the new balance.

class Account:
    acc_no = 3355567897
    balance = 5000
    def show_balance(self):
        print(self.acc_no)
        print(self.balance)
class SavingsAccount(Account):
    def add_interest(self, rate):
        self.balance = self.balance + (self.balance * rate / 100)
        print(self.balance)
s = SavingsAccount()
s.show_balance()
s.add_interest(5)
o/p:
3355567897
5000
5250.0
'''
#Multi-Level Inheritance
'''
Q6. Grandparent → Parent → Child
Create Grandparent with a method property() → prints "Ancestral property".
Create Parent(Grandparent) with a method house() → prints "Family house".
Create Child(Parent) with a method car() → prints "Own car".
Create a Child object and call all three methods.

class Grandparent:
    def property(self):
        print("Ancestral property")
class Parent(Grandparent) :
    def house(self):
        print("Family house")
class Child(Parent):
    def car(self):
        print('Own Car')
c=Child()
c.property()
c.house()
c.car()
o/p:
Ancestral property
Family house
Own Car    


Q7. Constructors chained with super()
Create three classes A, B(A), C(B), where each class's  __init__
prints its own class name (e.g., "Constructor of A") and
calls super().__init__() (except A). Create an object of C and observe the order of output.

class A:
    def __init__(self):
      print("Constructor of A")  
class B(A):
    def __init__(self):
        super().__init__()
        print("Constructor of B")  
class C(B):
    def __init__(self):
        super().__init__()
        print("Constructor of C")  
c=C()
o/p:
Constructor of A
Constructor of B
Constructor of C

Q8. Method overriding across 3 levels
Create Employee with method salary() → prints "Base salary: 20000".
Create Manager(Employee) that overrides salary() to add a bonus, calling super().salary() first.
Create Director(Manager) that overrides salary() again, adding a further bonus and calling super().salary().
Create a Director object and call salary().

class Employee:
    def salary(self):
        self.BaseSalary=20000
        print(self.BaseSalary)
class Manager(Employee):
    def salary(self):
        self.bonus=2000
        super().salary()
        self.BaseSalary+=self.bonus
        print(self.BaseSalary)
class Director(Manager):
    def salary(self):
        self.furtherbonus=10000
        super().salary()
        self.BaseSalary+=self.furtherbonus
        print(self.BaseSalary)
d=Director()
d.salary()
o/p:
20000
22000
32000

Q9. Real-world multi-level with parameterized constructors
Create Person(name, age), then Employee(Person) adding emp_id, then
Manager(Employee) adding department.
Each class should store its own attributes using super().__init__(...).

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Employee(Person):
    def __init__(self,name,age,empid):
        self.empid=empid
        super().__init__(name,age)
        print(self.empid)
class Manager(Employee):
    def __init__(self,name,age,empid,dept):
        self.dept=dept
        super().__init__(name,age,empid)
    def show(self):
        print(self.dept)
m=Manager('Rohit',23,'E01','DA')
m.show()
o/p:
Rohit
23
E01
DA

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,empid):
        self.empid=empid
        super().__init__(name,age)
class Manager(Employee):
    def __init__(self,name,age,empid,dept):
        self.dept=dept
        super().__init__(name,age,empid)
    def show(self):
        
        print(self.name)
        print(self.age)
        print(self.empid)
        print(self.dept)
o/p:
Rohit
23
E01
DA































