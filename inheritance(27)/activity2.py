class person:
    def __init__(self,name,idno):
        self.name=name
        self.idno=idno
    def display(self):
        print("id:",self.idno,"name",self.name)
class Employee(person):
    def __init__(self,name,idno,salary,post):
        self.salary=salary
        self.post=post
        person. __init__(self,name,idno)
obj=Employee("bob","3.14159265","10,000$","TL")
obj.display()