class payment:
    name='hello'
    fees=45896
    def fee(self):
        #using classname
        #print(payment.name)
        print(payment.fees)
        #using object 
        #print(self.name)
        print(self.fees)
p=payment()
#access using class nmae
#payment.fee(p)
#access using object
p.fee()
#modification using classname
#payment.fees=40000
#payment.fee(p)
#p.fees=45000
#p.fee()
