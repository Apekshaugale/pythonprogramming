#9.wap to print the number Table by using data given by user (take user input)
#expected output:-->2*1=2  2*2=4............2*10=20
num=eval(input('Enter the number : '))
i=1
while i<=10:
    print(num,'*',i,'=',i*num)
    i+=1
