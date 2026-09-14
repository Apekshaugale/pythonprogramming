'''class Teacher :
    def show(self):
        print('Teacher class')
class Student:
    def show(self):
        print('Student class1')
class Student2(Teacher.Student):
    def show(self):
        print('Student2')
s=Student2()
s.show()


'''
class Hotel:
    def __init__(self,hname,area,pin):
        self.hname=hname
        self.area=area
        self.pin=pin
    def Address(self):
        print(f'The hotel name is {self.hname}\n'
              f'The hotel area is {self.area}\n'
               f'The hotel pin is {self.pin}')
class Customer:
    def __init__(self,Cname,Tmember,Tbill,Ono):
        self.Cname=Cname
        self.Tmember=Tmember
        self.Tbill=Tbill
        self.Ono=Ono
    def data(self):
        print(f'The customer name is {self.Cname}\n'
              f'The total member is {self.Tmember}\n'
              f'The bill is {self.Tbill}\n'
              f'Order number is {self.Ono}')
class Review(Hotel,Customer):
    def __init__(self,rating,tipbill):
        super().__init__('Joy','Pune',444306)
        Customer.__init__(self,'Raju',8,5000,'Or:567')
        self.rating=rating
        self.tipbill=tipbill
    def Billdata(self):
        print(f'The rating is {self.rating}\n'
              f'The tip is {self.tipbill}')
r=Review('5*',500)
r.Address()
r.data()
r.Billdata()       

  #------------------------------------Muktiple inheritance----------------------------------------      
class Hotel:
    def __init__(self,hname,area,pin):
        self.hname=hname
        self.area=area
        self.pin=pin
    def Address(self):
        print(f'The hotel name is {self.hname}\n'
              f'The hotel area is {self.area}\n'
               f'The hotel pin is {self.pin}')
class Customer:
    def __init__(self,Cname,Tmember,Tbill,Ono):
        self.Cname=Cname
        self.Tmember=Tmember
        self.Tbill=Tbill
        self.Ono=Ono
    def data(self):
        print(f'The customer name is {self.Cname}\n'
              f'The total member is {self.Tmember}\n'
              f'The bill is {self.Tbill}\n'
              f'Order number is {self.Ono}')
class Review(Hotel,Customer):
    def __init__(self,rating,tipbill):
        super().__init__('Joy','Pune',444306)
        Customer.__init__(self,'Raju',8,5000,'Or:567')
        self.Address()
        self.data()
        self.Billdata()
        self.rating=rating
        self.tipbill=tipbill
    def Billdata(self):
        print(f'The rating is {self.rating}\n'
              f'The tip is {self.tipbill}')
r=Review('5*',500)
#r.Address()
#r.data()
#r.Billdata()       
