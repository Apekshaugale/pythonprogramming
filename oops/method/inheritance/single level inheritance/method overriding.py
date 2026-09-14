#-----------method overriding------------------------------------------------------
#child class has a method with the same name and same parameters:
class Dad:
   def spam(self):
       print("Dad's class")
class Child(Dad):
   def spam(self):
       print("Child class")
x=Child()
x.spam()#Child class
Child.spam(x)#Child class
