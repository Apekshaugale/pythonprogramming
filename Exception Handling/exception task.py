'''1.Write a Python program to accept input from the user and convert it into an integer. 
  Handle Value Error if the user enters a string.

try:
 a=int(input('Enter the input:'))
except ValueError:
    print("Handle ValueError")


2.Create a list of 5 elements. Ask the user to enter an index and print the corresponding element.
 Handle IndexError and ValueError

list1=list(input("Enter the list of 5 element :"))
a=int(input('Enter the index of element :'))
try:
  print(list1[a])
except IndexError :
    print("Index error handle")
except ValueError:
    print("Value Error")
    



3.Create a dictionary containing student names and marks. 
Ask the user to enter a student name and display their marks. Handle KeyError.

student=eval(input("enter the dictionary :"))
#print(type(student))
a=eval(input("Enter the key :"))
try:
  print(student[a])
except KeyError:
    print("Handle KeyError")

4.Accept two numbers from the user and divide them. Handle ZeroDivisionError and ValueError.



try:
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    print(a/b)
except ZeroDivisionError:
    print("Handle ZeroDivisionError")
except ValueError:
    print("Handle Value Errror")


5.Accept a string from the user and convert it into a floating-point number. Handle invalid conversions.


try:
  a=eval(input("Enter the string:"))
  print(float(a))
except BaseException as C:
    print("Handle ValueError")
    print(C)

6.Create a list containing integers and strings. Ask the user to calculate the sum of all elements.
 Handle TypeError for incompatible data types.


a=eval(input("Enter the list:"))
try:
  print(sum(a))
except:
    print("Handle TypeError")


7.Create a tuple containing 10 numbers. Ask the user to enter an 
index and display the corresponding element. Handle invalid indexes.


a=eval(input("Enter the tuple:"))
#print(type(a))
i=eval(input("Enter the index:"))
#print(type(i))
try:
  print(a[i])
except:
  print("Handle invalid idexes")

8.ATM Withdrawal (InsufficientBalanceError)
Accept the user's account balance and withdrawal amount.
Conditions:
Withdrawal amount must be positive.
Withdrawal amount must not exceed the available balance.
Handle invalid numeric input using ValueError.
Raise a custom exception for insufficient balance.





9.Student Result
Accept marks for three subjects and calculate the average.
Handle invalid input and raise ValueError if any mark is outside
the range of 0–100.


s1=eval(input("Enter the sbject1 mark:"))
if 0<s1<=100:
           print('Valid marks')
s2=eval(input("Enter the sbject2 mark:"))
if 0<s2<=100:
           print('Valid marks')

s3=eval(input("Enter the sbject3 mark:"))
if 0<s3<=100:
           print('Valid marks')

print((s1+s2+s3)/3)


10.Age Verification
Accept a user's age and determine whether
they are eligible to vote based on a minimum age of 18.
Handle non-numeric input and raise ValueError for negative ages.


class AgeError(BaseException):
  try:
     age=eval(input('Enter the age:'))   
     if age>=18:
      print('Eligible to vote')
     else:
      raise AgeError
  except:
    print('Handling error')


11.Shopping Discount
Accept the total shopping amount and calculate a discount:
Above ₹5,000: 20%
₹2,000–₹5,000: 10%
Below ₹2,000: No discount
Handle invalid input and negative amounts.

class NegativeError(BaseException):
 try:
    amount=eval(input('Enter the amount :'))
    if amount>5000:
      discount=amount*0.2
      bill=amount-amount*0.2
      print(discount)
      print(bill)
    elif 2000<amount<=5000:
      discount=amount*0.1
      bill=amount-amount*0.1
      print(discount)
      print(bill)
    elif 0<amount<2000:
      print(amount)
    elif amount<0:
      print('Invalid')
    raise NegativeError
 except:
    print('Handle Value Error')



12.Square of a Number  (function Topic)
Create a function square(n) that returns the square of a number.
Handle invalid input using TypeError.

def square(n):
    return n**2
try:
 print(square(eval(input('Enter the number: '))))
except TypeError:
    print('Handle invalid input')
    


