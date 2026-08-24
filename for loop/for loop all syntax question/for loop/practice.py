#armstrong
a=153
b=str(a)
c=len(b)
total=0
for i in b:
    total=total+int(i)**c
if total==a:
    print('Anagram')
else:
    print('not')

num=eval(input('Enter the number : '))
count=0
for i in range(1,num+1) :
    if num%i==0:
        count=count+1
        print(i)
if count==2:
          print('prime ')
else:
            print('not')
    
  
num=eval(input('Enter the number : '))
a=[]
for i in range(1,num+1) :
    if num%i==0:
        a.append(i)
print(a)


num=6
a=0
for i in range(1,num) :
    if num%i==0:
        a=a+i
     
if num==a:
    print('perfect')
else:
    print('not ')
