import os
os.chdir(r"C:\Users\HP\Desktop\python")
import csv
with open("PQR.csv","w",newline="") as file:
    a=csv.writer(file)
    #a.writerow(["Apple",545,576])
    a.writerow(["Banana",54,76])
os.popen("PQR.csv")

\

  
import os
os.chdir(r"C:\Users\HP\Desktop\python")
import csv
with open("PQR.csv","a",newline="") as file:
    a=csv.writer(file)
    a.writerow(["Apple",545,576])
    a.writerow(["Banana",54,76])
os.popen("PQR.csv")


