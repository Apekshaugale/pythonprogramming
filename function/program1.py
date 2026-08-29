#1. Greeting Function
#Write a function that takes a name and prints:
#Hello Amit



#2. Add Two Numbers
#Write a function that takes two numbers and returns their sum.
#Input: 10, 20
#Output: 30


#3. Find Difference
#Write a function that accepts two numbers and returns their difference.

#4. Find Maximum
#Write a function that accepts two numbers and returns the greater number.

#5. Find Minimum
#Write a function that accepts two numbers and returns the smaller number.

#6. Check Even or Odd
#Write a function that accepts a number and returns "Even" or "Odd".




#7. Check Positive, Negative or Zero
#Write a function that accepts a number and returns:
#Positive
#Negative
#Zero


#8. Square a Number
#Write a function that accepts a number and returns its square.
#Input: 5
#Output: 25

#9. Cube a Number
#Write a function that accepts a number and returns its cube.

#10. Find Last Digit
#Write a function that accepts a number and returns its last digit.
#Input: 12345
#Output: 5

#11. Find First Digit
#Write a function that accepts an integer and returns its first digit.
#Input: 45678
#Output: 4

#12. Calculate Area of Rectangle
#Write a function that accepts length and breadth and returns the area.
#Area = length × breadth
'''
def area():
    length=int(input('Enter the length : '))
    b=int(input('Enter the breadth : '))
    return length *b
print(area())

def area():
    l=int(input('Enter the length : '))
    b=int(input('Enter the breadth : '))
    print(l*b)
area()


#13. Calculate Simple Interest
#Write a function that accepts:
#principal
#rate
#time
#and returns simple interest.
#SI = (P × R × T) / 100
def SI():
    p=int(input('Enter the p : '))
    r=int(input('Enter the R : '))
    t=int(input('Enter the T : '))
    print(p*r*t/100)
SI()
'''
'''
#14. Find Average of Three Numbers
#Write a function that accepts three numbers and returns their average.
def avg(a,b,c):
    return (a+b+c)/3
print(avg(10,20,30))
'''    
'''
#15.Count Vowels
#Write a function that accepts a string and returns the number of vowels.
#Input: "education"
#Output: 5

def edu(Input):
    count=0
    for i in Input:
        if i in 'aeiou':
            count+=1
    print(count)
edu('education')

'''
    
'''
#16.Count Consonants
#Write a function that accepts a string and returns the number of consonants.
def edu(Input):
    count=0
    for i in Input:
        if i not in  'aeiou':
            count+=1
            print(i)
    print(count)
edu('education')

def edu(Input):
    count=0
    for i in Input:
        if i not in 'aeiou':
            return i
print(edu('education'))
'''
'''
#17. Count Digits in a String
#Write a function that accepts a string and counts how many digits are present.
#Input: "abc123xy5"
#Output: 4
def digit(dig):
    count=0
    sum=0
    for i in dig :
        if i.isdigit():
            count+=1
            sum=sum+int(i)
            print(i)
    print('count is =',count)
    print('sum of number is =',sum)
digit('abc123xy5')

o/p:
1
2
3
5
count is = 4
sum of number is = 11
'''
'''
#18.. Reverse a String
#Write a function that accepts a string and returns the reversed string.
#Input: "python"
#Output: "nohtyp"

def string(Input):
    for i in Input:
        return Input[::-1]
print(string('pyhton'))

def string(Input):
    
        print( Input[::-1])
string('pyhton')

o/p:
nothyp

'''

'''
 #9.Return Only Positive Numbers
#Write a function that accepts a list and returns a new list containing only positive numbers.
#a = [10, -5, 20, -2, 30]
def pos(num):
    a=[]
    for i in num:
        if i>0:
            a.append(i)
    print(a)
pos([10, -5, 20, -2, 30])

def pos(num):
    a=[]
    for i in num:
        if i>0:
            a.append(i)
    return a
print(pos([10, -5, 20, -2, 30]))
o/p:
[10, 20, 30]
'''
'''
#20.wap to perform addition and subtraction if "a" is greater than "b" return
#sum else return difference
def operation(a,b):
    if a>b:
        return a+b
    else:
        return a-b
print(operation(50,80))
print(operation(100,80))
o/p:
-30
180
'''
'''
#21.waf to check string is palindrome or not (take user input)
def pal(n):
    rev=''
    for i in n:
        rev= i+rev
    if rev == n:
        
        print(' palindrome')
    else:
        print("n p")
    
pal('level')         
      
'''
'''
#22.wap to return length of variable keywords arguments
def length_data(**kwargs):
    length=0
    for i in kwargs:
       length+=1
    print(length)
length_data(a=10,v=23,d=789)



length=0
def length_data(**kwargs):
    global length
    for i in kwargs:
       length+=1
    print(length)
length_data(a=10,v=23,d=789)
o/p:
3
'''
'''
#24.waf to search for character in a given string and return corresponding index
#string="coding part is done"


def check(string,sub):
    return string.index(sub)
e=check(string='coding part is done',sub='d')
print(e)

def data(string):
    sub=eval(input('enter the substring:'))
    for i in range(len(string)):
        if string[i]==sub:
            return sub,i
        return 'substring not found'
a=data('coding part is done')
print(a)

o/p:
2
enter the substring:'c'
('c', 0)


#25.wap to squaring of the element in the given list
#l=[1,2,3,4,5]
def square(input):
    a=[]
    for i in input:
        a.append(i**2)
    print(a)
square([1,2,3,4,5])
    
o/p:
[1, 4, 9, 16, 25]
'''
'''
#26.wap to fetch last digit number
def num():
    number=eval(input('Enter the number :'))
    print(number%10)
num()

def num():
    number=eval(input('Enter the number :'))
    return number%10
print(num())
'''
'''
#27.wap to read 3 numbers from the user,first two numbers should be added and the result of addition should be subtracted by third number
def three():
    n1=eval(input('Enter the number :'))
    n2=eval(input('Enter the number :'))
    a= n1+n2
    n3=eval(input('Enter the number :'))
    return a-n3
print(three())

o/p:
Enter the number :12
Enter the number :12
Enter the number :12
12

def three():
    n1=eval(input('Enter the number :'))
    n2=eval(input('Enter the number :'))
    a= n1+n2
    n3=eval(input('Enter the number :'))
    print(a-n3)
three()
o/p:
Enter the number :12
Enter the number :6
Enter the number :12
6
'''
'''
#28.wap to find square,cube,square root and cube root of a number
def num():
    n1=eval(input('Enter the number :'))
    return n1**2, n1**3,n1**(1/2),n1**(1/3)
print(num())
'''
'''
#29.wap to check the given characters is alphabets or digit or special characters
def char():
    a=eval(input('Enter the charcater :'))
    if a.isalpha():
        print('character')
    elif a.isdigit():
        print('digit')
    else:
        print('special character')
char()
o/p:
Enter the charcater :'a'
character

'''
'''
#30.wap to check given iterable is a sequence,if it is a sequence reverse it,if not add one extra element to the iterable
def num(input):
    a=[]
    for i in input:
        if isinstance(i,(str,list,tuple)):
            print( i[::-1])
        else:
            a.append(i)
    print(a)
num([123,'hello',{789,44,34},[1,3,4]])

o/p:
olleh
[4, 3, 1]
[123, {34, 44, 789}]
'''
'''
#31.write a function to print the below output
#func("TRACXN",1)
#should print RCN
def even(input):
    for i in range(1,len(input),2):
        print(input[i],end='')
even('TRACXN')    

#32.write a function to print the below output
#func("TRACXN",0)
#should print TAX
def function(input):
    for i in range(0,len(input),2):
        print(input[i],end='')
    
function('TRACXN')       
            
'''
'''
#33.A function take variable number of positional arguments
#   as input. how to check if the arguments are more than 5.
def num(*args):  
    if len(args)>5:
        print('length is greater than 5')       
num(3,4,5,789,3,45,67)     
o/p:
length is greater than 5


#34.waf to return a dictionary with characters and ascii value pair
def num(value):
    a={}
    for i in value:
        a[i]=ord(i)
    print(a)
num('sunday')

o/p:
{'s': 115, 'u': 117, 'n': 110, 'd': 100, 'a': 97, 'y': 121}
'''
'''
#35.wap to reverse a iterable if you are passing string or list or tuple else print type of the data
def iterable(value):
    for i in value:
      if isinstance(i,(list,str,tuple)):
          print(i[::-1])
      else:
           print(type(i))
iterable([12,345,'hello',[2,34,4],{23,4,5}])
'''
'''
#36.wap to check if a given character is alphabet or digit or special character (without using inbuilt function).
def check(character):
    if chr(97)<=character<=chr(122) or chr(65)<=character<=chr(90):
        print('character')
    elif chr(45)<=character<=chr(57):
        print('digit')
    else:
        print('special character')
check('5')        
'''
'''
#37.wap to return length of an iterable without using len() function
def length(value):
    count=0
    for i in value:
        count+=1
    print(count)
length([1,2,3,4,5])
'''
#38.wap to count the number of arguments passed inside the function call(both positional and keyword)


        
