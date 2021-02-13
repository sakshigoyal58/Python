class Student:
    def __init__(self):
        pass
    def __setname(self,name):
        self.__name =  name
    def __getname(self):
        return self.__name
    name = property(__getname,__setname)


sakshi = Student()
sakshi.name = "nkj"
print(sakshi.name)
