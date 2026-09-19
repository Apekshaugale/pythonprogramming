'''class Book:
    def __init__(self,a):
        self.a=a
    def __mul__(self,others):
        return self.a*others.a
    def __mul__(self,others):
        return self.a-others.a
    
b=Book(5)
b1=Book(6)
print(b*b1)
print(b-b1)
o/p:
-1
TypeError: unsupported operand type(s) for -: 'Book' and 'Book'



class Book:
    def __init__(self,a):
        self.a=a
    def __mul__(self,others):
        return self.a*others.a
    def __mul__(self,others):
        return self.a-others.a
    
b=Book(5)
b1=Book(6)
print(b*b1)
o/p:-1


class Book:
    def __init__(self,a):
        self.a=a
    def __mul__(self,others):
        return self.a*others.a
    def __mul__(self,others):
        return self.a-others.a
    
b=Book(5)
b1=Book(6)
print(b-b1)

o/p:
TypeError: unsupported operand type(s) for -: 'Book' and 'Book'
####

class Book:
    def __init__(self,a):
        self.a=a
    def __mul__(self,others):
        return self.a*others.a
    def __sub__(self,others):
        return self.a-others.a
    
b=Book(5)
b1=Book(6)
print(b*b1)
o/p:30

class Book:
    def __init__(self,a):
        self.a=a
    def __mul__(self,other):
        return self.a*other.a
    def __sub__(self,other):
        return self.a-other.a
    
b=Book(5)
b1=Book(6)
print(b-b1)
o/p:-1





class Student:
    def std(self):
        print('first class')
class Teacher(Student):
    def teach(self):
        super().std()
        print('Second')
class Study(Teacher):
    def stu(self):
        super().teach()
        print('Third')
class  Marks(Teacher,Study):
    def mark(self):
        super().stu()
        print('Fourth')
class Result(Study,):
    def res(self):
        super().teach()
        print('five')
m=Marks()
m.mark()

#to create empty class 
class Student:
    pass
s=Student()

#how to access class variable outside
class Student:
    x=30
    y=70
s=Student()
print(Student.x) #using class name
print(s.x)#using object




class Student:
    x=30
    y=70
s=Student
#hkllfdhkl

print(s)
#<class '__main__.Student'> mainclass pointing
s=Student()
print(s)
#<__main__.Student object at 0x0000019215155BE0> #whole class 
#print(Student.x) #using class name
#print(s.x)#using object
#print(Student.__dict__)
#help(Student)
print(Student.__doc__)


#instance method
class Student :
    amount=37984
    def demo(self):
        print(self.amount)
    def clas(self):
         self.money=475
         self.amount=self.amount+self.money
         print(self.amount)
s=Student()

s.clas()


'''
class Student:

  """ghhfgyu"""

  """hggff"""
  """u9i"""
  x=30
  y=70
    
s=Student


print(Student.__doc__)

