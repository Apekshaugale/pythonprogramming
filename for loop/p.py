'''WAP to check whether the given number lies between 1 to 19, if it is true square
that number or else false cube that number and display the number.
num=eval(input('Enter the number : '))
if 1<=num<=19:
    print(num**2)
else:
    print(num**3)
o/p:
Enter the number :5
25
Enter the number :20
8000

WAP to check whether a given value is even and in range of 47 to 58 and not in 0
or odd. if condition is True, to perform display the ascii character. or else to
perform floor division with 5 and display it.
num=eval(input('Enter the number :'))
if num%2==0  and 90<=num<=122:
    print(chr(num))
else:
    print(num//5)

o/p:
Enter the number :98
b

WAP to check whether a given value is less than 125 and in between 47 to 125 or
not. if condition is True, to perform store the given value as key and value as a
character into the dict or else to append the value in list and display it.


num=eval(input('Enter the value :'))
d={}
l=[]
if 47<=num<=125 :
    d[num]=chr(num)
    print(d)
else:
    l.append(num)
    print(l)

o/p:
Enter the value :124
{124: '|'}

WAP to check whether the given string of the first character is a special symbol
or not. If a special symbol, to extract and display the middle character or else to
reverse the string and display the half of the string.
'''
s=eval(input('Enter the string :'))
mid=len(s)//2
if  not s[0].isalnum() :
   
    print(s[mid])
else:
    a=s[::-1]
    print(a[:mid:])
