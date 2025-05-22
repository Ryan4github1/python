class fruit:
    def __init__(self,name,colour):
        self.nam=name
        self.col=colour
ob=fruit("apple","red")
ob1=fruit("banana","yellow")
print("this is the details of the first object:")
print(ob.nam)
print(ob.col)
print("this is the details of the second object:")
print(ob1.nam)
print(ob1.col)
