"""
4.write a decorator function calculate the execution time of any function

import time
def outer(func):
    def inner():
        start=time.time()
        print(start)
        func()
        end=time.time()
        print(end)
        print(end-start)
    return inner
@outer
def main():
    print()//time.sleep()
main()
    
        


5.wadf to check if the 1st arguments is lesser than 2nd argument
if then swap them and perform division
but the condition is you should not modify the original function

def outer(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            
            c=a/b
            print(c)
        
        func(a,b)
    return inner
@outer
def main(a,b):
    print("hello")
main(2,4)

6.wadf to add 2 numbers and display the message before
"i am doing addition operation" after performing print
the message "addition operation is done"

o/p--->i am doing addition operation"
       value
     "addition operation is done

def menu(func):
    def hello(a,b):
        print("i am doing addition operation")
        func(a,b)
        print("addition operation is done")
    return hello
@menu
def add(a,b):
    print(a+b)
add(5,6)

7.create a decorator to return only positive out from any subtraction

def dec(func):
    def positive(a,b):
        
        func(a,b)
        print(abs(a-b))
    return positive
@dec
def main(a,b):
    #print(a-b)
    pass
main(7,8)

8.create a decorator which counts the number of function calls

count=1
def outer(func):
    def inner():
        global count
        print(count)
        func()
        count+=1
    return inner
@outer
def demo():
    pass
demo()
demo()
demo()

9.wap to sum of the positional arguments and get the length
of the keywords arguments

def inner(func):
    def outer(*args,**kwargs):
        
        func(*args,**kwargs)
        print(sum(args))
        print(len(kwargs))
        
    return outer
@inner
def main(*args,**kwargs):
    print()
main(2,3,4,b=4,d=5)


10.write a decorator function to print the type of
datatype before performing the action

def outer(func):
    def inner(a,b):
        print(type(a))
        print(type(b))
        func(a,b)
    return inner
@outer
def demo(a,b):
    print()
demo("hello",[4,6])

11.write a decorator operation on the given number and the
condition is A>B then perform multiplication in decorator function else
 cube it in decorator

def num(func):
    def inn(a,b):
        if a>b:
            print(a*b)
        else:
            print(a**3,b**3)

        func(a,b)
    return inn
@num
def main(a,b):
    print()
main(1,2)

12.create a decorators to which prints name of called main
function and counts the function calls

count=0
def name(func):
    def inner():
        global count
        func()
        
        count+=1
        print(count)
    return inner
@name
def main():
    #print()
    ...
main()
main()
main()

13.create a decorators to which prints names of called functions
and checks the number is even or odd

def dec(func):
    def crt(a):
        if a%2==0:
            print("Even")
        else:
            print("Odd")
        print(func.__name__)
        func(a)
    return crt
@dec
def main(a):
    ...
main(5)
        
        

14.create a decorator which delays its execution as per user input

import time
def para(a):
  def dec(func):
     def inner():
        time.sleep(a)

        func()
        print("hello")

     return inner
  return dec
@para(int(input("Enter the dalay:")))
def main():
    ... 
main()

15.write a multilevel decorator to log some message

def first(one):
    def fir(a,b):
        print("add")
        one(a,b)
        print(a+b)
    return fir
def second(one):
    def fir(a,b):
        print("sub")
        one(a,b)
        print(a-b)
    return fir
def third(one):
    def fir(a,b):
        print("mul")
        one(a,b)
        print(a*b)
    return fir
@first
@second
@third
def multilevel(a,b):
    print("multilevel decorator")
multilevel(4,5)

16.write a multilevel decorators to accept username and register
number of employee

def outerf(c,d):
  def first(one):
     def fir(a,b):
        print(c,d)
        one(a,b)
       
     return fir
  return first

def outers(e,f):
  def second(one):
      def sec(a,b):
        print(e,f)
        one(a,b)
        
      return sec
  return second
def outert(g,h):
  def third(one):
     def thi(a,b):
        print(g,h)
        one(a,b)
        
     return thi
  return third
@outerf("sham",1993)
@outers("Ram",1003)
@outert("Hemant",1643)
def multilevel(a,b):
    print("multilevel decorator")
multilevel(4,5)

17.WADF TO DELAY FOR 3 SECONDS AND DISPLAY THE NAME, DELAY FOR
3 SECONDS AND DISPLAY EMAIL ADDRESS ,
 DELAY FOR 3 SECONDS AND DISPLAY PHONE NUMBER

import time
def delay(func):
    def deal():
        time.sleep(3)
        print("Ramu")
        time.sleep(3)
        print("ramu@gmail.com")
        func()
        time.sleep(3)
        print("4656789102")
    return deal
@delay
def demo():
    pass
demo()
        

18 .using 3 decorators show me one example"""
"""
