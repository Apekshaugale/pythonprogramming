2.Create a class Bank with attribute balance.
 Create a child class SavingsAccount with methods:
deposit()
withdraw() 

class Bank:
    def bal(self):
        self.balance=5000
        print(f'current balance is {self.balance}')
class SavingsAccount(Bank):
    def deposite(self):
        self.deposite=200
        self.balance+=self.deposite
        print(f'current balance is  after deposite {self.balance}')
    def withdraw(self):
        self.withdraw=100
        self.balance-=self.withdraw
        print(f'current balance is after withdraw {self.balance}')
s=SavingsAccount()
s.bal()
s.deposite()
s.withdraw()
o/p:
current balance is 5000
current balance is  after deposite 5200
current balance is after withdraw 5100

class Bank:
    def bal(self,balance):
        self.balance=balance
        print(f'current balance is {self.balance}')
class SavingsAccount(Bank):
    def deposite(self,deposite):
        self.deposite=deposite
        self.balance+=self.deposite
        print(f'current balance is  after deposite {self.balance}')
    def withdraw(self,withdraw): 
        self.withdraw=withdraw
        self.balance-=self.withdraw
        print(f'current balance is after withdraw {self.balance}')
s=SavingsAccount()
s.bal(6000)
s.deposite(100)
s.withdraw(200)
o/p:
current balance is 6000
current balance is  after deposite 6100
current balance is after withdraw 5900


