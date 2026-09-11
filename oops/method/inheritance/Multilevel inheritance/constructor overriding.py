#------constructor overriding-----------------
class Teacher:
    def __init__(self):
        print('First Class')
class Std1(Teacher):
    def __init__(self):
        super().__init__()
        print('Second class')
class Std2(Std1):
    def __init__(self):
        super().__init__()
        print('Third class')
s=Std2()
print(dir(s))


class Teacher:
    def __init__(self):
        print('First Class')
class Std1(Teacher):
    def __init__(self):
        super().__init__()
        print('Second class')
class Std2(Std1):
    def __init__(self):
        super().__init__()
        print('Third class')
s=Std2()
o/p:
First Class
Second class
Third class
