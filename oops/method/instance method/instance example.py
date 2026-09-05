#4.Create a class Employee Store name and salary Increase salary by 5000 Display details
'''class employee:
    name='pooja'
    salary=50000
    def emp(self):
        print(f'The name of employee is {employee.name}')
        print(f'The salary of employee is {employee.salary}')
e=employee()
employee.emp(e)
e.emp()
The name of employee is pooja
The salary of employee is 50000
The name of employee is pooja
The salary of employee is 50000


class employee:
    def emp(self):
        self.name='pooja'
        self.salary=50000
    def emp1(self):
        print(f'The name of employee is {self.name}')
        print(f'The salary of employee is {self.salary}')
e=employee()
#employee.emp1(e)
e.emp()  # creates name and salary
e.emp1()      # displays name and salary
employee.emp(e)
employee.emp1(e)
o/p:
The name of employee is pooja
The salary of employee is 50000
The name of employee is pooja
The salary of employee is 50000


class employee:
    def emp(self):
        self.name='pooja'
        self.salary=50000
        employee.emp1(self)
    def emp1(self):
        print(f'The name of employee is {self.name}')
        print(f'The salary of employee is {self.salary}')
e=employee()

e.emp()  
employee.emp(e)
o/p:
The name of employee is pooja
The salary of employee is 50000
The name of employee is pooja
The salary of employee is 50000


#5.Create a class Gameplayer  Store player name and score Increase score Display score
class Gameplayer:
    pname='hardik'
    score=60
    def sco(self):
        print(self.score)
        print(Gameplayer.score)
g=Gameplayer()
Gameplayer.sco(g)
g.sco()
o/p:
60
60
60
60


class Gameplayer:
    def sco(self):
     self.pname='hardik'
     self.score=60
    def sco1(self):
        print(self.score)
        
g=Gameplayer()
g.sco()
g.sco1()
o/p:60

class Gameplayer:
    def sco(self):
     self.pname='hardik'
     self.score=60
     Gameplayer.sco1(self)
    def sco1(self):
        print(self.score)
        
g=Gameplayer()
g.sco()
g.sco1()
o/p:
60
60
'''
#6.	BANK CLASS WAP TO CREATE A CLASS NAME AS A BANK Create a class Bank:
#Create account (name, balance)
#Deposit money
#Withdraw money
#Display balance

'''
7.	STUDENT CLASS
Question:
Create a class Student:
Store marks
Calculate grade


8.MOBILE CLASS
Question:
Create a class Mobile:
Store brand & price
Update price
Display details



9.	ACCOUNT CLASS
Question:
Create a class Account:
Store account number & balance
Check balance


10.Create a class Marks
Store marks of 3 subjects
Calculate total and average




'''

class menu:
    name='Apeksha'
    def name1(self):
        print(menu.name)
n=menu()
#menu.name1(n)
n.name='sakshi'
menu.name1(n)
