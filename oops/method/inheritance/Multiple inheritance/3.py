class Company:
    def __init__(self, name):
        self.company_name = name

    def show_company(self):
        print(f"Company Name: {self.company_name}")

class Employee(Company):
    def __init__(self, name, emp_name, emp_id):
        super().__init__(name)
        self.emp_name = emp_name
        self.emp_id = emp_id

    def show_employee(self):
        print(f"Employee: {self.emp_name}, ID: {self.emp_id}")

class Manager(Company):
    def __init__(self, name, mgr_name, dept):
        super().__init__(name)
        self.mgr_name = mgr_name
        self.dept = dept

    def show_manager(self):
        print(f"Manager: {self.mgr_name}, Department: {self.dept}")

# Creating objects
e = Employee("TechCorp", "Alice", 101)
m = Manager("Tech", "Bob", "HR")

e.show_company()
e.show_employee()

m.show_company()
m.show_manager()

o/p:
Company Name: TechCorp
Employee: Alice, ID: 101
Company Name: Tech
Manager: Bob, Department: HR
