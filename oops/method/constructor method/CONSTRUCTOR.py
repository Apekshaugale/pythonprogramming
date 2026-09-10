'''
class Happy:
    def __init__(self):
        print("constructor Class")
        print(self)
h=Happy()
print(h)
'''
'''
class Happy:
    def __init__(self):
        print("constructor Class")
        print(self)
h=Happy()
Happy.__init__(h)
'''

'''
class T:
    def __init__(self):
        print("first Method")

    def __init__(self):
        print("Second Method")
t=T()
'''

'''
class Data:
    def __init__(self):
        print("Hii")
        self.spam()

    def spam(self):
        print("spam method")

d=Data()
'''














'''

class Information:
    def __init__(self):
        self.name="ABC"
        self.age=34
        self.sal=5000
        self.add='Pune'
        print(f'Person name is {http://self.name}\n'
              f'Person age is {self.age}\n'
              f'Total sal is {self.sal}\n'
              f'Current Address is {self.add}\n')
i=Information()
print()
x=Information()
print()
y=Information()
'''


print()

'''
class Information:
    def __init__(self,name,age,sal,add):
        self.name=name
        self.age=age
        self.sal=sal
        self.add=add
        print(f'Person name is {http://self.name}\n'
              f'Person age is {self.age}\n'
              f'Total sal is {self.sal}\n'
              f'Current Address is {self.add}\n')
a=Information("ABC",23,1000,"Pune")
print()
b=Information("XYZ",45,6000,"Deccan")
print()
Information.__init__(,"PQR",55,9000,"Pune3")
'''

# class Data:
#     def __init__(self):
#         print("first Class")
# d=Data()         #By useing object
# Data.__init__(d)  #By useing ClassName



'''
class Room3:
    def __init__(self,total_std,Tg,Tb,sub):
        self.total=total_std
        self.girls=Tg
        self.Boys=Tb
        self.sub=sub
        print(f'Total students in class {http://self.total}\n'
              f'Total Girls count {self.girls}\n'
              f'Total Boys count {self.Boys}\n'
              f'Current subject name is {self.sub}')
r=Room3(45,20,25,"Python")
print()

r1=Room3(45,25,20,"SQL")
print()
r2=Room3(100,50,50,"Excel")


class Room3:
    def __init__(self,total_std,Tg,Tb,sub,**kwargs):
        self.total=total_std
        self.girls=Tg
        self.Boys=Tb
        self.sub=sub
        self.k=kwargs

    def class_information(self):
        print(f'Total students in class {http://self.total}\n'
              f'Total Girls count {self.girls}\n'
              f'Total Boys count {self.Boys}\n'
              f'Current subject name is {self.sub}\n'
              f'extra Information {self.k}')

e=Room3(100,50,50,"Python",a="*",b=90)
e.class_information()
print()


class Bank:
    def __init__(self):
        self.bal=0.0

    def deposit(self,amount):
        print(f'Before deposit Total amount {self.bal}')
        self.bal=self.bal+amount
        print(f'after deposit Total amount {self.bal}')

    def withdrawal(self,amount):
        self.bal=self.bal-amount
        print(f'after withdrawal total amount is {self.bal}')

b=Bank()
# b.bal=1000
Bank.bal=10000
print(b.bal) #0.0
b.deposit(5000)   #5000.0
b.withdrawal(2500)

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

m1 = Mobile("Samsung", 20000)
m1= Mobile("Apple", 80000)

print(m1.brand, m1.price)
#print(m2.brand, m2.price)


class Student:
    college = "ABC College"   # class variable

    def __init__(self, name):
        self.name = name      # instance variable

s1 = Student("Ram")
s2 = Student("Anu")

print(s1.name, s1.college)
print(s2.name, s2.college)

class roomno3:
    def __init__(self,total_std,Tg,Tb,sub,*args):#4parameter pass
        self.total_std=total_std
        self.g=Tg
        self.b=Tb
        self.sub=sub
        self.args=args
        
    def classinfo(self):
        
        print(f'Total student is {self.total_std}\n'
              f'Total girls is {self.g}\n'
              f'Total boys is {self.b}\n'
              f'Subject is {self.sub}\n'
              f'extra info {self.args}')
r=roomno3(55,29,30,'python',89,'ghee',709)       
r.classinfo()
'''
class bank:
    def __init__(self):
        self.bal=0.0
    def deposite(self,amount):
        print(f'Before deposite total amount is {self.bal}')
        self.bal+=amount
        print(f'After deposite total amount is {self.bal}')
    def withdraw(self,amount):
        self.bal-=amount
        print(f'After withdreaw total amount is {self.bal}')

b=bank()
bank.bal=1000
print(b.bal)#0.0
b.deposite(6000)
b.withdraw(200)

