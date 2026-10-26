from abc import ABC,abstractmethod
class SBI(ABC):
     #we can create constructor in parent class but we are not creating object parent we creae object of child
   @abstractmethod
   def __init__(self,HN,bal,acc_num):
    ...
   @abstractmethod
   def deposite(self,amount):
    ...
   @abstractmethod
   def withdraw(self,amount):
    ...
class ATM(SBI):
    def __init__(self,HN,bal,acc_num):
        self.name=HN
        self.bal=bal
        self.acc_num=acc_num
        print(self.name)
        print(self.bal)
        print(self.acc_num)
    def deposite(self,amount):
        print(f"Before deposite amount{self.bal}")
        self.bal+=amount
        print(f"After deposite amount is {self.bal}")
    def withdraw(self,amount):
        self.bal-=amount
        print(self.bal)
a=ATM("Ram",50000,12345678912)
a.deposite(2000)
a.withdraw(1000)




