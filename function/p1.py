# 1. Greeting Function
# Write a function that takes a name and prints:
# Hello Amit
'''#normal
def fun(name):
    print('Hello' ,name)
fun('Amit')
o/p:
    Hello Amit
    
#using return   
def fun(name):
    return 'Hello',name
print(fun('Amit'))
o/p:
    ('Hello', 'Amit')
    
#using yield
#using typecasting   
def fun(name):
    yield 'Hello',name
print(list(fun('Amit')))
o/p:
    [('Hello', 'Amit')]


#using next()
    
# 2. Add Two Numbers
# Write a function that takes two numbers and returns their sum.
# Input: 10, 20
# Output: 30
def num(a,b):
    return a+b
print(num(12,6))
#o/p:
#18

def num(a,b):
    print(a+b)
num(10,5)
#o/p:
#  15

#using user input
def num():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number :'))
    return a+b
print(num())
o/p:
Enter the number :8
Enter the number :8
16

#using for loop
def num(a,b):
    yield a+b
for i in num(12,6):
     print(i)
o/p:18

#using next()
def num(a,b):
    yield a+b
x = num(12, 13)
print(next(x))
#or
print(next(num(12,13)))
o/p:
    25
'''
'''
# 3. Find Difference
# Write a function that accepts two numbers and returns their difference.
#normal
def diff(a,b):
    print(a-b)
diff(12,6)
#o/p:
#  6

#using return and using user input
def diff():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    return a-b
print(diff())
#o/p:
#Enter the number :25
#Enter the number: 5
#20
'''
'''
#using yield
#using typecasting
def diff():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    yield a-b
print(list(diff()))
#o/p:
#Enter the number :5
#Enter the number: 3
#[3]

#using for loop
def diff():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    yield a-b
for i in diff():
    print(i)
#Enter the number :5
#Enter the number: 3
#2
    
#using next()
def diff():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    yield a-b
print(next(diff()))

# 4. Find Maximum
# Write a function that accepts two numbers and returns the greater number.
#normal
def Max():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    if a>b:
        print(f'{a} is greater than {b}')
    else:
        print(f'{b} is greater than {a}')
Max()
o/p:
Enter the number :15
Enter the number: 18
18 is greater than 15

#using return
def Max():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    if a>b:
        return (f'{a} is greater than {b}')
    else:
        return (f'{b} is greater than {a}')
print(Max())
#o/p:
Enter the number :5
Enter the number: 12
12 is greater than 5

#using typecasting  and using yield
def Max():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    if a>b:
        yield (f'{a} is greater than {b}')
    else:
        yield (f'{b} is greater than {a}')
print(list(Max()))

#using for loop
def Max():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    if a>b:
        yield (f'{a} is greater than {b}')
    else:
        yield (f'{b} is greater than {a}')
for i in Max():
   print(i)
o/p:
Enter the number :5
Enter the number: 11
11 is greater than 5

#using next()
def Max():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    if a>b:
        yield (f'{a} is greater than {b}')
    else:
        yield (f'{b} is greater than {a}')
print(next(Max()))
o/p:
Enter the number :8
Enter the number: 5
8 is greater than 5

# 5. Find Minimum
# Write a function that accepts two numbers and returns the smaller number.
#normal using user input
def Min():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    print(min(a,b))
Min()
o/p:
Enter the number :5
Enter the number: 8
5

#using return
def Min():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    return (min(a,b))
print(Min())
o/p:
Enter the number :8
Enter the number: 7
7

#using typecasting using yield
def Min():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    yield (min(a,b))
#print(Min())----><generator object Min at 0x0000015D4566B920>
print(list(Min()))

#using for loop
def Min():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    yield (min(a,b))
for i in Min():
    print(i)
    
#using next()
def Min():
    a=eval(input('Enter the number :'))
    b=eval(input('Enter the number: '))
    yield (min(a,b))
print(next(Min()))

# 6. Check Even or Odd
# Write a function that accepts a number and returns "Even" or "Odd".
#normal  and using user input
def evenodd():
    a=eval(input('Enter the number :'))
    if a%2==0:
        print('even')
    else:
        print('Odd')
evenodd()

#using return
def evenodd():
    a=eval(input('Enter the number :'))
    if a%2==0:
        return ('even')
    else:
        return('Odd')
print(evenodd())

#using typecasting and using yield
def evenodd():
    a=eval(input('Enter the number :'))
    if a%2==0:
        yield('even')
    else:
        yield('Odd')
print(list(evenodd()))

#using for loop
def evenodd():
    a=eval(input('Enter the number :'))
    if a%2==0:
        yield('even')
    else:
        yield('Odd')
for i in evenodd():
    print(i)

#using next()
def evenodd():
    a=eval(input('Enter the number :'))
    if a%2==0:
        yield('even')
    else:
        yield('Odd')
print(next(evenodd()))

o/p:
Enter the number :15
Odd
Enter the number :12
even


# 7. Check Positive, Negative or Zero
# Write a function that accepts a number and returns:
# Positive
# Negative
# Zero
#normal and using user input
def PNZ():
    a=int(input('Enter the number :'))
    if a>0:
        print('Positive')
    elif a<0:
        print('Negative')
    elif a==0:
        print('Zero')
PNZ()

    
#using return
def PNZ():
    a=int(input('Enter the number :'))
    if a>0:
        return 'Positive'
    elif a<0:
        return 'Negative'
    elif a==0:
        return 'Zero'
print(PNZ())

#using typecasting using yield
def PNZ():
    a=int(input('Enter the number :'))
    if a>0:
        yield 'Positive'
    elif a<0:
        yield 'Negative'
    elif a==0:
        yield 'Zero'
print(list(PNZ()))

#using for loop
def PNZ():
    a=int(input('Enter the number :'))
    if a>0:
        yield 'Positive'
    elif a<0:
        yield 'Negative'
    elif a==0:
        yield 'Zero'
for i in PNZ():
 print(i)
 
#using next()
def PNZ():
    a=int(input('Enter the number :'))
    if a>0:
        yield 'Positive'
    elif a<0:
        yield 'Negative'
    elif a==0:
        yield 'Zero'
print(next(PNZ()))

# 8. Square a Number
# Write a function that accepts a number and returns its square.
# Input: 5
# Output: 25
#normal #using user input
def squ():
    a=int(input('Enter the number : '))
    print(a**2)
squ()

#using return
def squ():
    a=int(input('Enter the number : '))
    return a**2
print(squ())

#using typecasting using yield
def squ():
    a=eval(input('Enter the number : '))
    yield a**2
print(list(squ()))
#using for loop
for i in squ():
    print(i)
#using next()
print(next(squ()))

o/p:
Enter the number : 15
[225]
Enter the number : 2
4
Enter the number : 5
25

# 9. Cube a Number
# Write a function that accepts a number and returns its cube.
#normal
#using return
#using typecasting
#using user input
#using yield
#using for loop
#using next()

# 10. Find Last Digit
# Write a function that accepts a number and returns its last digit.
# Input: 12345
# Output: 5
#normal using user input
def last():
    a=eval(input('Enter the numder :'))
    print(a%10)
last()

#using return
def last():
    a=eval(input('Enter the numder :'))
    return a%10
print(last())

#using typecasting using yield
def last():
    a=eval(input('Enter the numder :'))
    yield a%10
print(set(last())) 
#using for loop
for i in last():
    print(i)
#using next()
print(next(last()))

# 11. Find First Digit
# Write a function that accepts an integer and returns its first digit.
# Input: 45678
# Output: 4
#normal #using user input
def first_digit():
    n = int(input("Enter the number: "))

    for i in range(len(str(n))):
        n = n // 10
        if n < 10:
            return n

print(first_digit())
#using return
#using typecasting using yield
#using for loop
#using next()

# 12. Calculate Area of Rectangle
# Write a function that accepts length and breadth and returns the area.
# Area = length × breadth
#normal
def area(l,b):
    print(l*b)
area(3,2)

#using return
def area(l,b):
    return l*b
print(area(3,2))

#using typecasting using yield
def area(l,b):
    yield l*b
print(list(area(3,2)))

#using for loop
def area(l,b):
    yield l*b
for i in area(3,4):
 print(i)

#using next()
def area(l,b):
    yield l*b
print(next(area(3,4)))
'''
