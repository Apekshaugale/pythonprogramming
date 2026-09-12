--------------------Two class having one constructor and instance method each ------------------
class Company:
    def __init__(self,name,sal,yop):
        self.name=name
        self.sal=sal
        self.yop=yop

    def Data(self):
        print(f'employee name is {self.name}\n'
              f'total salary is {self.sal}\n'
              f'yop is {self.yop}')

class Information(Company):
    def __init__(self,eid,role,add):
        self.eid=eid
        self.role=role
        self.add=add
        super().__init__("Rahul",45000,5)
        super().Data()
    def Data(self):
        #super().Data()
        print(f'employee id is {self.eid}\n'
              f'Role is {self.role}\n'
              f'current address is {self.add}')

i=Information("R13","Analysis","Pune")
i.Data()
