class Main:
    def __init__(self,name,age):
        self.name=name
        self.a=age
    def main1(self):
        print(self.name)
        print(self.a)
class Single(Main):
    def __init__(self,name,age,eid):
        super().__init__(name,age)
        self.eid=eid
        #Single.main2(self)
    def main2(self):
        #Main.main1(self)
        super().main1()
        print(self.eid)
class Multilevel(Main):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno=rollno
    def main3(self):
        super().main1()
        print(self.rollno)
class Child(Single,Multilevel):

    def __init__(self,name,age,eid,rollno,amount):
       super().__init__(name,age,eid)
       Multilevel.__init__(self,name,age,rollno)
       self.amount=amount
    def child(self):
        super().main2()
        Multilevel.main3(self)
        print(self.amount)



m=Child("Rohan",23,4,99,50000)
m.child()
