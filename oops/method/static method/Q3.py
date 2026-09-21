
Q3. Student Result System
Create a class Student:

Constructor takes name and a list of marks (3 subjects).
Class variable passing_marks = 40.
Instance method total_and_average() → calculates
and prints total/average from self.marks.
Classmethod update_passing_criteria(cls, new_value) →
changes passing_marks.
Staticmethod is_pass(mark) → returns True/False by
comparing against a hardcoded 40 (independent check).

class Student:
    passing_marks = 40
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1mark=sub1
        self.sub2mark=sub2
        self.sub3mark=sub3
        
    def total_and_average(self):
        total=self.sub1mark+self.sub2mark+self.sub3mark
        print(total)
        average=total/3
        print(average)
        
    @classmethod
    def update_passing_criteria(cls, new_value):
        cls.passing_marks=new_value
        print(cls.passing_marks)

    @staticmethod
    def is_pass(mark):
        
        if mark>=40:
            return True
        else:
            return False
s=Student('Ram',45,67,45)
s.total_and_average()
s.update_passing_criteria(45)
print(s.is_pass(40))
o/p:
157
52.333333333333336
45
True
