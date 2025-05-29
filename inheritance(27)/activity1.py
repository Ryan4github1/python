class vehicle:
    def __init__(self,name,colour,price):
        self.name=name
        self.colour=colour
        self.price=price
    def show(self):
        print("name:",self.name,"colour:",self.colour,"price:",self.price)
class car(vehicle):
    pass
class bike(vehicle):
    pass
obj=car("ford","white","10,000,000$")
obj.show()
obj=bike("yamaha","black","314.159265$")
obj.show()
