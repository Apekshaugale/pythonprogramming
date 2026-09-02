'''#wap to fetch str value from list only if len >3
s=eval(input('Enter the list : '))
i=0
string=' '
while i<len(s):
    if type(s[i])==str and len(s[i])>3:
        string=s[i]+' '+string
    i+=1
print(string)


#While loop programs

# 1,wap to print series of 20 natural numbers
i=1
while i<=20:
    print(i,end=' ')
    i+=1

# 2.wap to print series of upper case characters
#output:--.A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
i=65
while i<=90:
    print(chr(i),end=' ')
    i+=1



# 3.wap to print series of lower case characters
#output:-->a b c d e f g h i j k l m n o p q r s t u v w x y z
i=97
while i<=122:
    print(chr(i),end=' ')
    i+=1



# 4.wap to print both upper and lower case characters
#output:-A a B b C c D d E e F f G g H h I i J j K k L l M m N n O o P p Q q R r S s T t U u V v W w X x Y y Z z
i=65
while i<=90:
    print(chr(i),end=' ')
    print(chr(i).lower(),end=' ')
    i+=1


# 5.wap to print series of even numbers till 20 in reverse order  
#output:->20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1
i=20
while i>=1:
    if i%2==0:
        print(i,end=' ')
        i=i-2
   

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
        
     
# 7.wap to print even positional characters in the given string
#s="hello world"
#output:-->h l o w r d
s="hello world"
i=0
while i<len(s):
    if i%2==0:
        print(s[i],end=' ')
    i+=1

# 8.wap to display the position of the substring
s="hello world"
i=0
while i<len(s):
        if s[i]=='w':
            print('position of the substring',i)
        i+=1


#9.wap to print the number Table by using data given by user (take user input)
#expected output:-->2*1=2  2*2=4............2*10=20
num=eval(input('Enter the number : '))
i=1
while i<=10:
    print(num,'*',i,'=',i*num)
    i+=1


#10.wap to print the names only if the length of the names is even
l=["vaidegi","ashwini","patil","srinidhi","susmitha","rahul","priyanka","usha"]
i=0
while i<len(l):
    if len(l[i])%2==0:
        print(l[i],end=' ')
    i+=1



#11.wap to print the elements which in tuple, print only the if it is collection data types
values=(10,2.5,[10,20],"hero", True,(3,4,5),{2,7},{90:"super"})
i=0
while i<len(values):
    if isinstance(values[i],(tuple,str,list,dict,set)):
        print(values[i])
    i+=1


#12.wap to print the name which is starting with vowel in the given list
names=["agra","bangalore","mumbai","pune","indore","isha","eshwar","surat"]
i=0
while i<len(names):
  if names[i][0] in 'aeiouAEIOU':
      print(names[i],end=' ')
  i+=1


#13.wap to print sum of numbers in the list
l=[2,4,6,7,8,9]
sum=0
i=0
while i<len(l):
    sum=sum+l[i]
    i+=1
print(sum)


#14.wap to extract only vowels and digits from the given string
s="hellopython123"
i=0
while i<len(s):
    if s[i]  in  'aeiouAEIOU':
        print(s[i],end=' ')
    elif s[i].isdigit():
        print(s[i],end=' ')
    i+=1




#16.wap if a names ends with vowels then reverse a names else print its length
names=["Kumar","Lakita","Umesh","Priyanka"]
i=0
while i<len(names):
    if names[i][-1] in "aeiouAEIOU":
        print(names[i])
    i+=1


#17.wap to print all individual data type from list
data=[34,"hai",3+4j,(1,2),{3,4},False,3.4]
i=0
while i<len(data):
    if isinstance(data[i],(int ,float,bool,complex)):
        print(data[i])
    i+=1


#18.wap to print each characters from a string
s="python masters"
i=0
while i<len(s):
    print(s[i],end=' ')
    i+=1




# 6.wap to count numbers of occurrence of specified elements in the collection
#output:-->enter the character:-->o
#specified character is o and repeated time is 6
count=0
i=0
string=eval(input('Enter the string : '))
char=eval(input('Enter the character : '))
while  i<len(string):
    if string[i]==char:
        count=count+1
    i+=1
print(f'specified character is {char} and repeated time is',count)



# 7.wap to print even positional characters in the given string
#output:-->h l o w r d
i=0
string=eval(input('Enter the string : '))
while  i<len(string):
    if i%2==0:
        print(string[i],end=' ')
    i+=1


# 8.wap to print 2 different list and print even and odd numbers from 1-20
even=[]
odd=[]
i=1
while i<=20:
    if i%2==0:
       even.append(i)
    else:
        odd.append(i)
    i+=1
print('Even : ',even)
print('Odd : ',odd)

'''












                          
