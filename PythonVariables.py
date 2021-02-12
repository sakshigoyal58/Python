#variable assignment
a = 5

#accessing global variable, no modification
def myfunc():
    print(a) #output->5

#passing a value when called, but will create a local "a" variable, not referenced to global variable "a"
def myfunc1(a):
    print(a) #output ->5

#passing a value when called, but will create a local "a" variable, not referenced to global variable "a"
def myfunc2(a):
    a = a+5
    print(a) #ouput->10
print(a) #ouput ->5

#"a" is a local variable, outside "a" is global variable but are different, though name is same
def myfunc3():
    a= 4
    print(a) #output ->4
print(a)#output ->5

#u can can only access global variable , but cant do any modification on it, will give error
#UnboundLocalError: local variable 'a' referenced before assignment
def myfunc4():
    a= a+5
    print(a) # will give error

#will give access to global variable , and u can modify
def myfunc5():
    global a
    a= a+5
    print(a) #output 10
print(a)#output 10

