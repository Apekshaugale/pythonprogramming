#number from 10 to 1
"""
i=10
while i>=1:
    print(i,end=' ')
    i=i-1

    
#cube of number from 1 to 5
i=1
while i<=5:
    print(i**3,end=" ")
    i=i+1
    

#sum of number all even number from 1 to 10
sum=0
i=1
while i<=10:
    if i%2==0:
      sum+=i
    i=i+1
print(sum)
   

#find sum odd n from 1 to n
sum=0
a=eval(input("enter the number:"))
i=1
while i<=a:
    if i%2==1:
        sum+=i
    i=i+1
print(sum)


#table of 5
i=1
while i<=10:
    print(i*5)
    i=i+1

#sum from 1 to 5

a=0
i=1
while i<=5:
    a+=i
    i=i+1
print(a)

#square from 1to 5
i=1
while i<=5:
    print(i*i)
    i=i+1

#count no divsible by 5 between 1 to 100
count=0
i=1
while i<=100:
    if i%5==0:
     count+=1
    i=i+1
print(count)


#print no divisible by 3 and 5 between 1 to 100
i=1
while i<=100:
    if i%3==0 and i%5==0:
        print(i)
    i=i+1
  
#factor of given no
num=eval(input("Enter the number"))
i=1
while i<=num:
    print(i+num())
"""
#calcualte power of no withut using the **operator

#count no of digit of givrn no
#find sum of digit of given no
