class Language():
    def getLanguage(self):#abstract method
        raise NotImplementedError("error")

class English(Language):
    def getLanguage(self):
        return "English";

class French(Language):
    def getLanguage(self):
        return "French"

class Chinese(Language):
    pass

eng = English()
f = French()
c = Chinese()
print(eng.getLanguage())
print(f.getLanguage())
print(c.getLanguage())