# print([j+i for i in range (1,4) for j in range (1,4)])

# a=[[10,20],[30,40],[50,60]]
# # o/p:
# # [10,20,30,40,50,60] flatten a nested list

# # for i in a:
# #     for j in i:
# #         print(j)

# print([j for i in a for j in i])

# print([i[0]+i[1] for i in a ])

# z=[10,5,25,30,40,15,20]
# for i in z:
#     for j in z:
#         if sum([i,j])==30:
#             print(i,j)

# print([(i,j) for i in z for j in z if sum([i, j]) == 30])

a=[100,200,350,450]
#o/p:
#[1000,900,750,650]

print([sum(a)-i for i in a ])