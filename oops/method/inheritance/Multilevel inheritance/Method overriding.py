#--------------------Method overriding   we can achieve using classname and super function----------------------------------------
class Dad:
    def Money(self):
        print('1cr')
class Child1(Dad):
    def Money(self):
        print('50lakh')
class Child2(Child1):
    def Money(self):
        print('25lakh')
c=Child2()
c.Money()#25lakh


class Dad:
    def Money(self):
        print('1cr')
class Child1(Dad):
    def Money(self):
        super().Money()
        print('50lakh')
class Child2(Child1):
    def Money(self):
        super().Money()
        print('25lakh')
c=Child2()
c.Money()#25lakh
