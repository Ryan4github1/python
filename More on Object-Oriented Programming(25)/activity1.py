class IOstring:
    def __init__(self):
        self.str1=''
    def getstring(self):
        self.str1=input("Enter the word:")
    def upstring(self):
        print("uppercase=",self.str1.upper())
obj=IOstring()
obj.getstring()
obj.upstring()