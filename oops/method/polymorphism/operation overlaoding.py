'''
class Book:
    def __init__(self,a):
        self.a=a

    def __add__(self, other):
        print(self.a+other.a)

    def __sub__(self, other):
        print(self.a-other.a)

    def __mul__(self, other):
        print(self.a * other.a)

    def __truediv__(self, other):
        print(self.a / other.a)

    def __floordiv__(self, other):
        print(self.a // other.a)

    def __mod__(self, other):
        print(self.a % other.a)

    def __gt__(self, other):
        print(self.a > other.a)

    def __lt__(self, other):
        print(self.a < other.a)

    def __eq__(self, other):
        print(self.a==other.a)

b=Book(100)
b1=Book(200)
b+b1  #300
b-b1  #-100
b*b1
b/b1
b//b1
b%b1
b>b1  #100>200
b<b1
b==b1


print()


class Book:
    def __init__(self,a):
        self.a=a

    def __add__(self, other):
        return self.a+other.a

    def __sub__(self, other):
        return (self.a-other.a)

    def __mul__(self, other):
        return (self.a * other.a)

    def __truediv__(self, other):
        return (self.a / other.a)

    def __floordiv__(self, other):
        return (self.a // other.a)

    def __mod__(self, other):
        return (self.a % other.a)

    def __gt__(self, other):
        return (self.a > other.a)

    def __lt__(self, other):
        return (self.a < other.a)

    def __eq__(self, other):
        return (self.a==other.a)

b=Book(100)
b1=Book(200)
print(b+b1)  #300
print(b-b1)  #-100
print(b*b1)
print(b/b1)
print(b//b1)
print(b%b1)
print(b>b1)  #100>200
print(b<b1)
print(b==b1)



class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return self.a+other.a,self.b+other.b
        #return  10+15,         20+25
p=Point(10,20)
p1=Point(15,25)
print(p+p1)


print()



class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return Point(self.a+other.a,self.b+other.b)
        #return  10+15,         20+25


    def __sub__(self, other):
        return Point(self.a-other.a,self.b-other.b)


    # def __str__(self):
    #     return f'{self.a} and {self.b}'
            #OR

    def __repr__(self):
        return f'{self.a} and {self.b}'


p=Point(10,20)
p1=Point(15,25)
print(p+p1)
print(p-p1)



class Point:
    
    def __init__(self,a):
        self.a=a

    def __add__(self, other):
        print(self.a+other.a)
p=Point(20)#poiting to self.a
p1=Point(30)#pointing to other.a
p+p1



class Point:
    
    def __init__(self,a):
        self.a=a

    def __add__(self, other):
        print(self.a+other.a)

    def __add__(self,other):
        print(self.a-other.a)
p=Point(20) #poiting to self.a
p1=Point(30) #pointing to other.a
p+p1#-10
p-p1#TypeError: unsupported operand type(s) for -: 'Point' and 'Point'


class Point:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
p=Point(50)
b=Point(20)
print(p+b)



class Point:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return Point(self.a+other.a)
    def __str__(self):
        return  f'{self.a}' #formating string must 
p=Point(50)
b=Point(20)
print(p+b)


class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return Point(self.a+other.a,self.b+other.b)
        #return  10+15,         20+25


    def __sub__(self, other):
        return Point(self.a-other.a,self.b-other.b)


    def __str__(self):
         return f'{self.a} and {self.b}'
            
p=Point(10,20)
p1=Point(15,25)
print(p+p1)
print(p-p1)     
'''
