'''

13.show me the 3 examples of nested try and except block

1.Accept two numbers from the user and perform division. Use a nested try-except block to handle:

Invalid numeric input using ValueError
Division by zero using ZeroDivisionError


try:
  a=eval(input('Enter the number:'))
  b=eval(input('Enter the number:'))
  
  try:
     print(a/b)
  except ZeroDivisionError:
      print("Handle ZeroDivisionError")
except :
    print("Handle ValueError")



13. Nested Try-Except — Example 2

Question:
Create a list of 5 elements. Ask the user to enter an index and divide the selected
element by a number entered by the user. Use nested try-except blocks to handle:

Invalid index using IndexError
Invalid numeric input using ValueError
Division by zero using ZeroDivisionError

try:
 a=eval(input('enter the list:'))
 i=eval(input('enter the index :'))
 
 try:
    print(a[i])
    try:
        print(i/a[i])
    except:
        print('Zero division Error')
 except:
     print("ValueError")
except:
    print("IndexError")


3.Question:
Create a simple student marks program. Accept marks for three subjects and calculate the average.
Use nested try-except blocks to handle:

Non-numeric marks using ValueError
Marks outside the range 0–100 by raising ValueError
Any other unexpected error using an outer except block
These three cover the main pattern of nested exception handling:
an inner try-except handles a
specific operation, while the outer try-except handles
errors that occur outside or escape the inner block.

try:
  s1=eval(input('enter the student1 marks:'))
  s2=eval(input('enter the student2 marks:'))
  s3=eval(input('enter the student3 marks:'))
  avg=(s1+s2+s3)/3
  print(avg)
  
except:
    print('ValueError.')


14.show me the 3 examples combination of try and except and else and finally block

try:
  a=eval(input('Enter the number:'))
  b=eval(input('Enter the number:'))
  
  try:
     print(a/b)
  except ZeroDivisionError:
      print("Handle ZeroDivisionError")
except :
    print("Handle ValueError")
else:
    print('condition satified')
finally:
    print('proper')
'''


'''

15. show one userdefined error ------->>>MockError

class MockError (BaseException):
        print('User defined error')
def num(n):
    try:
            if n>0:
                print('positive number')
            else:
                raise MockError

    except MockError:
        print('Handle MockError')
    else:
        print('Mock Error is not arises')
    finally:
        print('Done')
        
num(eval(input('Enter the number:')))    

3.Question:
Create a simple student marks program. Accept marks for three subjects and calculate the average.
Use nested try-except blocks to handle:

Non-numeric marks using ValueError
Marks outside the range 0–100 by raising ValueError
Any other unexpected error using an outer except block
These three cover the main pattern of nested exception handling:
an inner try-except handles a
specific operation, while the outer try-except handles
errors that occur outside or escape the inner block.

class ValueError(BaseException):
 try:
 
  s1=eval(input('enter the student1 marks:'))
  s2=eval(input('enter the student2 marks:'))
  s3=eval(input('enter the student3 marks:'))
  avg=(s1+s2+s3)/3
  print(avg)
  try:
      if 0<s1<100:
          print('valid')
     
      if 0<s2<100:
          print('valid')
      if 0<s3<100:
          print('valid')
      else:
          raise ValueError
        
  except:
      print('ValueError')
 except:
    print('ValueError.')

'''

        
