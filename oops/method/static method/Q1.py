'''Q1. Employee Payroll
Create a class Employee:

Constructor takes name and salary (instance variables).
Class variable company_name = "TechCorp".
Instance method show_details() →
prints name, salary, and company name (via self).
Classmethod change_company(cls, new_name)
→ updates company_name for all employees.
Staticmethod is_valid_salary(salary) → returns True if salary > 0, else False.

class Employee:
    cname = "TechCorp"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_details(self):
        print(self.name,self.salary,self.cname)
    @classmethod
    def ccompany(cls, new_name):
        cls.n=new_name

    @staticmethod
    def vaild(salary):
        if salary>0:
            print('True')
        else:
            print('False')
e=Employee('Ram',5000)
e.show_details()
e.ccompany('QSP')
e.vaild(5000)

o/p:
Ram 5000 TechCorp
True
