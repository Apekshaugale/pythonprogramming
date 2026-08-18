# 6.wap to count numbers of occurrence of specified elements in the collection
s = 'Hello guys Good morning python is a programming language'
count=0
i=0
while i<len(s):
    if s[i]=='o':
       count=count+1
    i+=1
print(count)

string=eval(input('Enter the data  : '))
element=eval(input('Enter the specified element : '))
i=0
while i<len(string):
    if string[i]==element:
        print(string.count(string[i]))
        break
    i+=1
#output---->
    6
Enter the data  : [10,20,30,10,20,10]
Enter the specified element : 20
2
