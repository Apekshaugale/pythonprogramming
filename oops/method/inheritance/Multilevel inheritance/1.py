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



'''
#construcor overrding
class Employee:
    def  __init__(self,Cname,Tmember,Tpackage):
        self.Cname=Cname
        self.Tmember=Tmember
        self.Tpackage=Tpackage
    def data(self):
        print(f'Company name is {self.Cname}\n'
              f'Total memeber is {self.Tmember}\n'
              f'Total package is {self.Tpackage}')
class Startemployee(Employee):
    def  __init__(self,Cname, Tmember, Tpackage,sal,yop,role):
        self.sal=sal
        self.yop=yop
        self.role=role
        super().__init__(Cname, Tmember, Tpackage)
    def Info(self):
        print(f'salary is {self.sal}\n'
              f'YOP  is {self.yop}\n'
              f'Role  is {self.role}')
class Rules(Startemployee):
    def __init__(self,Cname, Tmember, Tpackage,sal,yop,role,intime,outtime,rolename):
        self.intime=intime
        self.outtime=outtime
        self.rolename=rolename
        super().__init__(Cname, Tmember, Tpackage,sal,yop,role)
    def Check(self):
        print(f'Intime  is {self.intime}\n'
              f'Outtime is {self.outtime}\n'
              f'Intime  is {self.rolename}')
       
r=Rules('Capgemini',60,'7lpa',45000,2026,'Anyalist',2,5,'BA')
r.data()
r.Info()
r.Check()

o/p:
Company name is Capgemini
Total memeber is 60
Total packege is 7lpa
salary is 45000
YOP  is 2026
Role  is Anyalist
Intime  is 2
Outtime is 5
Intime  is BA


    
