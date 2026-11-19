#1.now()---->fetch current time of system 
# 2.%d------>Day
# 3.%m------>month number
# 4.%Y----->four-digit year
# 5.%y----->Two-digit year
# 6.%H------>24 hour format
# 7.%I------>12-hour format
# 8.%M------>Minutes
# 9.%s------>Seconds
# 10.%p----->AM/PM
# 11.%A------>Full weekday
# 12.%a------>short weekday
# 13.%B------>Full month
# 14.%b----->short month
# 15.%J----->Day of year

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

c=s.strftime("%A")
print(c)
# 11.%A------>Full weekday
# 12.%a------>short weekday
# 13.%B------>Full month
# 14.%b----->short month
# 15.%J----->Day of year
d=s.strftime("%a")
print(d)

d1=s.strftime("%B")
print(d1)

f=s.strftime("%b")
print(f)

e=s.strftime("%j")
print(e)
e=s.strftime("%m")
print(e)



#if yu want to create date
import datetime as d
w=d.date(2025,11,19)
print(w)

#how you are fetvhing microsedconds
