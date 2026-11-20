"""Level 1: Easy – Basic While Loop (1-10)
Write a Python program to print numbers from 1 to 10 using a while loop.

i=1
while i<=10:
    print(i)
    i=i+1

Write a program to print numbers from 10 to 1 in reverse order.

i=10
while i>=1:
    print(i)
    i=i-1


Write a program to print all even numbers from 1 to 50.

i=1
while i<=50:
    if i%2==0:
        print(i)
    i=i+1


Write a program to print all odd numbers from 1 to 50.

i=1
while i<=50:
    if i%2==1:
        print(i)
    i=i+1


Write a program to print the multiplication table of a given number.

a=eval(input("Enter the number :"))
i=1
while i<=10:
    print(a*i)
    i=i+1


Write a program to find the sum of numbers from 1 to N.

a=eval(input("Enter the number :"))
add=0
i=1
while i<=a:
    add+=i
    i=i+1
print(add)


Write a program to find the product of numbers from 1 to N.

a=eval(input("Enter the number :"))
add=1
i=1
while i<=a:
    add*=i
    i=i+1
print(add)



Write a program to count how many numbers are divisible by 5 between 1 and 100.

count=0
i=1
while i<=100:
    if i%5==0:
        count+=1
    i=i+1
print(count)


Write a program to print all numbers divisible by both 3 and 5
between 1 and 100.

i=1
while i<=100:
    if i%3==0 and i%5==0:
        print(i)
    i=i+1




Write a program to calculate the average of numbers from 1 to N."""
count=0
add=0
a=eval(input("Enter the number :"))
i=1
while i<=a:
    count=count+1
    add+=i
    i=i+1
print(add/count)
