a ="5"
print(int(a))
b =5
print(str(b))
print(bool(0))#false
print(bool(""))#false
print(bool(0.0))#false

j ="value"
j="sakshi" # possible will create a new  value and j will be assigned to it
print(j)
#j[0] ="a"
print(j)#will give error TypeError: 'str' object does not support item assignment
print(j[0])
print(j[-1])
#print(j[6])# IndexError: string index out of range
j= j.replace("s","a")
print(j)

#how to modify existing string
new_str = "sakshi"
l = list(new_str)
print(l)
k=0;
for i in l:
    if i =='s':
        l[k] = 'a'
    k= k+1
g=""
print(l)
print(g.join(l))

sentence = "i am, good girl"
print(sentence.split())


