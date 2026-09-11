#-------------by passing parameters-----------------------------
class Institude:
    def Information(self,In,Stack,Fee):
        self.In=In
        self.Stack=Stack
        self.Fee=Fee
        print(f'Institude name is {self.In}\n'
              f'Student Course name is {self.Stack}\n'
              f'Total fees is {self.Fee}')
class Student(Institude):
    def  Subject(self,Sn,Tc,Tp):
        self.Sn=Sn
        self.Tc=Tc
        self.Tp=Tp
        print(f'Subject name is {self.Sn}\n'
              f'Total class name is {self.Tc}\n'
              f'Total time  is {self.Tp}')
class Result(Student):
    def Finalstage(self,TM,Grade):
        self.TM=TM
        self.Grade=Grade
        print(f'Total marks is {self.TM}\n'
              f'Grade is {self.Grade}'   ) 
r=Result()
r.Finalstage(57,'A+')
r.Subject('Shree',60,'6month')        
r.Information("Qspider",'Datascience',85000)
o/p:
Total marks is 57
Grade is A+
Subject name is Shree
Total class name is 60
Total time  is 6month
Institude name is Qspider
Student Course name is Datascience
Total fees is 85000
