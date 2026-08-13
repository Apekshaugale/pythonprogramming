#while loop:
'''
Aset of instruction/block of code while willl execut repeatedly  untilll the condition is satisfied

Syntax:
     initilization
     while  <condition>:
               statement block/logic
                updation



if updation is skip then the loop will be converted to infinite loop.
'''

'''                                  [ START ]
                                              |
                      --------->[  While condition    ]--------->False------------  |
                      |                        |                                                                |
                                               |                                                                |
                      |                  [ True ]                                                          |
                                              |                                                                 |
                      |                       |                                                                 |
                      -----------[statement block /logic ]---------------------[Stop]


'''
'''

#wap to print 'idli vada' for 5 times

i=0
while i<5:
    print('idli vada')
    i=i+1
    
#wap to print from 1 to 10
i=1
while i<=10:
    print(i,end=' ')
    i=i+1
    
#wap to print reverse from 1 to 10
i=10
while i>=1:
    print(i,end=' ')
    i=i-1
'''
'''
#wap to print even number from 1 to 10
i=1
while i<=10:
    if i%2==0:
        print(i,end=' ')

        '''
'''
#wap to print sum of n natural number
n=int(input('Enter the number : '))
i=1
add=0
while i <=n:
    add=add+i
    i=i+1
print(add)
'''

#wap to print  multiplication of n natural numbers
n=int(input('Enter the number :'))
i=1
mul=1
while i<=n:
    mul=mul*i
    i=i+1
print(mul)
    

