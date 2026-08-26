'''
#Palindrome number → 121 → same when reversed
num=int(input('Enter the number : '))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
if num==rev:
    print('palindrome')
else:
    print('Not a palindrome')
#Armstrong number → 153 → 1³ + 5³ + 3³ = 153
num=153
s=str(num)
cube=len(s)
total=0
for i in s:
    total=total+int(i)**cube
if total==num:
    print('Armstrong')
else:
    print('not armstrong')


num = int(input('Enter the number: '))
temp = num
n = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** n
    temp = temp // 10

if num == sum:
    print('Armstrong')
else:
    print('Not Armstrong')
#Perfect number → 6 → factors 1 + 2 + 3 = 6
num = int(input('Enter the number: '))
total = 0
for i in range(1, num):
    if num % i == 0:
        total = total+ i
if num == total :
    print('Perfect')
else:
    print('Not Perfect')

#Prime number → 7 → divisible only by 1 and 7
num = int(input('Enter the number: '))
total = 0
for i in range(1, num+1):
    if num % i == 0:
        total = total+ 1
if total == 2 :
    print('Prime')
else:
    print('not Prime')
'''
#Strong number → 145 → 1! + 4! + 5! = 145
num = int(input('Enter the number: '))
temp = num
sum = 0

for i in range(len(str(num))):
    digit = temp % 10

    fact = 1
    for j in range(1, digit + 1):
        fact = fact * j

    sum = sum + fact
    temp = temp // 10

if num == sum:
    print('Strong Number')
else:
    print('Not Strong Number')
#Duck number → 1023 → contains 0
num = input('Enter the number: ')
count = 0
for i in num:
    if i == '0':
        count = count + 1
if count > 0:
    print('Duck Number')
else:
    print('Not Duck Number')
#Disarium number → 135 → 1¹ + 3² + 5³ = 135
num = int(input('Enter the number: '))
temp = num
sum = 0
n = len(str(num))
for i in range(n):
    digit = temp % 10
    sum = sum + digit ** (n - i)
    temp = temp // 10
if num == sum:
    print('Disarium Number')
else:
    print('Not Disarium Number')
