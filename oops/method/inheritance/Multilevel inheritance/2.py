
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'my name is {self.name} and mine age is {self.age}')
        
class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.sub=subject
    def show_data(self):
        print(f'mine subject name is {self.sub}')

class Incharge(Teacher):
    def __init__(self,name,age,subject,class_name):
        super().__init__(name,age,subject)
        self.class_name=class_name

    def details(self):
        print(f'i am taking in charge of {self.class_name}')

i=Incharge("Meera",28,"Python","A11")

i.show()
i.show_data()
i.details()
