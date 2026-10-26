#example:

from abc import ABC
class Test(ABC):
  def demo(self):
    print("demo method")
t=Test()
t.demo()

#example:

#comprate class
class Test:
  def demo(self):
    print("demo")#is it possible to create object for abc class yes when we are not decorated with @abcmodule
t=Test()
t.demo()

#example:

from abc import ABC, abstractmethod
class Test(ABC):
  @abstractmethod
  def __init__(self):
    print("constructor")

# Note: Instantiating the class directly raises a TypeError because it has abstract methods:
# t = Test()
# To use it, you must subclass it and implement __init__ in the child class.


#example:

from abc import ABC,abstractmethod
class Information(ABC):
  @abstractmethod
  def subject_name(self,name):
    pass
    #print("demo") in parent class we are hiding name and total .in parent class we use for hiding purpose .All method and parametes we have to declared as it is in child class
    #
  @abstractmethod
  def total_score(self,total):
    pass
    #print("demo")
  #we can't crete object for parent  class
class Result(Information):
  def subject_name(self,name):
    print(name)
  def total_score(self,total):
    print(total)
t=Test()
t.demo()



#example:

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
d=Data("Apeksha",23,"Pune",)
d.Role("HR")
d.sal(34000)
d.YOE(2026)
d.EID(102)




