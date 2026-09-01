'''#wap to generate only the string with odd length in given list
#l=["alexa","siri","google","cortrena"]
def odd(Input):
    for i in Input:
        if len(i)%2==1:
            print(i)
odd(["alexa","siri","google","cortrena"])
o/p:
    alexa
    
def odd(Input):
    for i in Input:
        if len(i)%2==1:
            yield i
print(list(odd(["alexa","siri","google","cortrena"])))
O/p:['alexa']

#wap to create a list of numbers if number are even square it else cube it
#l=[2,3,4,5,6,7]
def squ(Input):
    even=[]
    odd=[]
    for i in Input:
        if i%2==0:
            even.append(i**2)
            
        else:
            odd.append(i**3)
    print('Even :',even)        
    print('Odd',odd)
squ([2,3,4,5,6,7])
o/P;
Even : [4, 16, 36]
Odd [27, 125, 343]


def squ(Input):
    even=[]
    odd=[]
    for i in Input:
        if i%2==0:
            even.append(i**2)
            
        else:
            odd.append(i**3)
    yield ('Even :',even)        
    yield ('Odd',odd)
print(list(squ([2,3,4,5,6,7])))

O/p:
    [('Even :', [4, 16, 36]), ('Odd', [27, 125, 343])]
'''
'''
#wap to return a list if words is of even length reverse it
#l=["hello","world","python","apple","google","walmart"]
def fun(Input):
    for i in Input:
        if len(i)%2==0:
            yield i[::-1]
        else:
            yield i
print(list(fun(["hello","world","python","apple","google","walmart"])))
O/p:
    ['hello', 'world', 'nohtyp', 'apple', 'elgoog', 'walmart']
'''
#wap to generate the first letter of the word as key and words starting with letter as value
#s="python is a programming language and programming is part of life"
#output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]
def fun(s):
    d = {}
    s = s.split()
    for i in s:
        if i[0] not in d:
            d[i[0]] = [i]
        else:
            d[i[0]].append(i)
    return d
print(fun("python is a programming language and programming is part of life"))

#wap to generate a list if it is individual data type
#reverse it else keep it as it is
#l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]

def ind(l):

 for i in l:
     if isinstance(i,(int,float,bool)):
         yield ( str(i)[::-1])
     else:
        yield( i)
print(list(ind(["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36])))

o/p:
    ['flipkart', 'Amazon', '87', [2, 3, 4], '87', '78.9', (5, 3), '63.54']
