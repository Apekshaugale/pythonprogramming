#compositon
#HAS-A _relationship
'''
class Teacher:
    def demo(self):
       print('Frist term')
       
class Student:
    def show(self):

        t=Teacher()
        t.demo()
        print('Second')

s=Student()
s.show()


o/p:
Frist term
Second



class  Teacher:
    def show(self,name,age):
        self.name=name
        self.age=age

    def model(self):
        print(self.name)
        print(self.age)
        
class Employee:
    def show1(self,eid,eno):
        self.eid=eid
        self.eno=eno

    def model1(self):
        
        print(self.eid)
        print(self.eno)
e=Employee()
e.show1('E01',43)
e.model1()

class  Teacher:
    def show(self,name,age):
        self.name=name
        self.age=age

    def model(self):
        Teacher.show(self,'ROHIT',23)#access data using classname
        print(self.name)
        print(self.age)
        
class Employee:
    def show1(self,eid,eno):
        self.eid=eid
        self.eno=eno

    def model1(self):
        self.show1('E01',43)#access data using object
        t=Teacher()#create object by using  classname
        t.model()
        print(self.eid)
        print(self.eno)
e=Employee()
#e.show1('E01',43)
e.model1()

'''
class  Teacher:
    def show(self,name,age):
        print(name)
        print(age)
class Employee:
    def show1(self,eid,eno):
        t=Teacher()#create object by using  classname
        t.show('ROHIT',23)
        print(eid)
        print(eno)
e=Employee()
e.show1('E01',43)
