# def only_int(n,i=0,out=[]):
#     if i>=len(n):
#         return out
#     if type(n[i])==int:
#         out.append(n[i])
#     return only_int(n,i+1,out)
# print(only_int(eval(input('ENter the list :'))))


#to find the factor pf number if it is interger type 
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return n*fact(n-1) #recursion call
#we can call functiojn inside function
# def main(a,i=0,out=[]):#main function
#     if i>=len(a):#turmination condition
#          return out#to check value is intiger or not 
#     if type(a[i])==int and a[i]>0:
#         out.append(fact(a[i]))
#     else:
#         out.append(a[i])
#     return main(a,i+1,out)
# print(main(eval(input('Enter the list:'))))


#finfd that if the length of word is even then fetch lower case or id lengt is odd then fetch upper
# def even(n,i=0,out=''):
#     if i>=len(n):
#         return out
#     if n[i].islower():
#         out=out+n[i]
#     return even(n,i+1,out)
# def odd(n,i=0,out=''):
#     if i>=len(n):
#         return out
#     if n[i].isupper():
#         out=out+n[i]
#     return odd(n,i+1,out)
# def main(s,i=0,out={}):
#     b=s.split()
#     if i>=len(b):
#         return out
#     if len(b[i])%2==0:
#         out[b[i]]=even(b[i])#calling even function
#     else:
#         out[b[i]]=odd(b[i])
#     return main(s,i+1,out)
# print(main('HaI HeLLoO ApEKSha'))


#In=['hai',[34+j,True,78,9+2j],'sample',(3,7j+9),{19+20j,34,89},{'a':10},'data',[2+4j,3.8,7.9]]
# def string(n,i=0,out=''):
#     if i>=len(n):
#         return out
#     if type(n[i])==str:
#         out=out+n[i][::-1]
#     return string(n,i+1,out)
# def list(n,i=0,out=[]):
#     if i>=len(n):
#         return out
#     if type(n[i])==complex:
#         out.append(n[i])
#     return list(n,i+1,out)
# def dict(n,i=0,out={}):
#     if i>=len(n):
#         return out
#     if type(n[i])==complex:
#         out[n[i]]=n[i]
#     return dict(n,i+1,out)
# def set(n,i=0,out=set()):
#     if i>=len(n):
#         return out
#     if type(n[i])==complex:
#         out.add(n[i])
#     return set(n,i+1,out)
# def tuple(n,i=0,out=None):
#     if i>=len(n):
#         return out
#     if type(n[i])==complex:
#         out=n[i]
#     return tuple(n,i+1,out)
# def main(a,i=0,out=[]):
#     if i>=len(a):
#         return out
#     if type(a[i])==str:
#         out.append(string(a[i]))

#     elif type(a[i])==list:
#         out.append(list(a[i]))

#     elif type(a[i])==set:
#         out.append(set(a[i]))

#     elif type(a[i])==tuple:
#         out.append(tuple(a[i]))
#     elif type(a[i])==dict:
#         out.append(dict(a[i]))

#     return main(a,i+1,out)
# print(main(['hai',[34+5j,True,78,9+2j],'sample',(3,7j+9),{19+20j,34,89},{'a':10},'data',[2+4j,3.8,7.9]]))         



def string(n, i=0, out=''):
    if i >= len(n):
        return out

    if type(n[i]) == str:
        out = out + n[i][::-1]

    return string(n, i+1, out)


def list(n, i=0, out=[]):
    if i >= len(n):
        return out

    if type(n[i]) == complex:
        out.append(n[i])

    return list(n, i+1, out)


def dict(n, i=0, out={}):
    if i >= len(n):
        return out

    # Dictionary has keys and values.
    # Your input {'a':10} has no complex value,
    # so return empty dictionary.
    return dict(n, i+1, out)


def set(n, i=0, out=set()):
    if i >= len(n):
        return out

    if type(n[i]) == complex:
        out.add(n[i])

    return set(n, i+1, out)


def tuple(n, i=0, out=None):
    if i >= len(n):
        return out

    if type(n[i]) == complex:
        out = n[i]

    return tuple(n, i+1, out)


def main(a, i=0, out=[]):
    if i >= len(a):
        return out

    if type(a[i]) == str:
        out.append(string(a[i]))

    elif type(a[i]) == list:
        temp = list(a[i])
        if temp:
            out.append(temp)

    elif type(a[i]) == set:
        temp = set(a[i])
        if temp:
            out.append(temp)

    elif type(a[i]) == tuple:
        temp = tuple(a[i])
        if temp is not None:
            out.append(temp)

    elif type(a[i]) == dict:
        temp = dict(a[i])
        if temp:
            out.append(temp)

    return main(a, i+1, out)


print(main([
    'hai',
    [34+5j, True, 78, 9+2j],
    'sample',
    (3, 7j+9),
    {19+20j, 34, 89},
    {'a':10},
    'data',
    [2+4j, 3.8, 7.9]
]))