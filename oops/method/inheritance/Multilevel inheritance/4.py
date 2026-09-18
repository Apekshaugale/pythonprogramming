class Class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def demo(self):
        print(self.name)
        print(self.age)
        print('class first')
class Student(Class):
    def __init__(self,name,age,height,money):
        self.h=height
        self.m=money
        super().__init__(name,age)
    def demo(self):
        super().demo()
        print(self.h)
        print(self.m)
        print('class second')
class Teacher(Student):
    def __init__(self,name,age,height,money,course):
        self.c=course
        super().__init__(name,age,height,money)
        super().demo()
        print(self.c)
c=Teacher("Rohit",34,5,89065,"HTML")


o/p:
Rohit
34
class first
5
89065
class second
HTML
