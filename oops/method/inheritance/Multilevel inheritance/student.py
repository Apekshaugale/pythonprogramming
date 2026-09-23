2. Multilevel Inheritance

Q3. Student → CollegeStudent → EngineeringStudent
Create a class Student with name and age. Create a class CollegeStudent
that inherits from Student and adds college_name and percentage.
Create a class EngineeringStudent that inherits from CollegeStudent
and adds branch and cgpa. Use super() to initialize the attributes and display all details.

class Student:
    def student(self,name,age):
          self.name=name
          self.age=age
    def info(self):
        print(f'The name of student is {self.name} and age is {self.age}')
class CollegeStudent(Student):
    def cstudent(self,name,age,cname,percentage):
       super().student(name,age)
       self.cname=cname
       self.percentage=percentage
    def info (self):
        super().info()
        print(f'The College name of student is {self.cname} and percentage is {self.percentage}')
class EngineeringStudent(CollegeStudent):
    def estudent(self,name,age,cname,percentage,branch,cgpa):
        super().cstudent(name,age,cname,percentage)
        self.branch=branch
        self.cgpa=cgpa

    def info(self):
        super().info()
        print(f'The branch is {self.branch} and cgpa is {self.cgpa}')
e=EngineeringStudent()
e.student("Shree",23)
e.cstudent("Shree",23,"PRMCEAM",93)
e.estudent("Shree",23,"PRMCEAM",93,"CSE",8)
e.info()
o/p:
The name of student is Shree and age is 23
The College name of student is PRMCEAM and percentage is 93
The branch is CSE and cgpa is 8
