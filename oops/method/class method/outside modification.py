#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  '''  ##modifying class variable outside using classname it will work but if we do modification using object it won't work

class location:
    city='pune'
    @classmethod
    def loca(cls):
        print(cls.city)
        print(location.city)
#print(location.city)
#location.city='delhi'
#location.loca()
#o/p:
#delhi
#delhi
l=location()
l.city='Nagpur' #modification using object it won't work because it will work on class not object
l.loca() #pune pune
location.loca() #pune
