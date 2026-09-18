class Car:
    def start(self):
        print("Car started")

class Bike:
    def start(self):
        print("Bike started")

class Class:
    def start(self):
        print("class started")

class Engine:
    def start(self):
        print("Engine started")

class Metro:
    def start(self):
        print(" Metro started")

#1st way by creating one method and explicity pass one parameter
c=Car()
b=Bike()
c1=Class()
e=Engine()
m=Metro()
def Data(Q):
    Q.start()
Data(c)
#Data(Engine())
Data(m)
o/p:
Car started
Metro started

 
#2nd way by creating list
data=[Car(),Bike(),Class(),Engine(),Metro()]
for i in data :
    i.start()
o/p:
Car started
 Metro started
Car started
Bike started
class started
Engine started
 Metro started
