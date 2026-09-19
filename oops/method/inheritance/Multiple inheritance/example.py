'''Q10. School system
Create University with class variable univ_name. Create College(University) with a method exam().
Create Student(College) with a method assignment().
Access univ_name and call all methods from a Student object — then explain using dir()
what attributes/methods Student has access to.

class University:
    univname = 'SGBAU'
class College(University):
    def exam(self):
        print('College exam')
class Student(College):
    def assignment(self):
        super().exam()
        print(self.univname)
        print('Student assignment')
s = Student()
print(s.univname)
s.exam()
s.assignment()
print(dir(s))
o/p:
SGBAU
College exam
College exam
SGBAU
Student assignment
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'assignment', 'exam', 'univname']
'''
#Multiple Inheritance
'''
Q1. Basic two-parent inheritance
Create a class Father with a method skills() that prints "Gardening, Cooking".
Create a class Mother with a method talents() that prints "Painting, Singing".
Create a class Child(Father, Mother) with its own method hobbies() that prints "Cricket".
Create a Child object and call all three methods.

class Father :
    def skills(self):
        print("Gardening, Cooking")
class Mother:
    def talents(self):
        print("Painting, Singing")
class Child(Father, Mother):
    def hobbies(self):
        print( "Cricket")
c=Child()
c.skills()
c.talents()
c.hobbies()
o/p:
Gardening, Cooking
Painting, Singing
Cricket

Q2. Class variables from both parents
Create a class Company with class variable salary = 50000.
Create a class Bank with class variable interest_rate = 5.
Create a class Employee(Company, Bank) with a method details() that prints both salary and interest_rate.
Access both variables via object and via details().

class Company:
    salary=5000
class Bank:
    interest_rate = 5
class Employee(Company, Bank):
    def details(self):
        print(self.salary)
        print(self.interest_rate)
e=Employee()
e.details()
o/p:
5000
5

Q3. Method Resolution Order (MRO) — same method name in both parents
Create A with a method show() that prints "A's show".
Create B with a method show() that prints "B's show".
Create C(A, B) (no show() of its own). Create an object of C and call show().
Which one executes, and why? (Hint: look up MRO / C.__mro__).
'''
class A:
    def show(self):
        print("A's show")
class B:
    def show(self):
        print("B's show")
class C(A,B):
    def show(self):
        super().A()
        super().B()
c=C()
c.A()
c.B()
'''
Q4. Constructors in multiple inheritance
Create Employee with __init__(self, name) that sets self.name and prints "Employee constructor".
Create Trainer with __init__(self, subject) that sets self.subject and prints "Trainer constructor".
Create SeniorTrainer(Employee, Trainer) with its own __init__ that calls
both parent constructors manually (using Employee.__init__(self, name) and Trainer.
__init__(self, subject) — not super(), since super() behaves differently with multiple inheritance).
Create an object and print name and subject.

Q5. Real-world example — Smartphone
Create a class Camera with a method click_photo() that prints "Photo clicked".
Create a class MusicPlayer with a method play_song() that prints "Song playing".
Create a class Smartphone(Camera, MusicPlayer) with its own method make_call() that prints "Calling...".
Create an object of Smartphone and call all three methods.

Q6. Diamond problem (conceptual + code)
Create a class A with method info() → prints "Class A". Create B(A) and C(A), neither overriding info().
Create D(B, C). Create an object of D and call info(). Use print(D.__mro__) to see the order Python uses to resolve this —
explain in your own words why Python doesn't call info() from A twice.

Q7. Bank + Insurance combo account
Create SavingsAccount with balance and method deposit(amount). Create InsurancePolicy with policy_number
and method policy_details(). Create PremiumAccount(SavingsAccount, InsurancePolicy) that combines
both — able to deposit money and show policy details from a single object.
'''
