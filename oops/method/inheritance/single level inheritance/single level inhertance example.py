1.single level inheritance:

*A single child class will inherit a property from a single parent class is called single level inheritance.

#-------------------------------------------example-------------------------------------------------------------#

class Dad:
   def spam(self):
       print("Dad's class")
class Child(Dad):
   def demo(self):
       print("Child class")
x=Child()
x.demo()#Child class
x.spam()#Dad's class
Child.spam(x)#Dad's class
Child.demo(x)#Child class
