
'''
rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        print('*',end=' ')
    print()

o/p:
Enter the rows : 5
Enter the column : 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *

rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if row==col:
          print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

o/p=
Enter the rows : 5
Enter the column : 5
*         
  *       
    *     
      *   
        * 


rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if row+col==rows-1:
          print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


o/p=
Enter the rows : 5
Enter the column : 5
        * 
      *   
    *     
  *       
*         

rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if row==col or row+col==rows-1 :
          print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
o/p=
Enter the rows : 5
Enter the column : 5
*       * 
  *   *   
    *     
  *   *   
*       * 
    
rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if row==col:
            print('#',end=' ')
        elif row>=col:
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()

o/p=
Enter the rows : 5
Enter the column : 5
#         
@ #       
@ @ #     
@ @ @ #   
@ @ @ @ # 



rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if row==col:
            print('@',end=' ')
        elif row<=col:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()


o/p=
Enter the rows : 4
Enter the column : 4
@ # # # 
  @ # # 
    @ # 
      @ 

(0,0)  (0,1)  (0,2)  (0,3)  (0,4)

(1,0)  (1,1)  (1,2)  (1,3)  (1,4)

(2,0)  (2,1)  (2,2)  (2,3)  (2,4)

(3,0)  (3,1)  (3,2)  (3,3)  (3,4)

(4,0)  (4,1)  (4,2)  (4,3)  (4,4) 
 

rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if row<=col:
            print('@',end=' ')
        elif row<=col:
            print('#',end=' ')
        else:
            print(' ',end=' ')
    print()
o/p=
Enter the rows : 5
Enter the column : 5
@ @ @ @ @ 
  @ @ @ @ 
    @ @ @ 
      @ @ 
        @ 
'''
''' 
rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for row in range(rows):
    for col in range(columns):
        if  row+col>=rows  or row+col==rows-1:
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()



rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for i in range(rows):
    for  j in  range(columns):
        if  i+j==rows-1  or i+j<=rows:
            print('@',end=' ')
        else:
            print(' ',end=' ')
    print()


rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for i in range(rows):
    for  j in  range(columns):
        if i%2==1 and  j%2==1:
            print('  ',end=' ')
        else:
            print('*',end=' ')
    print()
o/p=
Enter the rows : 5
Enter the column : 5
* * * * * 
*    *    * 
* * * * * 
*    *    * 
* * * * * 

rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for i in range(rows):
    for  j in  range(columns):
        if i==j:
            print('*',end=' ')
        elif i>=j:
            print('@',end=' ')
        else:
            print(' ! ',end=' ')
    print()

o/p=
Enter the rows : 5
Enter the column : 5
*  !   !   !   !  
@ *  !   !   !  
@ @ *  !   !  
@ @ @ *  !  
@ @ @ @ * 

'''
rows=int(input('Enter the rows : '))
columns=int(input('Enter the column : '))
for i in range(rows):
    for  j in  range(columns):
        if i==j :
            print('*',end=' ')
        elif i>=j:
            print(' ! ',end=' ')
        else:
            print('@',end=' ')
    print()

o/p=
Enter the rows : 5
Enter the column : 5
* @ @ @ @ 
 !  * @ @ @ 
 !   !  * @ @ 
 !   !   !  * @ 
 !   !   !   !  * 




    
