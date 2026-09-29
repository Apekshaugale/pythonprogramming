#File Handling--> if we want to store  any data parmanently or temperorily then we can go for file

#types of file-->
#                            (1)--> Text File
#                           (2)---> Binary File(MP3,MP4)


#Syntax--(1)--> without context manager
#we need to close the file manually 

#                       New var_name('filename.extension','mode')

#where-->
#           mode--> operation

#Syntax--(2)--> with context manager
#once we close the loop automatically it will close the file 

#                   with open('filename.extension','mode') as filename:

#Mode operation--->

#NOTE-->>>if i not mentioned any mode then by default it will take it as a read mode (r-mode)

#(1)--x
#if we want to create empty file then we can go for x mode

#(2)--r
#if we want to read (reading purpose) all the data then we can go for r mode
#some methods in r mode--->



#(1)--read()--to read
#(2)--read(n)--
#           where (n)--number of character
#(3)--readline()
#(4)--readlines()  --output in list format
#(5)--readable()--output--true-false



#(3)--w
#if we want to add any data we can take the help of W mode
#single line
#(1)--writelines()--multiple lines
#(2)--writable()--output--true --false


#(4)--a
#(5)--rt
#(6)--wt
#(7)--at

#pickle--> 
#(8)--rb
#(9)--wb


#import os
#print(os.getcwd())
#os.mkdir("pyhton")
#os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
#file=open("Marker.txt",)
#print(file.name)
#print(file.mode)
#print(file.writable())
#print(file.readable())
#want to check my file is close or not we have to go for property----(file.close)
#file.close()   # want to close file manually then we use close function
#print(file.closed)  #output will be the form of boolean


#import os
#print(os.getcwd())
#os.mkdir("pyhton")
#os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
#file=open("Marker.txt",'r')
#os.popen("Marker.txt")
#print(file.read)


import os
print(os.getcwd())
os.mkdir("pyhton")
os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")

#file=open("pen.txt","w")
#print(file.write("Good Luck"))
#file.write("Good Afternoon")
#file.writelines(["Hello\n","java\n","python\n","Sql\n"])
#os.popen("pen.txt")

#(a-Mode)---->

file=open("mobile.txt","a")
file.write("programming \n")
os.popen("mobile.txt")




