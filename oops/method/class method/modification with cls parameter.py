#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                   # Modification In class variable inside class method by using cls Parameter and class name
class student:
    name='Apeksha'
    rollno=59
    @classmethod
    def std(cls):
        
        print(cls.name)
student.std() #apeksha

class student:
    name='Apeksha'
    rollno=59
    @classmethod
    def std(cls):
        cls.name='shruu'  #modification using cls
        print(cls.name)
student.std() #shruu
s=student()
s.std()#shruu
print()

class student:
    name='Apeksha'
    rollno=59
    @classmethod
    def std(cls):
        student.name='puja'#modification using classname
        print(cls.name)
student.std() #puja
s=student()
s.std() #puja
