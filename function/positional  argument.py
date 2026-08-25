'''# 1.Positional argument.
def demo(a,b,c):
    print(a,b,c)
demo(1,5,6)
#number odf paraments are always equal to number of argumne  else it show error.


# 2.keyword argument.
#syntax---->
#parameter=argument

def demo(a,b,c):
    print(a,b,c)
demo(a=1,b=5,c=6)

#if i use demo(2,5,1)---->it will acts like a positional argumnet.
#positonal arg always foloow the keyword argumnet
#keyword it won't follow  positinal


#postional +keyword it will working but keyword+posional won't work






#wap to check given no is even

a=10
def even(a):
    if a%2==0:
       print('even')
    else:
         print('odd')
even(10)
o/p:
even


def even_odd():
    num=int(input('Enter the the number :'))
    if num%2==1:
       print('odd')
    else:
         print('even')
even_odd()
op:
Enter the the number :4
odd


#wap to check the given program is palindrome
s='level'
if s==s[::-1]:
        print('palindrome')
else:
        print('not')

def palindrome(s):
    if s==s[::-1]:
        print('palindrome')
    else:
        print('not')
palindrome('level')


def palindrome():
    name=eval(input('Enter the string: '))
    if name==name[::-1]:
        print('palindrome')
    else:
        print('not')
palindrome()
o/p:
Enter the string: 'level'
palindrome


s=[1,2,3,4]
for i in s:
 if i%2==0:
     print(i)

o/p:
2
4

def name(s): 
  for i in s:
      if i%2==0:
         print(i,end=' ')
name([1,2,3,4])

o/p:
2
4


d=['hii','walmart','xyz','good','onoff']
for i in d:
    if len(i)%2==0:
        print(i)
    else:
        print(i[::-1])

o/p:
iih
tramlaw
zyx
good
ffono


def evenodd(d):
    for i in d:
      if len(i)%2==0:
        print(i)
      else:
        print(i[::-1])
evenodd(['hii','walmart','xyz','good','onoff'])

o/p:
iih
tramlaw
zyx
good
ffono


#key==char value =ord(char)

s='Hello'
d={}
for i in s:
    d[i]=ord(i)
print(d)

o/p:
{'H': 72, 'e': 101, 'l': 108, 'o': 111}


def dictinory(s):
   d={}
   for i in s:
    d[i]=ord(i)
   print(d)
dictinory('Hello')

o/p:
{'H': 72, 'e': 101, 'l': 108, 'o': 111}




d=[1,45,45,True,False,999]
for i in d:
    if isinstance(i,bool):     or  if type(i)==bool:
        print(i)

o/p:
    True
    False

def typ(d):
    for i in d:
        if isinstance(i,bool):
            print(i)
typ([1,45,45,True,False,999])

o/p:
    True
    False


#wap to seperate the data type 
e=[90,True,3.5,9+4j,'abc',[1,2,3],{56,78}]
a=[]
b=[]
for  i in e:
    if isinstance(i,(int,float,bool,complex)):
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)

o/p:
[90, True, 3.5, (9+4j)]
['abc', [1, 2, 3], {56, 78}]

def sep(e):
    individual=[]
    collection=[]
    for i in e:
        if isinstance(i,(int,float,bool,complex)):
            individual.append(i)
        else:
            collection.append(i)
    print('individual data type :',individual)
    print('collection data type',collection)
sep([90,True,3.5,9+4j,'abc',[1,2,3],{56,78}])

o/p:
individual data type : [90, True, 3.5, (9+4j)]
collection data type ['abc', [1, 2, 3], {56, 78}]

'''


