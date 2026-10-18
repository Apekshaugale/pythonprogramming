#reduce is a function:
#it is not a inbuild class so we will not perform typecasting

#so i have to import my reduce function
#from functools import tool

#no need to typecasting

#always reduce function always give one single value 

#always take two argument

from functools import reduce
1.# def sum(a,b):   
#     return a+b
# g=[1,4,5,6]
# res=reduce(sum,g)  
#if i do likeres=reduce(sum,g,100) (function name,var,initializer)
# print(res)

#2.
def grt(a,b):
    if a>b:
        return a
    else:
        return b
a=[10,45,75,97,45,677]
res=reduce(grt,a)
print(res)