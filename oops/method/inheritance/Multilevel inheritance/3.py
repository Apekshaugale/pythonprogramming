'''class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'My name is {self.name} and my age is {self.age}')


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.sub = subject

    def show_data(self):
        super().show()
        print(f'My subject name is {self.sub}')


class Incharge(Teacher):
    def __init__(self, name, age, subject, class_name):
        super().__init__(name, age, subject)
        self.class_name = class_name

    def details(self):
        super().show_data()
        print(f'I am taking in charge of {self.class_name}')


i = Incharge("Meera", 28, "Python", "A11")

#i.show()
#i.show_data()
i.details()
o/p:
My name is Meera and my age is 28
My subject name is Python
I am taking in charge of A11

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'My name is {self.name} and my age is {self.age}')


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.sub = subject

    def show(self):
        super().show()
        print(f'My subject name is {self.sub}')


class Incharge(Teacher):
    def __init__(self, name, age, subject, class_name):
        super().__init__(name, age, subject)
        self.class_name = class_name

    def show(self):
        super().show()
        print(f'I am taking in charge of {self.class_name}')
i = Incharge("Meera", 28, "Python", "A11")

i.show()
#i.show_data()
#i.details()
'''


