#15.wap to iterate inside the list check if it is having nested list if yes merge it
#list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
#excepted output:-->list1=["hello",10,20.55,True,False,"hai","bye",False,"goodnight","enjoy the holiday"]
'''
list1=["hello",10,20.55,True,False,"hai","bye",[False,"goodnight","enjoy the holiday"]]
i=0
a=[False,"goodnight","enjoy the holiday"]
while i<len(list1):
    if a  in list1:
        list1.append(a)
        print(list1)
     i+=1

out1=[]
out=[]
i=0
while i<len(list1):
    if type(list1[i])==list:
       out1.append(list1[i])
       print(out1)
       list1.pop(i)
    i+=1
print(list1)
list1.extend(out1)
print(list1)
'''


#find count of i in nitin
a='Nitin'
count=0
i=0
while i<len(a):
    if a[i]=='i':
        count=count+1
    i+=1
print('count of i is ', count)
