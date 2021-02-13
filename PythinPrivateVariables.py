class Demo:
    __name ="sakshi" #not accessbile outside class
    def __init__(self):
        self.__var = 123 #not accessible outside classs

    def getVal(self):
        self.__name = "sjbaskjd"
        return self.__name

d = Demo()
print(d.getVal())