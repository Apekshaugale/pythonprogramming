-------------Consturctor overriding-------------------
class Parent:
   def __init__(self):
       print("constructor class 1")


class Child(Parent):
   def __init__(self):
       super().__init__()
       print("constructor class 2")
c=Child()

o/p:
constructor class 1
constructor class 2
