a={"inda":"kashmir","uk":"usa","banglore":"rashia"}
b={'sham':"ram","geeta":'sita',"rahul":"rohan"}
# for i in zip(a,b):
#     print(i)

 c={}
for i,j in zip(a,b.values()):
     c[i]=j
 print(c)
      # print(i,j)
