#OS MODEL:(operating system)

#(1)-step1 --> import os
#

# if we want to check current location -- we have to use inbuilt function--( getcwd() )

#(1)-------------> getcwd()------------>

#syntax-->
#            [  os.getcwd()   ]--------print (s.getcwd)---shows current location--where we are 


#Exa-->

#import os
#print(os.getcwd())

#o/p--><built-in function getcwd>----------without parenthesis
#o/p--> C:\Users\vidhi\github\PythonSubject------with parenthesis


#(2)----------------chdir()------------> (change directory)
#where we want to go

#syntax--> os.chdir("path")

import os
print(os.chdir(r"C:\Users\vidhi\github\PythonSubject"))

#odd slash---> special sequence

# /n--new line                          
# /b--one backspace
# /t--one tab space

#way-(1)-->

#To avoide special sqquence we can use even slash

#                        OR

#way-(2)-->

#'r'--(RawString)

#(3)------------------MKDIR()--------------->

# to create single folder

#syntax---> os.mkdir('folder name')

#exa-->
"""
import os
os.mkdir('sql')
"""


#(4)-------------------MAKEDIRS()----------->

#if i want to create nested folder--->   MAKEDIRS()

#os.makedirs("A\B\C\B")


#(5)--------------------LISTDIR()------------>
#what are the things are present in the folder if we want to check then we can go for listdir

#Syntax--> os.listdir()
"""
import os
print(os.listdir())
"""

#(6)-------------RENAME()--------->

#--if you want to change file name or folder name then we have   to go for (rename inbuilt function ) or method name-- 

#Syntax-->  os.rename()


#example-->
"""
import os
os.rename("Hi.txt","Hello")
"""

#(7)------------RMDIR()------------>

#if we want to delete the folder then we can go for rmdir function

#Syntax--> os.rmdir("folder name")


#(1)--QUE-->difference between mkdir and rmdir

#(8)-------------REMOVE()----------->

#syntax--> os.remove('filename')

# If we want to delete the file then we can go for remove function

#----------(9)--POPEN()------------>

#Syntax--> os.popen('file name ')

#if we want to open file or folder we have to go for  popen fnction

#import os
#print(os.getcwd())
#os.chdir(r"C:\Users\vidhi\OneDrive\Desktop\E14")
#os.mkdir("java")
#os.rename("java.txt","SQL")

