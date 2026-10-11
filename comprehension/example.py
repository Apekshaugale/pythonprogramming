# 1. List Comprehension
# Q1. Write a list comprehension to print the squares of numbers from 1 to 10.
print([i**2 for i in range(1,11)])
# Q2. Write a list comprehension to print even numbers from 1 to 20.
print([i for i in range(1,21) if i % 2 == 0])
# Q3. Write a list comprehension to print odd numbers from 1 to 15.
print([i for i in range(1,16) if i % 2 != 0])
# Q4. Given a list [10, 20, 30, 40, 50], create a new list containing each number multiplied by 2.
a=[10, 20, 30, 40, 50]
print([i*2 for i in a ])
# Q5. Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only numbers greater than 5
print([i for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if i > 5])
# Q6. Given a list [12, 15, 20, 25, 30, 35, 40], create a new list containing numbers divisible by 5.
# Q7. Given a list [-5, 10, -2, 8, -9, 15], create a new list containing only positive numbers.
# Q8. Given a list [2, 4, 6, 8, 10], create a new list containing the square of each number.
# Q9. Given a list [1, 2, 3, 4, 5, 6], create a new list containing the cube of each number.
# Q10. Given a list [11, 22, 33, 44, 55, 66], create a new list containing numbers divisible by both 2 and 3.
# 2. String Comprehension
# Q11. Given the string "python", create a list containing each character.
# Q12. Given the string "education", create a list containing only the vowels.
# Q13. Given the string "Hello World", create a list containing only uppercase letters.
# Q14. Given the list ["apple", "banana", "kiwi", "mango"], create a new list containing words with more than 4 characters.
# Q15. Given the list ["python", "java", "sql", "html"], create a new list containing the length of each word.
# 3. Dictionary and Set Comprehension
# Q16. Create a dictionary using numbers from 1 to 5 as keys and their squares as values.
# Q17. Create a dictionary using numbers from 1 to 5 as keys and their cubes as values.
# Q18. Given the list [1, 2, 2, 3, 4, 4, 5, 5], use set comprehension to get unique numbers.
# Q19. Given the string "programming", use set comprehension to get unique characters.
# Q20. Given the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a dictionary where each even number is a key and its square is the value.