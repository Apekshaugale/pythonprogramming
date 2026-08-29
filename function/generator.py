'''def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a
    return b
    return c
d=check(10,20)
print(d)

#o/p:
#    30
print()
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(q)
#o/p:<generator object check at 0x00000216A562BBC0>
#to convert it into readable format we use typecasting, looping,next()
#typecastiong
#print(list(q))
#o/p:
#[30, -10, 200]
#looping
#for i in q:
 #   print(i)
#o/p:
#30
#-10
#200
print(next(q))
#o/p:30
print(next(q))
#o/p:
#30
#-10
print(next(q))
#30
#-10
#200
print(next(q))
#o/p:StopIteration :when we perform operation three time if i call four times it will show stop iteration error

print()
def check(x,y):
   
    yield x+y
    yield x-y
    yield x*y
    yield x+y,x_y,x*y #output in the form of tuple and operation will execute at a time using only single using next()
    
    
q=check(10,20)
print(q)
print(next(q))
print(next(q))
print(next(q))

print()
'''
'''
s=[1,2,3,4,5,6]
def square(x):
    a=[]
    for i in x:
       # print(i**2)
        a.append(i**2)
    print(a)
square([1,2,3,4,5,6])

#using generator
s=[1,2,3,4,5,6]
def square(x):
    for i in x:
       yield i**2
z=square([1,2,3,4,5,6])
print(z)
print(list(z))
#using return
s=[1,2,3,4,5,6]
def square(x):
    a=[]
    for i in x:
        a.append(i**2)
    return a
print(square([1,2,3,4,5,6]))
#using generator
'''
s=[1,2,3,4,5,6]
def square(x):
    #a=[]
    for i in x:
       #print(i**2)
        #a.append(i**2)
      yield i**2
print(list(square([1,2,3,4,5,6])))

'''
a=['walmart','vistara','vstar','blind','thankyou','promax','panthor']
def odd(x):
    b=[]
    for i in x:
        #print(i)
        if len(i)%2==1:
            b.append(i)
    print(b)
odd(['walmart','vistara','vstar','blind','thankyou','promax','panthor'])


a=['walmart','vistara','vstar','blind','thankyou','promax','panthor']
def odd(x):
    b=[]
    for i in x:
        #print(i)
        if len(i)%2==1:
           b.append(i)
    return b
print(odd(['walmart','vistara','vstar','blind','thankyou','promax','panthor']))

a=['walmart','vistara','vstar','blind','thankyou','promax','panthor']
def odd(x):
    b=[]
    for i in x:
        #print(i)
        if len(i)%2==1:
           b.append(i)
    return b
print(odd(['walmart','vistara','vstar','blind','thankyou','promax','panthor']))

    
a=['walmart','vistara','vstar','blind','thankyou','promax','panthor']
def odd(x):  
    for i in x:     
        if len(i)%2==1:     
           yield i
print(list(odd(['walmart','vistara','vstar','blind','thankyou','promax','panthor'])))

   ''' 


