from abc import ABC,abstractmethod
class Information(ABC):
  @abstractmethod
  def subject_name(self,name):
    pass
    #print("demo") in parent class we are hiding name and total .
    # in parent class we use for hiding purpose .All method and parametes 
    # we have to declared as it is in child class
    
  @abstractmethod
  def total_score(self,total):
    pass #only declaration
    #print("demo")
  #we can't crete object for parent  class
  
class Result(Information):
  def subject_name(self,name):
    self.name=name
    print(name)
  def total_score(self,total):
    self.total=total
    print(total)
r=Result()
r.subject_name("Apeksha")
r.total_score(23)
#how many parent class method we created all we have to call in child class then only it will work 
#otherwise it won't work 
# you can create new method in child class then also it work
# if i create 2 method and call  only one in child class then we get error