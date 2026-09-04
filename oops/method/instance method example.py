#Instance Method Examples (Practice_example)

'''
1.Create a class Person
Store name and age
Display details
'''
'''
class person:
    name='Sakshi'
    age=25
    def info(self):
        print(person.name)
        print(person.age)
p=person()
person.info(p)
o/p:
    Sakshi
25
class person:
    name='Sakshi'
    age=25
    def info(self):
        print(p.name)
        print(p.age)
p=person()
person.info(p)#usingclassname
o/p:
    Sakshi
25


class person:
    name='Sakshi'
    age=25
    def info(self):
        print(p.name)
        print(p.age)
p=person()
p.info()#using object
o/p:
    Sakshi
25

class person:
    def info(self):
        self.name='Sakshi'
        self.age=25
        person.info1(self)
    def info1(self):
        print(p.name)
        print(p.age)
p=person()
person.info(p)
o/p:
 Sakshi
25   


2.Create a class Dog
Store name and breed
Print dog details


class Dog:
    name='tizen'
    breed='Golden retriver'
    def details(self):
        print(Dog.name)
        print(self.breed)
d=Dog()
d.details()
#o/p:
#tizen
#Golden retriver
Dog.details(d)
o/p:
    tizen
Golden retriver


class Dog:
    def det(self):
         self.name='tizen'
         self.breed='Golden retriver'
         Dog.details(self)
    def details(self):
        print(self.name)
        print(self.breed)
d=Dog()
d.det()
Dog.det(d)
o/p:
tizen
Golden retriver
tizen
Golden retriver


'''

#3.Create a class Fan Store brand and price Display details
'''class fan:
    brand='titan'
    price=5990
    def fann(self):
        print(fan.price)
        print(self.brand)
f=fan()
fan.fann(f)
f.fann()
o/p:
5990
titan
5990
titan

class fan:
    def fan1(self):     
        self.brand='titan'
        self.price=5990
        fan.fann(self)
    def fann(self):
        #print(fan.price)
        print(self.brand)
f=fan()
fan.fan1(f)
o/p:
    titan


class fan:
    def fan1(self):     
        self.brand='titan'
        self.price=5990
        fan.fann(self)
    def fann(self):
        print(self.price)
        print(self.brand)
f=fan()
fan.fan1(f)
o/p:
5990
titan
'''

