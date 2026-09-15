
'''
class Student: #Student is a class name
    name='rock' #class variable 
    age=23
    total_sub=5
s=Student() #object creation #s is a object name
#print(name)---NameError: name 'name' is not defined
#print(age)
#print(total_sub) ----> we can't acces  data directly outside from the class  if we aces it it will show name error
'''

'''
Then How to acces class varable  data outside
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
here we have two ways :
1.By using ClassName
2.By using object

'''
'''
#by using class name
#print(f'student name is "{Student.name}"')
print(Student.name)
print(Student.age)
print(Student.total_sub)
#by using object
print(s.name)
print(s.age)
print(s.total_sub)

'''
'''
how data is internally arranging if we want to check

intaernally all data is present in form of dictionary
if you want to check :

print(ClassName.__dict__)#key :value
print(s.__dict__)#{}
#this method is magic method any method if we are using double underscopre it call magic
'''


#a=10-->public
#-a=10--->protected
#-a=10-->private
#--d--- --->magic method
'''
help(Student)
#help(class)
'''
'''
o/p:
Help on class Student in module __main__:

class Student(builtins.object)
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  age = 23
 |
 |  name = 'rock'
 |
 |  total_sub = 5

'''
'''
class emp:
    Eid=11
    Name='helo'
e=emp()
e1=emp()

    
#1
emp.Name='Hello'
print(emp.Name) #Hello
print(e.Name) #Hello
print(e1.Name) #Hello
#2
e.Eid=132
print(e.Eid)#132
print(e1.Eid)#11
print(emp.Eid)#11
#3
emp
'''
class emp :
    eid=89
    ename='khushi'
print(emp.eid)#89
e=emp()
print(e)#<__main__.emp object at 0x000001E1F6EC5D30>
e=emp
print(e)#<class '__main__.emp'>
