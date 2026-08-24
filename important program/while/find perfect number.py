#perfect number(number divisible by given number and its sum is equal to the given number)
#perfect number(number divisible by i )
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



#perfect number(6 che factors 1,2,3 and thier sum  1+2+3=6 that means 6 is a perfect number)


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
    
    