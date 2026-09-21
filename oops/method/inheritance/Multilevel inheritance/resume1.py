'''class School:
    
    def __init__(self):
        self.name='Apeksha Ugale'
        self.Sname='S.B.High.School'
        self.marks='91.60%'
    def school_info(self):
        super().__init__()
        print(f'My name is {self.name}\n'
              f'My School name is {self.Sname}\n'
              f'My 10th percentage is {self.marks} ')
        
class Twelth(School):
    
        def __init__(self):
            self.Cname='S.B.High.School And Jr Science College'
            self.marks='81.83%'

        def college_info(self):
            super().__init__()
            super().school_info()
            print(f'My College name is {self.Cname}\n'
              f'My 12th percentage is {self.marks} ')

class Degree(Twelth):

    def __init__(self):
        self.Dclgname='PRMCEAM'
        self.cgpa='8.4'
    def Degree_info(self):
        super().__init__()
        super().college_info()
        print(f'My Degree College name is {self.Dclgname}\n'
              f'My Degree CGPA is {self.cgpa} ')
t=Degree()
t.Degree_info()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

class School:
    def __init__(self,name,Sname,marks):
        self.name=name
        self.Sname=Sname
        self.marks=marks
    def school_info(self):
        print(f'My name is {self.name}\n'
              f'My School name is {self.Sname}\n'
              f'My 10th percentage is {self.marks} ')
        
class Twelth(School):  
        def __init__(self,name,Sname,marks,Cname,marks1):
            super().__init__(name,Sname,marks)
            self.Cname=Cname
            self.marks1=marks1
        def college_info(self):         
            super().school_info()
            print(f'My College name is {self.Cname}\n'
              f'My 12th percentage is {self.marks} ')

class Degree(Twelth):
    def __init__(self,name,Sname,marks,Cname,marks1,Dclgname,cgpa):
        super().__init__(name,Sname,marks,Cname,marks1)
        self.Dclgname=Dclgname
        self.cgpa=cgpa
    def Degree_info(self):
        super().college_info()#method overriding
        print(f'My Degree College name is {self.Dclgname}\n'
              f'My Degree CGPA is {self.cgpa} ')
t=Degree("Apeksha","SBHIGH school","91.60%","S.B.High.School And Jr Science College","81.83% ","PRMCEAM","8.4")
t.Degree_info()
