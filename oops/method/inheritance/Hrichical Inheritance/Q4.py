4. Hierarchical Inheritance   
Create a Company class with company name.
Create Employee and Manager classes that inherit from Company.
Employee should store employee name and ID. Manager should store manager name and department.
Display the details of both objects.
'''
class Company:
    def __init__(self,cname):
        self.cname=cname
    def cinfo(self):
        print(f'The company name is {self.cname}')
class Employee(Company):
    def emp_info(self,cname,name,ID):
        super().__init__(cname)
        self.name=name
        self.ID=ID
    def einfo(self):
        super().cinfo()
        print(f'The Employee name is {self.name} and employee id is {self.ID}')
class Manager(Company):
    def emp_info(self,cname,mname,dept):
        super().__init__(cname)
        self.mname=mname
        self.dept=dept
    def minfo(self):
        super().cinfo()
        print(f'The Manager name is {self.mname} and department  is {self.dept}')
e=Employee('Qspider')
m=Manager('Qspider')
e.emp_info('Qspider','Rushi','E14')
m.emp_info('Qspider','Ramu','DA')
e.einfo()
m.minfo()


class Company:
    def __init__(self,cname):
        self.cname=cname
    def cinfo(self):
        print(f'The company name is {self.cname}')
class Employee(Company):
    def __init__(self,cname,name,ID):
        super().__init__(cname)
        self.name=name
        self.ID=ID
    def einfo(self):
        super().cinfo()
        print(f'The Employee name is {self.name} and employee id is {self.ID}')
class Manager(Company):
    def __init__(self,cname,mname,dept):
        super().__init__(cname)
        self.mname=mname
        self.dept=dept
    def minfo(self):
        super().cinfo()
        print(f'The Manager name is {self.mname} and department  is {self.dept}')
e=Employee('Qspider','Rushi','E14')
m=Manager('JQspider','Ramu','DA')
e.einfo()
m.minfo()
