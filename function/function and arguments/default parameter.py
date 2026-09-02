'''
#default parameter
def joy(x=2,y=3,z=6):
    print(x,y,z)
joy()
joy(5)
joy(10,11,23)
joy (1,2)



#positional args
def  demo(a,b,c):
    print(a,b,c)
demo(5,8,8)
#demo()   #error
#demo(4)   #error
#demo(4,5)   #error


#keyword

def  demo(a,b,c):
    print(a,b,c)
demo(a=5,b=8,c=8)


#only posional (/)
def  demo(a,b,/,c):
    print(a,b,c)
demo(5,5,c=8)
# demo(5,a=5,c=8)------Error
demo(12,15,31)




#only keyword(*)
def  demo(a,b,*,c):
    print(a,b,c)
demo(5,5,c=8)
#demo(5,5,5)     ----->error
demo(a=3,b=10,c=0)
#demo(a=3,b=10,0)  ----->error


#combination of / and *
def  demo(a,b,/,c,d,*,e):
    print(a,b,c,d,e)
demo(5,5,c=2,d=4,e=50)
demo(2,3,4,5,e=9)
'''
def  demo(a,b,c):
    print(a,b,c)
demo(5,8,c=8)
