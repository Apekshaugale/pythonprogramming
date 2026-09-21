2. Multilevel Inheritance   
Create a Python program using multilevel inheritance:
BankAccount = store holder name and balance.
SavingAccount = add interest rate and calculate interest.
SeniorSavingAccount = add age and give 1% extra interest
if age >= 60.
class 

class BankAccount:
    def __init__(self,name,balance):
        self.n=name
        self.balance=balance
    def person_info(self):
         #super().__init__()
         print(f"Person name is {self.n}\n"
               f"The account balance is {self.balance}")      
class SavingAccount(BankAccount):
    def __init__(self,name,balance,int_rate):
        super().__init__(name,balance)
        self.int_rate=int_rate
        self.calculate_interest=self.balance*self.int_rate
    def account_info(self):
        super().person_info()
        print(self.calculate_interest)
class SeniorSavingAccount(SavingAccount):
#(self,name,balance,int_rate,age):
    def demo(self,name,balance,int_rate,age):
       # super().__init__(name, balance, int_rate)
        self.age=age
        if self.age>60:
            self.calculate_interest=self.calculate_interest*0.1
            price=self.balance+self.calculate_interest
            print(price)
        else:
            print(self.calculate_interest)
s=SeniorSavingAccount("Apeksha",50000,0.2)
s.account_info()      
s.demo("Apeksha",50000,0.2,65)       
    
