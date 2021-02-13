class BaseClass1():
    def __init__(self,name):
        self.name = name
class BaseClass2():
    def __init__(self,age):
        self.age = age

class DerivedClass(BaseClass1,BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self,"sakshi")
        BaseClass2.__init__(self,45)

s = DerivedClass()
print(s.name)
print(s.age)

