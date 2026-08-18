#Wap to reverse the given number.
'''
num = input('Enter the number: ')
i = len(num) - 1
while i >= 0:
    print(num[i], end='')
    i -= 1
#Wap to find the sum of individual digits of a number.
sum=0
num=input('Enter the number')
i=0
while i<len(num):
    sum=sum+int(num[i])
    i+=1
print(sum)



#Wap to check whether the number is perfect or not.
i = 1
fact = 0
num = int(input('Enter the number : '))
while i < num:
    if num % i == 0:
        fact = fact + i
    i += 1
if fact == num:
    print('Perfect number.')
else:
    print('Not a perfect number.')


#Wap to login to phonepe by entering correct otp.
Opt = 1234
i = 0
while i < 3:
    opt = int(input('Enter the OTP: '))
    if opt == Opt:
        print('Login success')
        break
    else:
        print('Incorrect OTP')
    i += 1

    '''
#Wap to run infinite loop until user enters the correct password.

#Wap to extaract all the even integers present in a tuple at odd index.

#Wap to remove duplicates from a list without converting into set.

#Wap to find the sum of all the odd numbers between the given range.

#Wap to find the greatest number in a given list of integers.

#Wap to find the sum of cube of a number in a string.

#Wap to check whether the number is Armstrong or not
