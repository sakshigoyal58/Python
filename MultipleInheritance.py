class BaseClass1():
    __school = "abcdefg"
    def __init__(self,name):
        self.name = name
    def get(self):
        return self.__school
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
print(s.get())


