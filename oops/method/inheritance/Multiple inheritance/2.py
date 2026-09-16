class Parent1:
    def __init__(self, name):
        #self.name=name
        print(f"Parent1 Constructor: Hello {name}")

    def show(self, age):
        print(f"Parent1 Show: Age is {age}")

class Parent2:
    def __init__(self, city):
        print(f"Parent2 Constructor: You live in {city}")

    def show(self, country):
        print(f"Parent2 Show: Country is {country}")

class Child(Parent1, Parent2):
    def __init__(self, name, age,city,country):
        #print("Child Constructor starts")
        super().__init__(name)    # Calls Parent1 first (MRO)
        Parent2.__init__(self, city)  # Manually call second parent
        #print("Child Constructor ends")

    #def show(self, age, country):
        print("Child Show Method")
        super().show(age)             # Calls Parent1's show
        Parent2.show(self, country)   # Manually call Parent2's show

# Test
c = Child("Prince", 25,"Bangalore", "India")
#c.show(25, "India")
