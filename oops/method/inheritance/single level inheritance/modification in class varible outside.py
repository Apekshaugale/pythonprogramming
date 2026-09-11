class Dad:
   money=100
   def villa(self):
       print("Dad's villa")
class Child(Dad):
   name="Joy"
   def Study(self):
       print("No study")
x=Child()
print(x.money)#100
print(x.name)#Joy

x.money=2000
print(Dad.money)#100

x.money=2000
print(x.money)#2000

Dad.money=2000
print(x.money)#2000

Dad.money=2000
print(Dad.money)#2000
