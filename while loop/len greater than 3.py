#wap to fetch str value from list only if len >3
s=eval(input('Enter the list : '))
i=0
string=' '
while i<len(s):
    if type(s[i])==str and len(s[i])>3:
        string=s[i]+' '+string
    i+=1
print(string)
