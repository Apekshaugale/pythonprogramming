'''class method:
    a=100
    def subject(self):
        print('Welcome to class ')
        #print(x)#nameerror
        print(method.a)#class name
        
b=method()
b.subject()
'''
'''
class Student:
    sub="SQL"   #classvariable
    def subject_name(self):
        print(f'subject name is {self.sub}')
s=Student()

#Modification by useing Class Name
# Student.sub="Python"

#Modification by useing Object
s.sub="Python_and_Sql"
s.subject_name()
'''
'''
class employee:
    sal=700
    def data(self):
        print(employee.sal)
        
a=employee()
a.data()
a.sal=800
a.data()
'''
'''
class expensive:
    def price(self):
        self.choclate=20
        self.biscuit=40
        print(self.choclate)
a=expensive()
a.price()
expensive.price(a)
  '''
'''
#instance method without parameter
class expensive:
    def price(self):
        self.choclate=20#syntax--->self.vn=value
        self.biscuit=40
        expensive.price1(self)
        expensive.price1(a)#using class name  #syntax -->classname.method(object)
    def price1(self):
        print(self.choclate)
        print(self.biscuit)
a=expensive()
a.price()
#expensive.price(a)
a.price1()

#instance method with parameter
class expensive:
    def price(self):
        self.choclate=20#syntax--->self.vn=value
        self.biscuit=40
        expensive.price1(self)
        expensive.price1(a)#using class name  #syntax -->classname.method(object)
    def price1(self):
        print(self.choclate)
        print(self.biscuit)
a=expensive()
a.price()
#expensive.price(a)
a.price1()
'''
'''

class student : #define class student
      
    def std(self):
#by default it takes self it is a object
        self.a=34
        self.b='pooja'
        student.std1(self) 
    def std1(self):
        print(self.a)
#std.student()   ---Name error without object declation
s=student()
#s.student()
#std.student()
s.std() #blankspace 
s.std1()#34

class su:
    a=100
    def add(self):
        
          print(self.a)
b=su()
#b.add()
su.a=200
b.add()
b.a=300
b.add()
su.add(b)

'''
'''
class student:
  name='Apeksha'
  def std(self):
       #print('working')
       print(student.name)
       print(self.name)
s=student()
#s.std()
#student.std(s)

#student.name='shruti'
#shruti
#shruti



s.name='lekha'
#Apeksha
#lekha

student.std(s)
s.std()
'''
class payment:
    name='hello'
    fees=45896
    def fee(self):
        #using classname
        #print(payment.name)
        print(payment.fees)
        #using object 
        #print(self.name)
        print(self.fees)
p=payment()
#access using class nmae
#payment.fee(p)
#access using object
p.fee()
#modification using classname
#payment.fees=40000
#payment.fee(p)
#p.fees=45000
#p.fee()

