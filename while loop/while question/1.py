# Wap to login to phonepe by entering correct otp.

'''
otp = 1123
while True:
    Otp = eval(input('Enter the Otp : '))
    if otp == Otp:
        print('Login Success')
        break
    else:
        print('Incorrect OTP')

o/p:Enter the Otp : 1123
Login Success
        
# Wap to run infinite loop until user enters the correct password.
pin = 1123
while True:
    passward = eval(input('Enter the passward : '))
    if pin != passward:
        
        continue
    else:
        print('correct password')
        break

o/p:Enter the passward : 132
Enter the passward : 1234
Enter the passward : 1123
correct password


# Wap to extaract all the even integers present in a tuple at odd index.
a=(1, 12, 2, 3,12,8)
i=0
while i<len(a):
    if a[i]%2==0 and i%2==1:
        print(a[i])
    i+=1
o/p:12
8

# Wap to remove duplicates from a list without converting into set.
a=[5,55,8,6,5,'hello','hi','hello',55]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
        
    i+=1
print(b)

o/p:[5, 55, 8, 6, 'hello', 'hi']

# Wap to find the sum of all the odd numbers between the given range.
a=[5,55,8,6,5,55]
i=0
sum=0
while i<len(a):
    if a[i]%2==1:
        sum=sum+a[i]
    i+=1
print(sum)

o/p:120

a=eval(input('Enter the range of numbers :' ))
i=0
sum=0
while i<len(a):
    if a[i]%2==1:
        sum=sum+a[i]
    i+=1
print(sum)

o/p:Enter the range of numbers :[465,45,44,98]
510

# Wap to find the greatest number in a given list of integers.
a = [5, 55, 8, 6, 5, 55]
i = 0
greatest = a[0]
while i < len(a):
    if a[i] > greatest:
        greatest = a[i]
    i += 1
print(greatest)

o/p=55

# Wap to find the sum of cube of a number in a string.
sum=0
a=[10,20,55,87,47,45]
i=0
while i<len(a):
    b=a[i]**3
    sum=sum+b
    i+=1
print(sum)


 '''   
# Wap to check whether the number is Armstrong or not.
# Wap to check whether the number is Armstrong or not.

a = input('Enter the number : ')
i = 0
sum = 0

while i < len(a):
    sum = sum + int(a[i]) ** 3
    i += 1

if sum == int(a):
    print('armstrong')
else:
    print('not armstrong')

o/p=Enter the number : 153
armstrong
