Only Positional arguments(/)
"""
"""
Before the forward slash if we Pass only Positional
arguments it will work properly.
but Before the forward slash if we Pass keyword arguments
it will show syntax error but after the  forward slash
we can Pass Positional or keyword arguments it will
work.

def demo(a,b,/,c):
    print(a,b,c)
demo(1,2,3)
demo(1,2,c=3)
demo(1,2,c=3)
"""
"""
only keyword arguments (*)

Here Before the * symbole we can Pass both
Positional and keyword arguments but after the
* symbole only we can Pass keyword argumnets.

def demo(a,b,*,c):
    print(a,b,c)

demo(1,b=10,c=90)
demo(1,10,c=90)
demo(1,10,90) Typeerror
"""
"""
combination of / and *
def spam(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
spam(1,2,3,d=90,e=89)
spam(1,2,c=3,d=45,e=33)
spam(100,200,300,d=900,1000)
"""

"""
1.Positional arguments (-->)
2.keyword argumnets (--->)
3.only Positional arguments(/)
4.only keyword arguments(*)
5.combination of / and *
6.variable Positional argumnets(*args)(--->)
7.variable keyword argumnets(**kwargs) (--->)
8.combination of *args and **kwargs (--->)
"""
'''
#6.variable Positional argumnets(*args)(--->)
def spam(*args):
    # print(args)  #Packed format
    print(*args)  #unPacked format
spam()
spam(1)
spam(1,2,3,4,5)
spam("abc",[1,2,3],True,False,{567,90},{5:9})

ex-->2
def check(*python):
    print(*python)
check()
check(90,100,200)
check([1,2,3,4],{90,23},8+9j)
'''

'''
# 7.variable keyword argumnets(**kwargs) (--->)
def check(**kwargs):
    print(kwargs)
check()
check(a=90)
check(a=90,b=23,c=True,d={34,56},e=[1,2,3],f="Hii")
check(a1=90)
print()

def check(**kwargs):
    print(*kwargs)
check()
check(a=90)
check(a=90,b=23,c=True,d={34,56},e=[1,2,3],f="Hii")
check(a1=90)

print()

def check(**sql):
    print(*sql)
check()
check(a=90)
check(a=90,b=23,c=True,d={34,56},e=[1,2,3],f="Hii")
check(a1=90)
'''
'''
# 8.combination of *args and **kwargs (--->)
def Data(*args,**kwargs):
    print(*args,*kwargs)
Data()
Data(11,12)
Data(110,120,a=90,b=99)
