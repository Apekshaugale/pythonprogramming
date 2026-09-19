#ouside modificaton using getter,setter,deleter
'''class Bank:
    def __init__(self,name,accno,bal):
        self.name=name
        self._accno=accno
        self.__bal=bal
    def Getter(self):
        print(getattr(self,"name","Name is deleted\n"),
              getattr(self,"_accno","Accno s deleted\n"),
              getattr(self,"_Bank__bal","Balance is deleted"))
    def Setter(self,name,acc_num,bal):
        self.name=name
        self._accno=acc_num
        self.__bal=bal
    def Deleter(self):
        del self.__bal
        del self.name
    
b=Bank("Monu",6198708093,900000)
b.Getter()
b.Setter("dipe",697902124,80000)
#b.Deleter()
b.Getter()


#property decorator:

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @property
    def data(self):
        return (getattr(self,"name","deleted\n"),
                getattr(self,"age","delelted"))
    @data.setter
    def data(self,newname,newage):
        self.name=newname
        self.newage=newage
    @data.deleter
    def data(self):
        del self.name
e=Employee("xys",32)
print(e.data)

e.data=("hkfk",43)#TypeError: Employee.data() missing 1 required positional argument: 'newage'

print(e.data)

class Parent:
    def name1(self):
     #self.name="sneha"
    #print(self.name)
class Mom(Parent):
    def demo(self):
       self.name="sneha"
        
class Baba(Parent):
    def baba(self):
        self.no=7905
        print(self.no)
class Son(Mom,Baba):
    def son(self):
        super().baba()
        super().name()
b=Baba()
#b.demo()
s=Son()
s.son()

class Parent:
    def name1(self):
        value=55
class Mom(Parent):
    def demo(self):
        self.name='sneha'
        print(self.name)
class Baba(Parent):
    def baba(self):
        self.no=3827
        print(self.no)
class Son(Mom,Baba):
    def son(self):
        super().baba()
        super().demo()
b=Baba()
s=Son()
s.son()

class Class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def demo(self):
        print(self.name)
        print(self.age)
        print('class first')
class Student(Class):
    def __init__(self,name,age,height,money):
        self.h=height
        self.m=money
        super().__init__(name,age)
    def demo(self):
        super().demo()
        print(self.h)
        print(self.m)
        print('class second')
class Teacher(Student):
    def __init__(self,name,age,height,money,course):
        self.c=course
        super().__init__(name,age,height,money)
        super().demo()
        print(self.c)
c=Teacher("Rohit",34,5,89065,"HTML")

'''
class School:
    name="Priya"
    @classmethod
    def demo(cls):
        print(cls.name)
School.demo()
