'''
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
        return University(self.a+other.a,self.b+other.b)#class name
    def __str__(self):
        return f'{self.a}and{self.b}'
        
    
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
        return  University(self.a+other.a,self.b+other.b,self.c+other.c)
    def __mul__(self,other):
        return University(self.a*other.a,self.b*other.b,self.c*other.c)
    def __str__(self):
        return f'{self.a} and{self.b}and{self.c}'
u=University(8,8,80)
u1=University(8,8,70)
print(u+u1)

print(u*u1)


