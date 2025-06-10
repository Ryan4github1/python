class BMW:
    def start(self):
        print("BMW is starting.")

    def speed(self):
        print("BMW can go up to 250 km/h.")

    def fuel_type(self):
        print("BMW uses petrol.")

class Ferrari:
    def start(self):
        print("Ferrari is starting.")

    def speed(self):
        print("Ferrari can go up to 340 km/h.")

    def fuel_type(self):
        print("Ferrari uses special petrol.")

def car_details(car):
    car.start()
    car.speed()
    car.fuel_type()
    print("-" * 30)

bmw_car = BMW()
ferrari_car = Ferrari()

car_details(bmw_car)
car_details(ferrari_car)