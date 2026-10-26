from abc import ABC,abstractmethod
class Emp(ABC):
    #in parent class there is only implemention no declaration
    @abstractmethod
    def Role(self,role_name):
        pass
    @abstractmethod
    def sal(self,total_sal):
        ...

    @abstractmethod
    def YOE(self,year):
        ...
    @abstractmethod
    def EID(self,eid):
        ...

class Data(Emp):
    def __init__(self,ename,age,loc):
        self.ename=ename
        self.age=age
        self.loc=loc
        print(f"Emp name is {self.ename} and age is {self.age} and loc is {self.loc}")
    def Role(self,role_name):
        self.role=role_name
        print(self.role)
    def sal(self,total_sal):
        self.total_sal=total_sal
        print(self.total_sal)
    def YOE(self,year):
        self.year=year
        print(self.year)
    def EID(self,eid):
        self.eid=eid
        print(self.eid)
d=Data("Apeksha",23,"Pune")
d.Role("HR")
d.sal(34000)
d.YOE(2026)
d.EID(102)




