'''#Wap to print python for 5 times.
i=1
while i<=5:
    print('Python')
    i+=1


#Wap to print n natural numbers.
num=eval(input('Enter the number : '))
i=1
while i<=num:
    print(i,end=' ')
    i+=1

#Wap to print multiplication table for n.
num=eval(input('Enter the number : '))
i=1
while i<=10:
    print(i*num)
    i+=1

#Wap to run infinite loop until user enters the correct password.

passward='hello'

while True:
    Pass=input('Enter the passward : ')
    if Pass==passward:
        print('Entered correct passward .')
        break
o/p=Enter the passward : jfg
Enter the passward : 'hello'
Enter the passward : 'hello'
Enter the passward : hello
Entered correct passward .

#Wap to find the sum of n natural numbers.
i=1
sum=0
num=eval(input('Enter the number : '))
while i<num+1:
    sum=sum+i
    i+=1
print('Sum is =',sum)

o/p:Enter the number : 10
55


#Wap to find the product of n natural numbers or factorial of a number.
i=1
mul=1
a =[ ]
num=eval(input('Enter the number : '))
while i<=num:
    mul=mul*i
    a.append(mul)
    i+=1
print(mul)
print(a)

o/p:Enter the number : 5
120
[1, 2, 6, 24, 120]



#Wap to print all the characters of a string.
i=0
s=eval(input('Enter the number : '))
while i<len(s):
    print(s[i])
    i+=1
o/p:Enter the number : 'string'
s
t
r
i
n
g



#Wap to print all the characters present at even index of a string.
i=0
s=eval(input('Enter the number : '))
while i<len(s):
    if i%2==0:
      print(s[i],end=' ')
    i+=1

o/p:Enter the number : 'string'
s r n 
    


#Wap to extract all the lowercase characters present in a string.
i=0
s=eval(input('Enter the string : '))
while i<len(s):
    if s[i].islower():
        print(s[i])
    i+=1
o/p:Enter the number : 'fjkAERTDYF'
f
j
k



#Wap to extract all the vowels present in a string
i=0
s=eval(input('Enter the string : '))
while i<len(s):
    if s[i] in 'aeiouAEIOU':
        print(s[i])
    i+=1

o/p:Enter the string : 'fjkAERTDYF'
A
E



#Wap to print factors of a integer 

i=1
fact=[]
num=eval(input('Enter the number : '))
while i<=num:
    if  num % i == 0:
      fact.append(i)
      print(fact)
    i+=1

o/p:Enter the number : 5
[1]
[1, 5]

'''

'''
#Wap to toggle a string.
i=0
s=eval(input('Enter the string :'))
while i<len(s):
    if ord('a')<ord(s[i])<ord('z'):
        print()



#Wap to reverse the given number.
s=eval(input('Enter the number :'))
i=0
while i<len(s):
    print(a[::-1])
    i+=1
'''

#Wap to find the sum of individual digits of a number.



