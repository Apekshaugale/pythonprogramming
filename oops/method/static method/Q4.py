Q4. Product Inventory
Create a class Product:

Constructor takes name, price, quantity.
Class variable tax_rate = 18.
Instance method total_price() → returns price * quantity plus tax
(using self. and class var).
Classmethod update_tax(cls, new_rate) → changes tax_rate globally.
Staticmethod apply_discount(price, discount_percent) →
returns discounted price (pure calculation, no self/cls).

class Product:
    tax_rate = 18
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def total_price(self):
        total=((self.price*self.quantity)+self.tax_rate)
        return total

    @classmethod
    def update_tax(cls, new_rate):
        cls.tax_rate=new_rate
        print(cls.tax_rate)

    @staticmethod
    def apply_discount(price, discount_percent):
        return price-(price*discount_percent/100)
p=Product('Sita',45000,5)
print(p.total_price())
p.update_tax(25)
print(p.apply_discount(45000, 10))
