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
'''
#wap to print  multiplication of n natural numbers
n=int(input('Enter the number :'))
i=1
mul=1
while i<=n:
    mul=mul*i
    i=i+1
print(mul)
    
'''

#for collection data type use always condition while i<len(collection):
'''
#wap to fetch lower case character from string
s=str(input('Enter the String : '))
out=' '
i=0
while i<len(s):
    if s[i].islower():
        out=out+s[i]
    i+=1
print(out)
'''
'''
#wap to print uppercase ,lowercase,digit ,special caharcter
s=str(input('Enter the string :'))
upper=' '
lower=' '
digit=' '
special=' '
i=0
while i<len(s):
    if s[i].isupper():
        upper=upper+s[i]
    elif s[i].islower():
        lower=lower+s[i]
    elif s[i].isdigit():
        digit=digit+s[i]
    else:
        special=special+s[i]
    i+=1
print(upper)
print(lower)
print(digit)
print(special)
'''
'''
#in given list do addition of intiger value
a=[10,4j+8,'ape','DON',45,90,'di']
sum=0
i=0
while i<len(a):
    if isinstance(a[i],int):
        sum=sum+a[i]
    i+=1
print(sum)
'''

#wap to fetch str value from list only if len >3
s=list(input('Enter the list : '))
i=0
string=' '
while i<len(s):
    if type(s[i])==str and len(s[i])>3:
        string=string+s[i]
    i+=1
print(string)

'''
#wap to add of ascii value of special char in a string
a=str(input('Entre the string : '))
i=0
add=0
while i<len(a):
    if not  a[i].isalnum():
        add=add+ord(a[i])
    i=i+1
print(add)
'''

