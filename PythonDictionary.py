dictionary = {"name" :"sakshi", "name" : "varnit"}
print(dictionary) #wont give error but will take the last one only

dic1 = {"name" : "sakshi", "age" : 23}
for i in dic1:
    print(dic1[i])
tuple= (1,2,1,1)
print(sorted(tuple))
x=10

y=x
y=12
z=12
if id(z) == id(y):
    print("yes")
else:
    print("No")
