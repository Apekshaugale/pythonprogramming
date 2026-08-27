#3.only positional argument
# symbol(/)frowars slash

#Before the forward slash if we passs only positional argument it will work proprly .
#but before forward slash if we pass keyword argumnet it will show syntax error but after forward slash
#we can pass posional as well as keyword argument anything you can used.




#     before /  only                            <---- [ / ]---> after
#        positional  argument                                            /  any positional or keyword argument
                                                                   




#what is difference between / and *

#4.only ketword argument (*)
'''


before *   keyword or                     <---- [ * ]---> after only 
        positional  argument                                            *   keyword argument
        

'''


'''
#5.combination of / and *


def demo(a,d,/,v):
    print(a,d,v)
demo(1,5,v=5)
demo(a=1,4,5)   #error

#6.variable positional args(*args)
#we can pass n number of vaues

def demo(*args) :   #it is aproperty
    print(args)
demo(1,4563,1,2)


#difference between posional args nad variable position args

'''


#7keyword arguments
(var-name==value)



