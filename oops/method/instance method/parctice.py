'''Q1. Employee Payroll
Create a class Employee:

Constructor takes name and salary (instance variables).
Class variable company_name = "TechCorp".
Instance method show_details() →
prints name, salary, and company name (via self).
Classmethod change_company(cls, new_name)
→ updates company_name for all employees.
Staticmethod is_valid_salary(salary) → returns True if salary > 0, else False.

class Employee:
    cname = "TechCorp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print(self.name,self.salary,self.cname)
    @classmethod
    def ccompany(cls, new_name):
        cls.n=new_name

    @staticmethod
    def vaild(salary):
        if salary>0:
            print('True')
        else:
            print('False')
e=Employee('Ram',5000)
e.show_details()
e.ccompany('QSP')
e.vaild(5000)

o/p:
Ram 5000 TechCorp
True
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q2. Bank Account
Create a class BankAccount:

Constructor takes holder_name and balance.
Class variable bank_name = "State Bank".
Instance method deposit(amount) → adds to self.balance.
Classmethod rename_bank(cls, new_name) →
changes bank_name for all accounts.
Staticmethod validate_amount(amount) → returns True only if amount > 0.

class BankAccount:
    bank_name = "State Bank"
    def __init__(self,holder_name,balance):
        self.hname=holder_name
        self.balance =balance
    def deposit(self,amount) :
        self.amount=amount
        self.balance+=self.amount
        print(self.balance)

    @classmethod
    def rename_bank(cls, new_name):
        cls.name=new_name
        print(cls.name)

    @staticmethod
    def validate_amount(amount):
        if amount >0:
            return 'Truee'
        else:
            return 'False'
b=BankAccount('jitu',50000)
b.deposit(5000)
b.rename_bank('sbi')
print(b.validate_amount(5000))
o/p:
55000
sbi
Truee
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Q3. Student Result System
Create a class Student:

Constructor takes name and a list of marks (3 subjects).
Class variable passing_marks = 40.
Instance method total_and_average() → calculates
and prints total/average from self.marks.
Classmethod update_passing_criteria(cls, new_value) →
changes passing_marks.
Staticmethod is_pass(mark) → returns True/False by
comparing against a hardcoded 40 (independent check).

class Student:
    passing_marks = 40
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1mark=sub1
        self.sub2mark=sub2
        self.sub3mark=sub3
        
    def total_and_average(self):
        total=self.sub1mark+self.sub2mark+self.sub3mark
        print(total)
        average=total/3
        print(average)
        
    @classmethod
    def update_passing_criteria(cls, new_value):
        cls.passing_marks=new_value
        print(cls.passing_marks)

    @staticmethod
    def is_pass(mark):
        
        if mark>=40:
            return True
        else:
            return False
s=Student('Ram',45,67,45)
s.total_and_average()
s.update_passing_criteria(45)
print(s.is_pass(40))
o/p:
157
52.333333333333336
45
True

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q4. Product Inventory
Create a class Product:

Constructor takes name, price, quantity.
Class variable tax_rate = 18.
Instance method total_price() → returns price * quantity plus tax
(using self. and class var).
Classmethod update_tax(cls, new_rate) → changes tax_rate globally.
Staticmethod apply_discount(price, discount_percent) →
returns discounted price (pure calculation, no self/cls).

class Product:
    tax_rate = 18
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        total=((self.price*self.quantity)+self.tax_rate)
        return total

    @classmethod
    def update_tax(cls, new_rate):
        cls.tax_rate=new_rate
        print(cls.tax_rate)

    @staticmethod
    def apply_discount(price, discount_percent):
        return price-(price*discount_percent/100)
p=Product('Sita',45000,5)
print(p.total_price())
p.update_tax(25)
print(p.apply_discount(45000, 10))
o/p:
225018
25
40500.0
'''

