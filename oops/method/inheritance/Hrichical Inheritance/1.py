#hirarchical inhertance

#one parents multiple childern
#multiple object we create
#no of object ==no of child
'''

class Dad:
    def property(self):
        print('Dad')


class Child1(Dad):
    def Bike(self):
        print('Bike')
        
class Child2(Dad):
    def Car(self):
        print('Car')
        
class Child3(Dad):
    def Plane(self):
        print('Plane')
        
c1=Child1()
c1.property()
c1.Bike()
print(dir(Child1))

c2=Child2()
c2.property()
c2.Car()

c3=Child3()
c3.property()
'''

#modification in child class will not affect the parient class but modification
#in parent will affects the child class

class School:
    def __init__(self,name,tstudent):
        self.name=name
        self.t=tstudent      
    def show(self):     
        print(f'The Name of School is {self.name}')
        print(f'The Total number of student is {self.t}')
class Principal(School):
    def __init__(self,name,tstudent,pname,sign):
        super().__init__(name, tstudent)
        self.p=pname
        self.s=sign
    def show1(self):       
        print(f'The Principal is {self.p}')
        print(f'The Signature is {self.s}')
class Teacher(School):
    def __init__(self,name,tstudent,tname,age):
        super().__init__(name, tstudent)
        self.t=tname
        self.age=age
    def show2(self):
        
        print(self.t)
        print(self.age)
p = Principal('ABC School', 78, 'Mr. Sharma', 'Sharma')
t = Teacher('ABC School', 78, 'Mrs. Patil', 35)
p.show()
p.show1()
t.show()
t.show2()


o/p:
The Name of School is ABC School
The Total number of student is 78
The Principal is Mr. Sharma
The Signature is Sharma
The Name of School is ABC School
The Total number of student is Mrs. Patil
Mrs. Patil
35
