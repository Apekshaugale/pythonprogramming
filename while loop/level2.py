"""Level 2: Intermediate - Number-Based Programs (11-20)
Write a program to count the number of digits in a given number.

count=0
a=eval(input("Enter the number :"))
while i<=

Write a program to find the sum of digits of a given number.

Write a program to find the product of digits of a given number.

Write a program to reverse a given number.

Write a program to check whether a given number is a palindrome.

a=str(input("Enter te string:"))
b=""
for i in a:
    b+=i
    if b==a:
        print("Palindrome")
    

a = input("Enter the string: ")
b = ""
i = 0
while i < len(a):
    b = a[i] + b
    i += 1
if a == b:
    print("palindrome")
else:
    print("Not palindrome")


Write a program to find the first and last digits of a number.
"""
a = eval(input("Enter the string: "))
i=1
while i<=str(len(a)):
    num=a%10
    print(num)
    c=a//10
    print(c)
    i+=1
"""
Write a program to find the largest digit in a given number.

Write a program to find the smallest digit in a given number.

Write a program to count the number of even and odd digits in a given number.

Write a program to check whether a number is an Armstrong number."""
