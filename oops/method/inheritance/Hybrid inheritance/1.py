#single level +mutilevel+indipendent+multiple
class Name:
    def show(self):
        print('first class')
        
class Student(Name):
    def demo(self):
        print('Singel level')
        
class Teacher(Student):
    def info(self):
        print('Multilevel Inheritance')
        
class Principal(Teacher):
    def info1(self):
        print('Principal class')
        
class School:
    def info2(self):
        print('Independent')
        
class Manager(School,Principal):
    def show1(self):
        print('Multiple Inheritance')
s=Student()
s.show()
s.demo()
p=Principal()
p.info()
p.info1()
m=Manager()
m.show1()
m.info2()

#single level +hirachical+multiple

class Name:
    def show(self):
        print('first class')
        
class Student(Name):
    def demo(self):
        print('Singel level')
        
class Teacher(Name):
    def info(self):
        print('Multilevel Inheritance')
        
class Principal(Student,Teacher):
    def info1(self):
        print('Principal class')
        
p=Principal()
p.demo()
p.info1()
