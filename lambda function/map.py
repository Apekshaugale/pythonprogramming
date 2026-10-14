# '''map can take any normal func inside it'''
# def mul(n):
#     print(n)
#     return n*2
# a=[10,20,3.3]
# res_var=map(mul,a)
# print(type(res_var))

# for i in res_var:
#     print(i)

# """lambda can be passed inside map function"""

# res=map(lambda n:n+5,eval(input('enter list:')))
# print(list(res))

# """map function  can multiple iterables"""

# def mul(x,y):
#     return x*y
# a=[10,20,30]
# b=[1,2,3]
# res=map(mul,a,b)
# print(list(res))

# def add(x,y):
#     return x+y
# a=[10,20,30,50,60]
# b=[1,2,3]
# res=map(add,a,b)
# print(list(res))

# def add(x,y):
#     return x+y
# a=[10,20,30,50,60]
# res=map(add,a)
# print(list(res)) #typeerror


# 1-->WAP TO FIND SQUARE OF ALL THE VALUES PRESENT BETWEEN THE RANGE(1 TO 5).
# a=[1,2,3,4,5]
# res=map(lambda x: x**2, a)
# print(list(res))

# def squ(n):
#     return n**2
# a=[1,2,3,4,5]
# res=map(squ,a)
# print(list(res))
# 2-->WAP TO FIND LENGTH OF EACH AND EVERY WORD PRESENT INSIDE THE GIVEN STRING.
# def string(n):
#     return len(n)
# a="My name is Apeksha"
# res=map(string,a.split())
# print(list(res))
# 3-->WAP TO GET THE FOLLOWING O/P:
# I/P='GOOD MORNING'
# O/P={'GOOD':4,'MORNING':7}

# def dictionary(n):
#     return (n, len(n))
# a = 'GOOD MORNING'

# res = map(dictionary, a.split())
# print(dict(res))

# 4-->WAP TO FIND FACTORIAL OF ALL THE NUMBERS PRESENT INSIDE THE GIVEN HOMOGENOUS LIST COLLECTION.
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# a=[1,2,3,4,5]
# res=map(fact,a)
# print(list(res))

# 5-->WAP TO GET THE FOLLOWING O/P
# I/P='PYTHON IS EASY'
# O/P={'PYTHON':'python', 'IS':'is', 'EASY':'easy'}
def string(n):
    return (n,n.lower())
a='PYTHON IS EASY'
res=map(string,a.split())
print(dict(res))

# 6-->wap to return if the key is individual returns its value else return its type
# d={10:"ten","hai":"value",(1,2,3):"colln",1.2:"decimal"}

# 7-->wap to create a list of 1st characters from each name
# names=["manu","lohit","jivago","wank","yaseen"]


# 8-->wap to return list of name and length pair
# names1=["laptop","mouse","board","house","week"]


# 9-->wap to print sum of indices from both list
# l1=[2,3,4,5,6]
# l2=[3,4,5,8,9]


# 10-->wap to make a pair of names and age
# names=["a","b","c","d"]
# age=[20,35,21,56]