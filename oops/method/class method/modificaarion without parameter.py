#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
  #modifying class variable inside second class method without parametr  
class School:
        fee=1000
        @classmethod
        def Data(cls):
                print(f'Total School Fee {cls.fee}')

        @classmethod
        def Updated_data(cls):
                School.fee=9000 #modify using classname
                #cls.fee=30000  #modify using cls
                print(f'Total School Fee {cls.fee}')#access cl
                print(f'Total School Fee {School.fee}')#cname
x=School() #oobject create 
x.Data() #1000
x.Updated_data() #9000
School.Data() # calling class name
School.Updated_data()
