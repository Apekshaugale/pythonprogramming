Static Method 

#A static method is a type of method in a class that does not take self (object reference) or cls (class reference) as its first parameter.


#It behaves just like a normal function, but it belongs to a class’s namespace.


#It is defined using the @staticmethod 



#A static method does not depend on the class or instance — it is independent.


#It is useful when you want to write utility/helper methods inside a class.


#You can call a static method using:
1. class name

#The object reference
 (but no extra implicit arguments are passed).


#Static methods can accept arguments, but those must be passed explicitly by the caller.

#Unlike instance methods and class methods, static methods cannot access or modify class-level or instance-level attributes directly.


syntax:
-------
class ClassName:
    @staticmethod
    def fun1():
        ...
ClassName.fun1()
    (or)
c = ClassName()
c.fun1()
