'''#find factor of given nuber .
num=eval(input('Enter the number : '))
i=1  #initialization
out=[] #temparoty variable
while i<=num: 
    if num%i==0:
        out.append(i)
    i+=1
print(out)

'''
'''
#perfect number(6 che factors 1,2,3 and thier sum  1+2+3=6 that means 6 is a perfect number)
num=eval(input('Enter the number : '))
i=1
a=[]
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
        a.append(i)
    i+=1
print(a)
print(sum)
        

#facrorial
num=6
a=[]
i=1
while i<num:
    if num%i==0:
        a.append(i)
    i+=1
print(i)

#prime number number which is divsible by 1 and itself only.
num=eval(input('Enter the number : '))
i=1
b=[]
while i<=num:
    if num%i==0:
        b.append(i)
    i+=1
if len(b)==2:
        print('Prime number .')
else:
        print('The number is not a prime')



num=eval(input('Enter the number : '))
i=1
while i<=num:
  if num%i==0:
        print('prime number ')
  else:
        print('Not an prime number')
    i+=1
'''
'''
#armstrong number

num=eval(input('Enter the number : '))
i=0
total=0
a=str(num)
power=len(a)
while i<len(a):
        total=total+int(a[i])**power
        i+=1
    
if total==num:
        print('its armstrong')
else:
        print('its not a armstrong')


num=eval(input('Enter the number : '))
dum=num
st=str(num)
b=len(st)
out=0
while num>0:
    last_digit=num%10
    out=out+last_digit**b
    num=num//10#increment
if out==dum:
    print('Armstrong')
else:
    print('Not armstrong')


#digerium num=135=5^3(index postion=3),3^2(index position of 3=2),1^1(index postion of 1=1)
num=eval(input('Enter the number : '))
a=num
b=len(str(num))
temp=0
while num>0:
    lastdigit=num%10
    temp=temp+lastdigit**b
    num=num//10
    b=b-1
if temp==a:
    print('Digerium')
else:
    print('Not digerium')
    

#perfect number 

num=eval(input('Enter the number :'))
i=1
sum=0
while i<num:
 if num%i==0:
    sum=sum+i
 i+=1
if sum==num:
  print(f'The given number  {num} is perfect')
else:
  print(f'The given number {num}  is not a perfect number')

'''
'''
num=eval(input('Enter the input rows : '))
#range contains start and end
for i in range(1,num+1):
    for j in range(1,num+1):
        print('*',end=' ')
    print()
'''

a=70
for i in range(65,a+1,1):
    for j in range(65,i+1,1):
        print(chr(i),end=' ')
        
        
    print()

