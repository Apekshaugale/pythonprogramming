#wap to print uppercase ,lowercase,digit ,special caharcter
s=str(input('Enter the string :'))
upper=' '
lower=' '
digit=' '
special=' '
i=0
while i<len(s):
    if s[i].isupper():
        upper=upper+s[i]
    elif s[i].islower():
        lower=lower+s[i]
    elif s[i].isdigit():
        digit=digit+s[i]
    else:
        special=special+s[i]
    i+=1
print(upper)
print(lower)
print(digit)
print(special)
