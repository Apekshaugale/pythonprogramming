#class method
#in class method object creation is not manditory

#in class method we pass 'cls' as a parameter

#cls---->always pointing to main class

'''#any method which is decorated wirh @classmethod then this method is class method.


                          #normal example
                            
class pen:
    @classmethod
    def summ(cls):
        print('Heloooooo Guysssss')
pen.summ()  #calling using class name not need to pass object
#o/p:Heloooooo Guysssss
#cls.summ()    #NameError: name 'cls' is not defined

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                  #instance method


class pen:
    def summ(self):
        print('Heloooooo Guysssss')
        
p=pen()       
pen.summ(p)  #calling using class name not need to pass object
#o/p: Heloooooo Guysssss
self.summ() #NameError: name 'self' is not defined
p.summ()
#o/p: Heloooooo Guysssss



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                #creating object
class pen:
    @classmethod
    def summ(cls):
        print('Heloooooo Guysssss')
pen.summ()  #calling using class name not need to pass object
#o/p:Heloooooo Guysssss
#cls.summ()    #NameError: name 'cls' is not defined
p=pen() #object creation
p.summ()#calling using object
#o/p:Heloooooo Guysssss
print(p)  #<__main__.pen object at 0x0000025D2F825D30> pointing to whole class object address
'''
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
if we want to access class variable inside the class method then we can access it by teo ways:
     1.using classname
     2.using self

     '''
                                       #classvariable  example and  #access using cls
'''
class pen:
    pin='steel'
    @classmethod
    def summ(cls):
        print(f'The pin is made up of {cls.pin}')   #access using cls
pen.summ()    # call using classname 
#o/p:
#The pin is made up of steel

                                                  #access using classname
                                                  
class pen:
    pin='steel'
    @classmethod
    def summ(cls):
        print(f'The pin is made up of {pen.pin}')       #access using classname
pen.summ()  # call using classname 

#o/p:
#The pin is made up of steel
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   # call using object

class pen:
    pin='steel'
    @classmethod
    def summ(cls):
        print(f'The pin is made up of {cls.pin}')        #access using classname
  
p=pen()
p.summ()  # call using object
#o/p:
#The pin is made up of steel

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   # Modification In class variable inside class method by using cls Parameter and class name
class student:
    name='Apeksha'
    rollno=59
    @classmethod
    def std(cls):
        
        print(cls.name)
student.std() #apeksha

class student:
    name='Apeksha'
    rollno=59
    @classmethod
    def std(cls):
        cls.name='shruu'  #modification using cls
        print(cls.name)
student.std() #shruu
s=student()
s.std()#shruu
print()

class student:
    name='Apeksha'
    rollno=59
    @classmethod
    def std(cls):
        student.name='puja'#modification using classname
        print(cls.name)
student.std() #puja
s=student()
s.std() #puja

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
  #modifying class variable inside second class method without parametr  
class School:
        fee=1000
        @classmethod
        def Data(cls):
                print(f'Total School Fee {cls.fee}')

        @classmethod
        def Updated_data(cls):
                School.fee=9000 #modify using classname
                #cls.fee=30000  #modify using cls
                print(f'Total School Fee {cls.fee}')#access cl
                print(f'Total School Fee {School.fee}')#cname
x=School() #oobject create 
x.Data() #1000
x.Updated_data() #9000
School.Data() # calling class name
School.Updated_data()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ##modifying class variable inside second class method with parameter
class school:
    name='yogi'
    @classmethod
    def std(cls):
        print(cls.name)
        print(school.name)

    @classmethod
    def std1(cls,newstd):
            #school.name=newstd
            cls.name='shreee'
            print(school.name)
#school.std1('shreee')
school.std()
school.std1('shreee')
o/p:
yogi
yogi
shree
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  '''  ##modifying class variable outside using classname it will work but if we do modification using object it won't work

class location:
    city='pune'
    @classmethod
    def loca(cls):
        print(cls.city)
        print(location.city)
#print(location.city)
#location.city='delhi'
#location.loca()
#o/p:
#delhi
#delhi
l=location()
l.city='Nagpur' #modification using object it won't work because it will work on class not object
l.loca() #pune pune
location.loca() #pune
