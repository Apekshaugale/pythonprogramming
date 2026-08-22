'''
bal=eval(input('Enter the balance :'))
if bal>0:
    print(f'the balance is {bal}')

num=str(input('Enter the string :'))
if num==num[::-1]:
    print('Palindrome ')
else:
    print('not')

a=153
total=0
c=str(a)
b=len(str(a))
for i in c:
    total=total+int(i)**b
if total==a:
        print('armstrog')
else:
        print('not')

num=eval(input('Enter the number : '))
for i in range(1,11):
    
        print(i*num)
    


num=6
a=[]
b=0
for i in range(1,6):
   i%2==0
   a.append(i)
   b=b+i
if num==b:
    print('perfect')
else:
    print('not')

num=6
a=[]
b=0
for i in range(1,6):
    
  if  i%2==0:
    a.append(i)
    b=b+i
if num==b:
    print('perfect')
else:
    print('not')

s='hello'
for i in enumerate(s):
    print(i)
print(list(enumerate(s)))
a='hell'
for i in reversed(a):
    print(i,end=' ')
print(tuple(reversed(a)))

for i in sorted(a):
    print(i,end=' ')
    
for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

a='hel'
b='elh'
if sorted(a)==sorted(b):
    print('anagram')
else:
    print('not')

a=153
total=0
c=str(a)
power=len(c)
for i in c:
    total=total+int(i)**power
if total==a:
    print('Armstrong')
else:
    print('Not armstrong')


a=[20,30]
d={}
for i in a:
        d[i]=chr(i)
print(d)
'''
a=[23,45]
dict.fromkeys(a)
print(a)
