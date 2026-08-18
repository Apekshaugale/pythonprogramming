#Write a program to get the following output
#input=[‘jiocinema.com’ , ‘file.py’ , ‘web.html’]
#output=[‘com’ , ‘py’ , ‘html’]
'''
s = ['jiocinema.com', 'file.py', 'web.html']
i = 0
a = []

while i < len(s):
    x = s[i].split('.')
    a.append(x[1])
    i += 1

print(a)

'''
#Q62.Write a program to get the following output
#input=[‘jiocinema.com’ , ‘file.py’ , ‘web.html’ , ‘amazon.com’ , ‘text.py’]
#output={‘com’:[‘jiocinema’ , ‘amazon’] , ‘py’:[ ‘file’ , ‘text’], ‘html’:[‘web’]}
input=['jiocinema.com', 'file.py' , 'web.html' , 'amazon.com' , 'text.py']
d={}
i=0
while i<len(input):
    x=input[i].split('.')
    print(x)
    
    d[(x[1])]=[x[0]]
    if x[1] in d:
        d[(x[1])].append(x[0])
        i+=1
print(d)

input = ['jiocinema.com', 'file.py', 'web.html', 'amazon.com', 'text.py']
d = {}
i = 0
while i < len(input):
    x = input[i].split('.')
    print(x)
    if x[1] in d:
        d[x[1]].append(x[0])
    else:
        d[x[1]] = [x[0]]
    i += 1
print(d)
#Q63.Write a program to get the following output(count no of vowels)
#input=‘hai hello’
#output={‘hai’:2 , ‘hello’:2}
