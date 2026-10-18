# #  FILTER


# # *filter is an inbuilt class which is used to filter default values.

# # *it will accept only 2 arguments that are "function and iterable".

# # *if the function is returned o/p as default value then it will filter that input.

# # *if the function is not returning any default value then it will keep the input.

# # *the output of the filter will be object format.
 
# # syntax:
# # -------
# # filter(function_name, iterable)

# # note:
# # -----
# # *no need of specifying map() class when we use filter, because filter itself only passes the input to function.
# # ""

# 1.wap to return a list having only even values

# l=[4,3,5,6,7,8,10]
# def name(n):
#     if n%2==0:
#       return n
#     else:
#       return 0
# l=[4,3,6,7,8,10]
# res=filter( name,l)
# print(list(res))

# a=[4,3,6,7,8,10]
# res=filter(lambda x:x%2==0,a)
# print(list(res))

# 2.wap to return a list having only flowers
# def flower(n):
#     if n.endswith("flowers"):
#           return n
#     else:
#         return 0
#l=["sun flowers","banana tree","lily flowers","lotus flowers","marigold flowers"]
# res=filter(flower,l)
# print(list(res))

# res=filter(lambda n:n.endswith("flowers"),l)
# print(list(res))

# 3.wap to return a list having elements which are starting with consonants
# def cons(n):
#     if n[0] not in ('a','e','i','o','u'):
#           return n
#     else:
#         return 0
# l=["hello","guys","please","respond","to","insta","computer"]
# res=filter(cons,l )
# print(list(res))

# 4.waf to build a list with only even length strings using filter

#k=["apple","google","walmart","fb","insta","act","zomato"]


# 5.waf to return only positive values in the list using filter

# m=[-5,-6,9,-34,90,-28,78,100,89,45,-65]

def low(a,i=0,res=''):
    if i>len(a):
        return res
    if a[i].islower():
        res=res+a[i]
    return low(a,i+1,res)
print(low("HELLo"))