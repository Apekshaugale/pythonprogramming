'''class bank:
    def total_balance(self):
        self.amount=5000
        print(self.total_balance)
    def deposit(self,bal):
        self.amount+=self.bal
        print(self.deposit)
    def withdraw(self,bal):
        self.amount-=self.bal
        print(self.withdraw)
b=bank()
b.total_balance()
b.deposit(2000)
b.withdraw(1000)

'''
class flipkart:
    productname='car'
    cost=500
    totalproduct=4
    address='pune'
    def productdata(self):
        print(f'product name is {self.productname}')
        print(f'product cost is {self.cost}')
        print(f'product totalproduct  is {self.totalproduct}')
    def Address(self):
        print(f'current address is {self.address}')
        print()
    def Modificationdata(self,newcost,tp):#(self)
        self.cost=newcost
        #self.cost=6990
        self.totalproduct=tp
        print(f'Updated cost price is{self.cost}\n'f'Updated total product is{self.totalproduct}')
f=flipkart()
f.productdata()
f.Address()
f.Modificationdata(5000,7)
print(f.cost)#calling class varable #o/p:will be updated cost
print(f.totalproduct)#obj.varname
