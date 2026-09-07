'''class data:
    def __init__(self):
        print('first')
d=data() #create object
data.__init__(d) #using classname


class apeksha:
    def __init__(self):
        print('afternoon')
    def __init__(self):
        print('Afternoon')#constructor overloading it will execute latest one always 
d=apeksha()
        


class student:
    def __init__(self):  #constructor method
        print('student class')
    def show(self):  #instance method
        print('show class')
s=student()
s.show()

#calling instance method into constructor method
class student:
    def __init__(self):
        print('student class')
        self.show()
    def show(self):
        print('show class')
s=student()

#constructor with instance method without parameter
class car:
    def __init__(self):

        #instance variable
        self.name='BMW' #instance variable
        self.colour='Red'
        self.cost='1cr'
        print(f'My car name is {self.name}\n'
              f'My car colour is {self.colour}\n'
              f'My car cost is {self.cost}')
c=car()

#constructor with instance method without parameter

class car:
    def __init__(self):

        #instance variable
        self.name='BMW' #instance variable
        self.colour='Red' #self.varname=value
        self.cost='1cr'
    def info(self):
        print(f'My car name is {self.name}\n'
              f'My car colour is {self.colour}\n'
              f'My car cost is {self.cost}')
c=car()
car.info(c)#if we are calling using calss name then we have to pass explicitly object name in it
c.info()
       
class car:
    def __init__(self):

        #instance variable
        self.name='BMW' #instance variable
        self.colour='Red' #self.varname=value
        self.cost='1cr'
        self.info()
    def info(self):
        print(f'My car name is {self.name}\n'
              f'My car colour is {self.colour}\n'
              f'My car cost is {self.cost}')
c=car()


#with usig parameter

class roomno3:
    def __init__(self,total_std,Tg,Tb,sub):#4parameter pass
        self.total_std=total_std
        self.g=Tg
        self.b=Tb
        self.sub=sub
        print(f'Total student is {self.total_std}\n'
              f'Total girls is {self.g}\n'
              f'Total boys is {self.b}\n'
              f'Subject is {self.sub}\n')
r=roomno3(55,29,30,'python')

class roomno3:
    def __init__(self,total_std,Tg,Tb,sub):#4parameter pass
        self.total_std=total_std
        self.g=Tg
        self.b=Tb
        self.sub=sub
    def classinfo(self):
        
        print(f'Total student is {self.total_std}\n'
              f'Total girls is {self.g}\n'
              f'Total boys is {self.b}\n'
              f'Subject is {self.sub}\n')
r=roomno3(55,29,30,'python')       
r.classinfo()        
        
a=roomno3(68,9,45,'java')
a.classinfo()

o/p:
Total student is 55
Total girls is 29
Total boys is 30
Subject is python

Total student is 68
Total girls is 9
Total boys is 45
Subject is java



class roomno3:
    def __init__(self,total_std,Tg,Tb,sub):#4parameter pass
        self.total_std=total_std
        self.g=Tg
        self.b=Tb
        self.sub=sub
        self.classinfo() #calling instance method in construcotr method
    def classinfo(self):
        
        print(f'Total student is {self.total_std}\n'
              f'Total girls is {self.g}\n'
              f'Total boys is {self.b}\n'
              f'Subject is {self.sub}\n')
r=roomno3(55,29,30,'python')       

o/p:
Total student is 55
Total girls is 29
Total boys is 30
Subject is python

class roomno3:
    def __init__(self,total_std,Tg,Tb,sub):#4parameter pass
        self.total_std=total_std
        self.g=Tg
        self.b=Tb
        self.sub=sub
    def classinfo(self):
        
        print(f'Total student is {self.total_std}\n'
              f'Total girls is {self.g}\n'
              f'Total boys is {self.b}\n'
              f'Subject is {self.sub}\n')
r=roomno3(55,29,30,'python','*',709)       
r.classinfo()
#TypeError: roomno3.__init__() takes 5 positional arguments but 7 were given



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
r=roomno3(55,29,30,'python','*',709)       
r.classinfo()
o/p:
Total student is 55
Total girls is 29
Total boys is 30
Subject is python
extra info ('*', 709)


class roomno3:
    def __init__(self,total_std,Tg,Tb,sub,**kwargs):#pass
        self.total_std=total_std
        self.g=Tg
        self.b=Tb
        self.sub=sub
        self.kwargs=kwargs
        
    def classinfo(self):
        
        print(f'Total student is {self.total_std}\n'
              f'Total girls is {self.g}\n'
              f'Total boys is {self.b}\n'
              f'Subject is {self.sub}\n'
              f'extra info {self.kwargs}')
r=roomno3(55,29,30,'python',a='*',b=709)       
r.classinfo()

o/p:
Total student is 55
Total girls is 29
Total boys is 30
Subject is python
extra info ('*', 709)
Total student is 55
Total girls is 29
Total boys is 30
Subject is python
extra info {'a': '*', 'b': 709}


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
b.bal=1000
print(b.bal)#0.0
b.deposite(6000)
b.withdraw(200)
o/p:
1000
Before deposite total amount is 1000
After deposite total amount is 7000
After withdreaw total amount is 6800



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
bank.bal=10000 #using class name we can't do modification in instance variable we can do midificatoion using only object
print(b.bal)#0.0
b.deposite(6000)
b.withdraw(200)
o/P:
0.0
Before deposite total amount is 0.0
After deposite total amount is 6000.0
After withdreaw total amount is 5800.0
'''
        
