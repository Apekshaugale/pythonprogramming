Q2. Bank Account
Create a class BankAccount:

Constructor takes holder_name and balance.
Class variable bank_name = "State Bank".
Instance method deposit(amount) → adds to self.balance.
Classmethod rename_bank(cls, new_name) →
changes bank_name for all accounts.
Staticmethod validate_amount(amount) → returns True only if amount > 0.

class BankAccount:
    bank_name = "State Bank"
    def __init__(self,holder_name,balance):
        self.hname=holder_name
        self.balance =balance
        
    def deposit(self,amount) :
        self.amount=amount
        self.balance+=self.amount
        print(self.balance)

    @classmethod
    def rename_bank(cls, new_name):
        cls.name=new_name
        print(cls.name)

    @staticmethod
    def validate_amount(amount):
        if amount >0:
            return 'Truee'
        else:
            return 'False'
b=BankAccount('jitu',50000)
b.deposit(5000)
b.rename_bank('sbi')
print(b.validate_amount(5000))

o/p:
    55000
sbi
Truee
