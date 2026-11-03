# Function checklist
# 0 of 15 completed



# [ ] Task 1. Create a function that accepts two numbers and returns their sum.
# Expected: {t.out}
# Hint: Use two parameters and return a + b.
# def two(a, b):
#     return a + b
# print(two(3, 5))


# [ ] Task 2. Create a function that checks whether a number is even or odd.
# Expected: {t.out}
# def num(a):
#     if (a%2==0):
#         return "Even"
#     else:
#        return "odd"
# print(num(4))





# [ ] Task 3. Create a function that returns the square of a number.
# Hint: Multiply the number by itself.

# def square(num):
#     return num * num
# print(square(5)) 


# [ ] Task 4. Create a function that returns the factorial of a number.
# Hint: Use a loop and a variable initialized to 1.

# def fac(a,b=0,*args,c=0):
#     print(a*b*c)
# print(fac(2,3,4,5,6,c=7))



# [ ] Task 5. Create a function that accepts three numbers and returns the greatest.
# Hint: Compare the three numbers using if/elif/else.
# def three(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(three(3,5,7))



# [ ] Task 6. Create a function that checks whether a number is prime.
# Hint: Check divisibility from 2 up to the square root, or use a simple loop.
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(11))  # True


# [ ] Task 7. Create a function that counts the digits in an integer without converting it to a string.
# Hint: Repeatedly use // 10.
# def count_digits(n):
#    return len(str((n)))
# print(count_digits(12345))


# [ ] Task 8. Create a function that returns the reverse of an integer without converting it to a string.
# Hint: Use % 10 and // 10.




# [ ] Task 9. Create a function that accepts a number and returns the sum of its digits.

# Medium

# Expected: {t.out}

# Hint: Extract each digit using % 10.




# [ ] Task 10. Create a function that checks whether a number is a palindrome.

# Medium

# Expected: {t.out}

# Hint: Compare the original number with its reversed value.




# [ ] Task 11. Create a function that accepts a list of numbers and returns a new list containing only even numbers.

# Medium

# Expected: {t.out}

# Hint: Use a loop and append().




# [ ] Task 12. Create a function that accepts a number and returns all its factors.

# Medium

# Expected: {t.out}

# Hint: Loop from 1 to the number and check divisibility.




# [ ] Task 13. Create a function that accepts a list and returns the second-largest distinct number.

# Medium

# Expected: {t.out}

# Hint: Avoid counting duplicate values as separate numbers.




# [ ] Task 14. Create a function that accepts any number of positional arguments and returns their sum.

# Medium

# Expected: {t.out}

# Hint: Use *args.





# [ ] Task 15. Create a function that accepts another function and a number, then applies that function to the number.
# Hint: This is a higher-order function. Call the passed function inside it.


# def demo(**kwargs):
#     print(kwargs)
#     print(*kwargs)
# #demo()
# demo(a=10)


# def demo(*args):
#     print(args)
#     print(*args)
# #demo()
# demo(10)


# def demo(a,b,/,c):
#     print(a)
# demo(a=3,4,c=5)

#recursion
# def even(n):
#     if n==0:
#         return
#     even(n-1)#funcion calling(recusion calling)
#     if n%2==0:
#         print(n)
# even(10)


# def demo(n):
#     if n==0:
#         return
#     demo(n-1)
#     if n%2==1:
#         print(n)
# demo(10)

# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# print(sum(5)) 


#ask 1: Print even numbers from 2 to 10 using recursion.
# def even(n):
#     if n<=0:
#         return
#     even(n-1)
#     if n%2==0:
#         print(n)
# even(10)

#Print numbers from 1 to 10 using recursion.
# def num(n):
#     if n==0:
#         return
#     num(n-1)
#     print(n)
# num(10)


# Print numbers from 10 to 1 using recursion.
# def num(n):
#     if n == 0:
#         return

#     print(n)
#     num(n-1)

# num(10)



# Print all even numbers from 2 to 20.
# def even(n):
#     if n>20:
#         return n
#     if n%2==0:
#         print(n)
#     even(n+1)
# even(1)


# Print all odd numbers from 1 to 19.
# def odd(n):
#     if n>19:
#         return 
#     if n%2!=0:
#         print(n)
#     odd(n+1)
# odd(1)


# Find the sum of numbers from 1 to N.

# def sums(n): 
#     if n==0:
#         return 0
#     return n+sums(n-1)
# print(sums(5))

    


# Find the factorial of a number.

# def fact(n):
#     if n==1:
#         return 1
#     return n* fact(n-1)
# print(fact(5))


# Find the product of numbers from 1 to N.
# def product(n):
#     if n==1:
#         return 1
#     return n*product(n-1)
# print(product(5))



# Calculate the power of a number without using **.
# def power(a,b):
#     if b==0:
#         return 1
#     return a*power(a,b-1)
# print(power(2,3))


# Count the number of digits in a given number.
# def count(n):
#     if n==0:
#         return 0
#     return 1+count(n//10)
# print(count(12345))


# Find the sum of digits of a given number.
# def sum_digits(n):
#     if n==0:
#         return 0
#     return (n%10) + sum_digits(n//10)
# print(sum_digits(12345))