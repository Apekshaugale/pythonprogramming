# import b
# # b.demo(4,6)
# b.a
# import module_name
# import module_name as alias_name
# from module_name import function_name
# from module_nmae import func1,func2
# from module_name import * (* will consider all the function name and variable)

import datetime #datetime is a module
print(datetime.datetime.now())#now is used to get current address

import datetime as dt
s=dt.datetime.now()
print(s)

#strftime will always accept one arg which is always present inside thw quotes
x=s.strftime("%Y")#4digit yr
print(x)

x1=s.strftime("%y")#short form of yera use small y
print(x1)

x2=s.strftime("%d")#print current day
print(x2)

x4=s.strftime("%m")#month no
print(x4)

x5=s.strftime("%H")#24hr format
print(x5)

x6=s.strftime("%I")#12hr format
print(x6)

x7=s.strftime("%M")#minutes
print(x7)

x9=s.strftime("%S")#sec
print(x9)

x10=s.strftime("%p")#am/pm
print(x10)

c=s.strftime("%A")#sec
print(c)

d=s.strftime("%a")#sec
print(d)

d1=s.strftime("%B")#sec
print(d1)

f=s.strftime("%b")#sec
print(f)

e=s.strftime("%j")#sec
print(e)

