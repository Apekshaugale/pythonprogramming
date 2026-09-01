'''#wap to generate a+b,a-b,a*b,a/b by taking a and b from user

def operation():
    a=int(input('Enter the number :'))
    b=int(input('Enter the number :'))
    yield a+b
    yield a-b
    yield a*b
    yield a/b
print(list(operation()))#execute at a time in list format output
#Enter the number :5
#Enter the number :5
#[10, 0, 25, 1.0]
for i in operation(): #execute one by one unpacked format at a time 
    print(i)
#Enter the number :8
#Enter the number :6
#14
#2
#48
#1.3333333333333333

x=operation()
print(next(x))#first operation perform hold next operation
#Enter the number :9
#Enter the number :4
#13
print(next(x))
print(next(x))
print(next(x))
print(next(x)) #StopIteration


#wap to generate only values which are divisible by 5
#l=[34,55,60,56,78,90,25,40]
def div(Input):
    for i in Input:
        if i%5==0:
            yield i
#print(div([34,55,60,56,78,90,25,40]))
x=div(([34,55,60,56,78,90,25,40]))
print(next(x))  #55
print(next(x))  #55 60
print(next(x)) #55 60 90
print(next(x)) #55 60 90 25
print(next(x))#55 60 90 25 40
print(next(x))#StopIteration




#wap to return a iterator which is having square root of values present in the list
#l=[25,36,49,81,9,16]
def squ(Input):
        for i in range(1,11):
            if i**2 in Input:
                    print(i)
squ([25,36,49,81,9,16])

o/p:
3
4
5
6
7
9

def squ(Input):
        for i in range(1,11):
            if i**2 in Input:
                    yield i
print(list(squ([25,36,49,81,9,16])))

o/p:[3, 4, 5, 6, 7, 9]

#wap to return a iterator having tuples of word and its len pair and typecast into dictionary
#l=["instagram","facebook","whatsapp","meta","oracle"]
def dic(Input):
    d={}
    for i in Input:
        d[i]=len(i)
    print(d)
dic(["instagram","facebook","whatsapp","meta","oracle"])
o/p:
{'instagram': 9, 'facebook': 8, 'whatsapp': 8, 'meta': 4, 'oracle': 6}

def dic(Input):
    #d={}
    for i in Input:
        #d[i]=len(i)
     yield i ,len(i)
print(dict(dic(["instagram","facebook","whatsapp","meta","oracle"])))

O/p:
{'instagram': 9, 'facebook': 8, 'whatsapp': 8, 'meta': 4, 'oracle': 6}

#wap to generate only numeric values in given list
#l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
def num(numeric):
    for i in numeric:
        if isinstance(i,(int,float)):
            print(i)
num(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])
O/p:
78
78
9.87
45.36

def num(numeric):
    for i in numeric:
        if isinstance(i,(int,float)):
            yield i
print(list(num(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])))
O/p:
    [78, 78, 9.87, 45.36]
  


#wap to generate a list if it is individual data type reverse it else return as it is
#l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
def ind(rev):
    for i in rev:
        if isinstance(i,(str,list,tuple,dict)):
            print(i[::-1],end=' ')
        else:
            print(i,end=' ')
ind(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])
O/p:
    trakpilf nozamA 78 [4, 3, 2] 78 9.87 (3, 5) 45.36
'''
def ind(rev):
    for i in rev:
        if isinstance(i,(str,list,tuple,dict)):
            yield i[::-1]
        else:
            yield i
print(list(ind(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])))
O/p:
    ['trakpilf', 'nozamA', 78, [4, 3, 2], 78, 9.87, (3, 5), 45.36]
'''
