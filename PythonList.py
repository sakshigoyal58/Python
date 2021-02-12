list1 = [1,2,3,4,5]
list2 = [4,5,2,3,5]
list1.extend(list2)
print(list1)
print(list2)
list2[0]= 103
print(list2)
print(list1)
l1= [1,2,3]
l2=l1
print(l1)
print(l2)
l2[0] = 67
print(l1)
print(l2)
list3 =[]
list3 = list1.copy()
print(list3)
list3[0]=99
print(list1)
print(list3)
list3.pop()
print(set(list3)) #will convert to set