#Nested For Loop:
'''
#Wap to get the following output. without length function.
s = 'power star'
d = {}
for word in s.split():
    count = 0
    for i in word:
        count += 1
    d[word] = count
print(d)
#Out={'power':5,'star':4}




#Wap to get the following output.
#S='power star'
#Out={'power':2,'star':1} (no of vowels is key)
s = 'power star'
d = {}

for a in s.split():
    count=0
    for i in a:
        if i in 'aeiou':
            count=count+1
            d[a]=count      
print(d)        

 

#Wap to get the following output.
s='kabab is love'
d={}
for i in s.split():
    count=0
    even=' '
    for a in i:
        if a in 'aeiou' :
          count=count+1
          if  i%2==0:
              even =even+a[i]
              d[i]=[i[::-1],count,even]
print(d)
        
#Out={'kabab':['babak',2,'kbb'],'is':['si',1,'i'],'love':['evol',2,'lv']}
#[reverse,no of vowels,char at even index]



#Wap to get the following output.
#S='kabab is love'
#Out={'kb':('kbb',3,'bbk'),'is':('s',1,'s'),'le':('lv',2,'vl')}
#{ 1ˢᵗ+last char: (consonant,no of consonant,rev of consonant)}
s='kabab is love'
d={}
for i in s.split():
    count=0
    consonant=' '
    for a in i:
        if a not in 'aeiou' :
            
          count=count+1
          consonant=consonant+a
          d[i[0]+i[-1]]=[consonant,count,consonant[::-1]]
print(d)

'''

       



