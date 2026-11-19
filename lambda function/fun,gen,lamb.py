# 1. Function Tasks (4)
# Task 1. Check Even or Odd
# Basic
# What to do:
# 1. Create a function named check_number().
# 2. Accept one number as an argument.
# 3. Check whether the number is even or odd.
# 4. Return "Even" or "Odd".
# Expected output:
# EvenOdd
def check_number(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
print(check_number(6))



# Task 2. Find the Largest Number
# Basic
# What to do:
# 1. Create a function named largest().
# 2. Accept three numbers as arguments.
# 3. Find the largest number without using max().
# 4. Return the largest number.
# Expected output:
# largest(10, 25, 15)25
def largest(a,b,c):
    if a>b and a>c:
        return "a greater"
    elif  b>a and b>c:
        return "b greater"
    else:
        return "c greater"
print(largest(10, 25, 15))   


# Task 3. Calculate Factorial
# Intermediate
# What to do:
# 1. Create a function named factorial().
# 2. Accept one number.
# 3. Calculate its factorial using a loop.
# 4. Return the result.
# Expected output:
# factorial(5)120
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))

# Task 4. Function with Multiple Arguments
# Intermediate
# What to do:
# 1. Create a function named calculate().
# 2. Accept any number of numerical arguments using *args.
# 3. Calculate the sum of all numbers.
# 4. Calculate their average.
# 5. Return both results.
# Expected output:
# calculate(10, 20, 30, 40)Sum = 100Average = 25.0
def calculate(*args):
     a=sum(args)
     b=len(args)
     c=a/b
     return c
print(calculate(10, 20, 30, 40))



# 2. Generator Tasks (4)
# Task 5. Generate Numbers
# Basic
# What to do:
# 1. Create a generator function named numbers().
# 2. Generate numbers from 1 to 10.
# 3. Use the yield keyword.
# 4. Print the generated values using a loop.
# Expected output:
# 12345678910



# Task 6. Generate Even Numbers
# Basic
# What to do:
# 1. Create a generator function named even_numbers().
# 2. Accept a number n.
# 3. Generate all even numbers from 1 to n.
# 4. Use yield instead of return.
# Expected output:
# even_numbers(10)246810



# Task 7. Generate Squares
# Intermediate
# What to do:
# 1. Create a generator function named square().
# 2. Accept a number n.
# 3. Generate the square of numbers from 1 to n.
# 4. Use yield to produce each square.
# Expected output:
# square(5)1491625



# Task 8. Fibonacci Series Using Generator
# Challenge
# What to do:
# 1. Create a generator function named fibonacci().
# 2. Accept the number of terms.
# 3. Generate the Fibonacci series.
# 4. Use yield to return each term.
# 5. Do not use a list to store the series.
# Expected output:
# fibonacci(7)0112358




# 3. Lambda Function Tasks (4)
# Task 9. Square of a Number
# Basic
# What to do:
# 1. Create a lambda function named square.
# 2. Accept one number.
# 3. Return its square.
# Expected output:
# square(5)25



# Task 10. Find the Largest of Two Numbers
# Basic
# What to do:
# 1. Create a lambda function named largest.
# 2. Accept two numbers.
# 3. Return the larger number.
# 4. Do not use the max() function.
# Expected output:
# largest(20, 30)30



# Task 11. Sort Tuples Based on Second Element
# Intermediate
# What to do:

# 1. Create the following list:
# data = [(1, 50), (2, 20), (3, 40), (4, 10)]



# 2. Use sort() or sorted().
# 3. Use a lambda function as the key.
# 4. Sort the tuples based on their second element in ascending order.
# Expected output:
# [(4, 10), (2, 20), (3, 40), (1, 50)]



# Task 12. Filter Positive Numbers
# Challenge
# What to do:

# 1. Create a list:
# numbers = [-10, 20, -5, 30, 0, -15, 40]



# 2. Use filter().
# 3. Use a lambda function to check whether a number is positive.
# 4. Convert the filter result into a list.
# Expected output:
# [20, 30, 40]