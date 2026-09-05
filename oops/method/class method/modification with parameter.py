#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ##modifying class variable inside second class method with parameter
class school:
    name='yogi'
    @classmethod
    def std(cls):
        print(cls.name)
        print(school.name)

    @classmethod
    def std1(cls,newstd):
            #school.name=newstd
            cls.name='shreee'
            print(school.name)
#school.std1('shreee')
school.std()
school.std1('shreee')
o/p:
yogi
yogi
shree
