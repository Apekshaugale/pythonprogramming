# def eve(n):
#     if n%2==0:
#         return True
#     else:
#         return False
a=[10,12,20,1,21,31,41,14,55,52]
# res=filter(eve,a)
# print(list(res))

res=filter(lambda x:x%2==0,a)
print(list(res))
