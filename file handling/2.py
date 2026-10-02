import os
os.chdir(r"C:\Users\HP\Desktop\python")
import csv
with open("ABC.csv","w",newline="") as file:
    a=csv.DictWriter(file,fieldnames=['EID','ENAME','CONTACT'])
    a.writeheader()
    a.writerow({'EID':102,'ENAME':'Sham','CONTACT':75869394947})
    a.writerow({'EID':103,'ENAME':'Ramu','CONTACT':75861491147})
os.popen("ABC.csv")



import os
os.chdir(r"C:\Users\HP\Desktop\python")
import csv
with open("ABC.csv","a",newline="") as file:
    a=csv.DictWriter(file,fieldnames=['EID','ENAME','CONTACT'])
    a.writeheader()
    a.writerow({'EID':104,'ENAME':'Geeta','CONTACT':75869394947})
    a.writerow({'EID':105,'ENAME':'Rami','CONTACT':75861491147})
os.popen("ABC.csv")




