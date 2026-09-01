'''
#1.
* * * *
* * * *
* * * *

for i in range(1,5):
    for j in range(1,5):
        print('*',end=' ')
    print()

#2.
1 1 1 1
1 1 1 1
1 1 1 1

for i in range(1,5):
    for j in range(1,5):
        print('1',end=' ')
    print()

#3.
1 2 3
1 2 3
1 2 3

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()

#4.
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4

for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print()


#5.
*
* *
* * *
* * * *

for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')
    print()


#6.
1
1 2
1 2 3
1 2 3 4

for i in range(1,5): 
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#7.
1
2 2
3 3 3
4 4 4 4

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=' ')
    print()



#8.
*
* *
* * *
* * * *
* * * * *

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

#9.
* * * *
* * *
* *
*

for i in range(5,1,-1):
    for j in range(1,i):
         print('*',end=' ')
    print()
        

#10.
1 2 3 4
1 2 3
1 2
1

for i in range(4,1,-1):
    for j in range(1,i):
        print(j,end=' ')
    print()


#11.
4 4 4 4
3 3 3
2 2
1

for i in range(4,0,-1):
    for j in range(1,i):
        print(i,end=' ')
    print()


#12.
1
2 3
4 5 6
7 8 9 10
'''

for i in range(1,5):
    for j in range(1,i+1):
        print(num,end=' ')
        num += 1
    print()

