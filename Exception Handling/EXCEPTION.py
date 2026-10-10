'''1.Write a program that accepts two numbers and performs division.
#Handle ZeroDivisionError if the second number is 0. 

a=int(input('Enter the number:'))

try:
    b=int(input('Enter the number:'))
    print(a/b)
except:
    print("Handle ZeroDivisionError")

#2.Ask the user to enter an integer. Handle ValueError if the user
enters text instead of a number. 


try : 
    a=int(input('Enter the interger:'))
except :
       print("HandleValueError")
  
3.numbers = [10, 20, 30, 40, 50]
Ask the user for an index and print the value. Handle IndexError.

numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter the index: "))
    print(numbers[index])
except IndexError:
    print("Handle Index Error")

#4.student = {"name": "Rahul", "age": 22, "course": "Python"}
#Ask the user for a key and print its value. Handle KeyError.

student = {"name": "Rahul", "age": 22, "course": "Python"}
try:
    A=eval(input("Enter the key : "))
    print(student[A])
except:
    print('Handle KeyError')


5.Write a program that accepts two inputs and performs division.
Handle both ValueError and ZeroDivisionError. 


try:
    a=int(input("Enter the number:"))
    b=int(input("enter the number:"))
    print(a/b)
except ZeroDivisionError:
     print("ZeroDivisionError")
except ValueError:
    print("Value Error")
    

6.Write a program that converts "abc" into an integer.
and display the exception message.

try:
    a=int(input('Enter the number:'))
except BaseException  as A:
    print(A)
    print('Generic exception block')


7.Write a program to open data.txt and read its contents.
Handle FileNotFoundError.Use finally to display: File operation completed

try:
   file=open("hello.txt",'r')
   print(file)
except FileNotFoundError:
    print(' Handle FileNotFoundError')

8.Create a login program.
username = "admin"
password = "python123"
Ask the user for username and password.
Handle invalid input and use finally to print:
Login process completed



uname = "admin"
pword = "python123"
username=eval(input('Enter the username :'))
password=eval(input('Enter the password :'))

try:
 if uname==username and pword==password:
    print('Login process completed')
 else:
        print('Invalid_inputError')
except:
    print('Invalid_inputError Handle')
finally:
    print("Login process completed")

9.Create a situation where an undefined variable is accessed.
Handle NameError. 

a=5
b=5
try:
    print(c)
except:
    print('Handle NameError')

10.Create a situation where a method is called on an
object that doesn't support that method. Handle AttributeError.  '''
a="string"
try :
    print(a.append(5))
 
except BaseException as A:
    print("Handle AttributeError")
    print(A)



