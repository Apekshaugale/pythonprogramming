class Employee:
    def __init__(self, Cname, Tmember, Tpackage):
        self.Cname = Cname
        self.Tmember = Tmember
        self.Tpackage = Tpackage
    def Data(self):
        print(f'Company Name : {self.Cname}\n '
              f'and Total Member : {self.Tmember}\n '
              f'and Total Package : {self.Tpackage}')
class Startemployee(Employee):
    def __init__(self, Cname, Tmember, Tpackage, sal, yoe, role):
        super().__init__(Cname, Tmember, Tpackage)
        self.sal = sal
        self.yoe = yoe
        self.role = role
    def Info(self):
        print(f'Salary : {self.sal} \n'
              f'and YOE : {self.yoe}\n '
              f'and Role : {self.role}')
class Rules(Startemployee):
    def __init__(self, Cname, Tmember, Tpackage,
                 sal, yoe, role, intime, outtime, rolename):
        super().__init__(Cname, Tmember, Tpackage, sal, yoe, role)
        self.intime = intime
        self.outtime = outtime
        self.rolename = rolename
    def Check(self):
        print(f'In-time : {self.intime}\n '
              f'and Out-time : {self.outtime}\n '
              f'and Role Name : {self.rolename}')

r = Rules('Capgemini', 60, '7lpa', 45000, 2026, 'Analyst', 2, 5, 'BA')
r.Data()
r.Info()
r.Check()   
