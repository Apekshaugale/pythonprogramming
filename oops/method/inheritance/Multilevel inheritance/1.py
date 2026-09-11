'''class Grandpa:
    def Agrii(self):
       print('Land')
class Father(Grandpa):
    def Property(self):
        print('Home')
class Child(Father):
    def Bike(self):
        print('Bike')
c=Child()
c.Bike()
c.Property()
c.Agrii()
#--------------------Method overriding   we can achieve using classname and super function----------------------------------------
class Dad:
    def Money(self):
        print('1cr')
class Child1(Dad):
    def Money(self):
        print('50lakh')
class Child2(Child1):
    def Money(self):
        print('25lakh')
c=Child2()
c.Money()#25lakh


class Dad:
    def Money(self):
        print('1cr')
class Child1(Dad):
    def Money(self):
        super().Money()
        print('50lakh')
class Child2(Child1):
    def Money(self):
        super().Money()
        print('25lakh')
c=Child2()
c.Money()#25lakh

#-------using classname---
class Dad:
    def Money(self):
        print('1cr')
class Child1(Dad):
    def Money(self):
        Dad.Money(self)
        print('50lakh')
class Child2(Child1):
    def Money(self):
        Child1.Money(self)
        print('25lakh')
c=Child2()
c.Money()
#1cr
#50lakh
#25lakh


#------constructor overriding-----------------
class Teacher:
    def __init__(self):
        print('First Class')
class Std1(Teacher):
    def __init__(self):
        super().__init__()
        print('Second class')
class Std2(Std1):
    def __init__(self):
        super().__init__()
        print('Third class')
s=Std2()
print(dir(s))


class Teacher:
    def __init__(self):
        print('First Class')
class Std1(Teacher):
    def __init__(self):
        super().__init__()
        print('Second class')
class Std2(Std1):
    def __init__(self):
        super().__init__()
        print('Third class')
s=Std2()
o/p:
First Class
Second class
Third class
#-------------by passing parameters-----------------------------
class Institude:
    def Information(self,In,Stack,Fee):
        self.In=In
        self.Stack=Stack
        self.Fee=Fee
        print(f'Institude name is {self.In}\n'
              f'Student Course name is {self.Stack}\n'
              f'Total fees is {self.Fee}')
class Student(Institude):
    def  Subject(self,Sn,Tc,Tp):
        self.Sn=Sn
        self.Tc=Tc
        self.Tp=Tp
        print(f'Subject name is {self.Sn}\n'
              f'Total class name is {self.Tc}\n'
              f'Total time  is {self.Tp}')
class Result(Student):
    def Finalstage(self,TM,Grade):
        self.TM=TM
        self.Grade=Grade
        print(f'Total marks is {self.TM}\n'
              f'Grade is {self.Grade}'   ) 
r=Result()
r.Finalstage(57,'A+')
r.Subject('Shree',60,'6month')        
r.Information("Qspider",'Datascience',85000)
o/p:
Total marks is 57
Grade is A+
Subject name is Shree
Total class name is 60
Total time  is 6month
Institude name is Qspider
Student Course name is Datascience
Total fees is 85000


#construcor overrding
class Employee:
    def  __init__(self,Cname,Tmember,Tpackege):
        self.Cname=Cname
        self.Tmember=Tmember
        self.Tpackege=Tpackege
    def data(self):
        print(f'Company name is {self.Cname}\n'
              f'Total memeber is {self.Tmember}\n'
              f'Total packege is {Tpackege}')
class Startemployee(Employee):
    def  __init__(self,sal,yoe,role):
        self.sal=sal
        self.yop=yop
        self.role=role
        super().__init__(Cname, Tmember, Tpackage)
    def Info(self):
        print(f'salary is {self.sal}\n'
              f'YOP  is {self.yop}\n'
              f'Role  is {self.role}')
class Rules(Startemployee):
    def __init__(self,intime,outtime,rolename):
        self.intime=intime
        self.outtime=outtime
        self.rolename=rolename
        super().__init__(Cname, Tmember, Tpackage,sal,yop,role)
    def Check(self):
        print(f'Intime  is {self.intime}\n'
              f'Outtime is {self.outtime}\n'
              f'Intime  is {self.rolename}')
       
r=Rules('Capgemini',60,'7lpa',45000,2026,'Anyalist',2,5,'BA')
r.Data()
r.Info()
r.Check()
'''
class Employee:
    def __init__(self, Cname, Tmember, Tpackage):
        self.Cname = Cname
        self.Tmember = Tmember
        self.Tpackage = Tpackage
    def Data(self):
        print(f'Company Name : {self.Cname}\n '
              f'and Total Member : {self.Tmember}\n '
              f'and Total Package : {self.Tpackage}')
class Startemployee(Employee):
    def __init__(self, Cname, Tmember, Tpackage, sal, yoe, role):
        super().__init__(Cname, Tmember, Tpackage)
        self.sal = sal
        self.yoe = yoe
        self.role = role
    def Info(self):
        print(f'Salary : {self.sal} \n'
              f'and YOE : {self.yoe}\n '
              f'and Role : {self.role}')
class Rules(Startemployee):
    def __init__(self, Cname, Tmember, Tpackage,
                 sal, yoe, role, intime, outtime, rolename):
        super().__init__(Cname, Tmember, Tpackage, sal, yoe, role)
        self.intime = intime
        self.outtime = outtime
        self.rolename = rolename
    def Check(self):
        print(f'In-time : {self.intime}\n '
              f'and Out-time : {self.outtime}\n '
              f'and Role Name : {self.rolename}')

r = Rules('Capgemini', 60, '7lpa', 45000, 2026, 'Analyst', 2, 5, 'BA')
r.Data()
r.Info()
r.Check()       
