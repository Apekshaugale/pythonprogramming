Q4. Product → Electronics → Mobile
Create a class Product with product_name and price. Create a class Electronics
that inherits from Product and adds warranty. Create a class Mobile that inherits
from Electronics and adds ram and storage. Use constructor chaining
and display all details.

class Product:
     def __init__(self,product_name,price):
         self.product_name=product_name
         self.price=price
     def  pinfo(self):
        print(f'The Product name is {self.product_name} and price is {self.price}')        
class Electronics(Product):
     def __init__(self,product_name,price,adds_warranty):
         super().__init__(product_name,price)
         self.adds_warranty=adds_warranty
     def einfo(self):
        super().pinfo()
        print(f'The adds_warranty is {self.adds_warranty}')

class Mobile(Electronics):
    def __init__(self,product_name,price,adds_warranty,ram ,storage):
        super().__init__(product_name,price,adds_warranty)
        self.ram=ram
        self.storage=storage
    def minfo(self):
        super().einfo()
        print(f'The ram is {self.ram} and storage is {self.storage}')
m=Mobile('Samsung',59000,"1year","8gb","1TB")
m.minfo()

o/p:
The Product name is Samsung and price is 59000
The adds_warranty is 1year
The ram is 8gb and storage is 1TB
