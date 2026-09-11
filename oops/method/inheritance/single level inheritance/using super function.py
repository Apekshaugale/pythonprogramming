class Dad:
   def show(self):
       print("method-->1")
class Child(Dad):
   def show(self):
       
       print("method-->2")
       super().show()
s=Child()
s.show()
Child.show(s)
o/p:
method-->2
method-->1
method-->2
method-->1
