class vehicle:
    def __init__(self,mileage,max_speed):
        self.mile=mileage
        self.max=max_speed
obj=vehicle(99999,10000)
print("maximum speed of the car=",obj.max)
print("total mileage of the car=",obj.mile)