Q5. BankAccount → SavingAccount → SeniorSavingAccount
Create a class BankAccount to store account holder name and balance.
Create a class SavingAccount that adds an interest rate and calculates interest.
Create a class SeniorSavingAccount that adds age and gives 1% extra interest
if the age is greater than or equal to 60. Display the final interest.
'''
class BankAccount:
    def __init__(self,hname,balance):
        self.hname=hname
        self.balance=balance
    def demo(self):
        print(f'The holder name is {self.hname} and balance is {self.balance}')
        

class SavingAccount(BankAccount):
    def __init__(self,hname,balance, interest):
        super().__init__(hname,balance)
        self.interest=interest
        self.calculate=self.balance*self.interest
    def demo(self):
        super().demo()
        print(f'The interest rate is {self.interest}')
        print(f'The calculated interest is {self.calculate} ')
#s=SavingAccount("RAmu",50000,0.1)
#s.demo()
class SeniorSavingAccount(SavingAccount):
    def __init__(self,hname,balance, interest,age):
        super().__init__(hname,balance, interest)
        self.age=age
    def demo(self):
        super().demo()
        if self.age>=60:
             self.calculate=self.balance+(self.balance*0.1)
             print(f'The  person age is greater than 60 then they gets total amount is {self.calculate}')
        else:
           print(f"Age is less than 60")
s=SeniorSavingAccount("Ra+mu",50000,0.1,65)
s.demo()

o/p:
The holder name is Ra+mu and balance is 50000
The interest rate is 0.1
The calculated interest is 5000.0 
The  person age is greater than 60 then they gets total amount is 55000.0

