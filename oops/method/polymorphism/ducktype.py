'''#Duck type:

#Definition
#Duck Typing is a concept in Python where the type or class of an object is less important than the methods or properties it has.


#In simple words: “If it looks like a duck, swims like a duck, and quacks like a duck, then it is treated as a duck.” 


#Python checks for behavior (methods/attributes), not the actual type of the object.



ex-->1
class Dog:
    def sound(self):
        print("bark......")

class Cat:
    def sound(self):
        print("Meow......")

class Duck:
    def sound(self):
        print("Quack.......")

def Animal(x):
    x.sound()

# l=[Dog(),Cat(),Duck()] #l=Dog(),l=Cat(),l=Duck()

for i in (Dog(),Cat(),Duck()):
    Animal(i)

'''

'''
ex--->2
class Bird:
    def fly(self):
        print("am flying")
class Plane:
    def fly(self):
        print("am travelling")
class Human:
    def fly(self):
        print("am plying above------>****")
def Check(q):
    http://q.fly()

for i in (Bird(),Plane(),Human()):
    Check(i)

print()
l=[Bird(),Plane(),Human()]
for k in l:
    Check(k)

print()

x=Bird()
y=Plane()
z=Human()
Check(x)
Check(y)
Check(z)

class University:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
u=University(5)
u1=University(9)
print(u+u1)


class University:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a+other.a,self.a+other.a
u=University(4,5)
u1=University(5,4)
print(u+u1)


class University:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return University(self.a+other.a,self.a+other.a)#class name
    def __str__(self):
        return f'{self.x}+{self.y}'
        
    
u=University(4,5)
u1=University(5,4)
print(u+u1)
'''

class University:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def __add__(self,other):
        return self.a+other.a,self.b+other.b,self.c+other.c
    def __mul__(self,other):
        return self.a*other.a,self.b*other.b,self.c*other.c
u=University(8,8,80)
u1=University(8,8,70)
print(u+u1)

print(u*u1)

