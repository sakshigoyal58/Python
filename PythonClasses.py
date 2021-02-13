class Student:
    _numberOfStudents = 0
    def __init__(self, name, grade):
        self.name = name
        self._percentage = grade
        Student._numberOfStudents +=1
    def calculateDiscount(self):
        return 2*3

class Sakshi(Student):
    def __init__(self,name):
        super().__init__(name,85)
        self.__name = name
    def getName(self):
        Student._numberOfStudents = 6
        return Student._numberOfStudents
    def calculateDiscount(self):
        return 2*888
class d:
    def __init__(self):
        pass

class Varnit(Student,d):
    def __init__(self,name):
        self.name = name
    def getName(self):
        pass

sakshi = Sakshi("sakshi")
print(sakshi.name)
print(sakshi._numberOfStudents)
print(sakshi.getName())
print(sakshi._percentage)
sakshi._percentage = 99
print(sakshi._percentage)
sakshi.__name = "sweety"
print(sakshi.calculateDiscount())


