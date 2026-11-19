#lambda examples// Anonymous function

# 1.wap to find square and cube of given number
var=lambda n:n**2
print(var(3))

# 2.wap to check the given number is palindrome or not
ele=lambda b:"palindrome" if b==b[::-1] else "not"
print(ele("mom"))
# 3.wap to convert negative number to positive number
# num=lambda a: abs(a)
# print(num(eval(input("Enter the nuber:"))))
# # 4.wap to return the key of a dictionary
#a={"hello":"Sony","How":"are","you":"bye"}
dic=lambda a:a.keys()
print(dic({"hello":"Sony","How":"are","you":"bye"}))

# 5.wap to check if the number is even or odd
# num=lambda a:"even" if a%2==0 else "odd"
# print(num(eval(input("enter the number:"))))

# 6.wap which returns first element of a sequence
first=lambda n:n[0]
print(first([10, 20, 30]))

# 7.wap which returns length of any iterable
length=lambda a:len(a)
print(length([10, 20, 30]))
print(length("hjej"))

# 8.wap which returns the list of squares of numbers in a list
# l=[2,3,4,5,6]


squ = lambda lst: [a ** 2 for a in lst]
print(squ([2,3,4,5,6]))

# 9.wap to check list elements are palindrome or not
# l=["nayana","kayak","mom","school","bag","dad"]
lst=lambda ele:[i for i in ele if i==i[::-1]]
print(lst(["nayana","kayak","mom","school","bag","dad"]))

# 10.wap to print the numbers present in a list with their corresponding indices pair
# l=[100,200,300,400,500]
num=lambda a:[i for i in enumerate(a) ]
print(num([100,200,300,400,500]))

# 11.wap to check a data is sequence if it is sequence then return length pair else type pair
check=lambda a: len(a) if isinstance(a,(str,tuple,list)) else type(a)
print(check("helo"))
print(check(123))

# 12.wap to check given number is divisible by 5 and 3
# num=lambda n: "dividible" if n%3==0 and n%5==0 else "not divisible"
# print(num(eval(input("enter the number:"))))

# 13.wap to check even or odd,if it is even return square of that value else square root of that 
# value
# num=lambda e:e**2 if e%2==0 else e**0.5
# print(num(eval(input("enter the number:"))))

# 14.wap to check len of given string ,if length is even return as it is else return reverse
# of that string
string=lambda a: a if len(a)%2==0 else a[::-1]
print(string("leveq"))

# 15.wap to check length of given string and return value and length in tuple and dictionary


# 16.wap to check a data is sequence if it is sequence then return length pair else type pair
seq=lambda a: len(a) if isinstance(a,(str,list,tuple)) else (a, type(a))
print(seq(12))

# 17.wap to return if no is divisible by 5 then increment with 5 else decrement with 5
num=lambda a:a+5 if a%5==0 else a-5
print(num(12))
# """

