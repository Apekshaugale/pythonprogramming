
'''#scope
#The place of variable


#types of scope :
#   1.local
#   2.global
#   3.nonlocal


#   1.local variable 
# Any variable present inside the function then we can called  it as a local variable

#local variable we can't  access outside directly if we access it will show name error

#how to access local variable outside ?
'''
#by help of return keyword
'''
def spam():
    name='python'
    print(name)
spam()
print(name)         #------>Name Error


def span():
    name='python'
    return name
q=spam()
print(q)

#   2.global variable

#Any variable is present outside the function then we can call it as a global variable

#Global variable we can access anywhere into function means  access inside or access ouside the function it will work.

x=200           #global variable
def display():
    a=100             #local variable
    print(x)          #global variable
display()
print(x)



x=200           #global variable
def display():
    a=100             #local variable
    print(x)          #global variable
    print(a)
    
display()
print(x)

'''
#   3.Nonlocal variable

#a variable which is inbetween the two function
#it always uses nested function then we can used
#we can used nonlocal kwyword in inner function of that variable.
'''
x=10
def outer():
    y=20
    print(x)

    def inner():
        z=30
        print(x)
        print(z)
        print(y)
    inner()
    print(x)
    print(y)
outer()
print(x)
print(z)    #Name error


#using nonlocal keyword used for modification
#nested function can't work on global keyword
x=10
def outer():
    y=20
    print(x)

    def inner():
        nonlocal y
        z=30
        print(x)
        y+=180     
        print(z)
        print(y)
    inner()
    print(x)
    print(y)
outer()
print(x)
print(z) 
'''
'''
def demo(a,b,c):
    print(a,b,c)
demo(12,30,40)
demo
print(demo)
def demo(a,b,c):
    return
print(demo(12,30,40))
'''
def demo(a,b):
    #print(a,b)
    return a,b
x=demo(10,20)
print(x)
