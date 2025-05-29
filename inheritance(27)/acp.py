class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def get_info(self):
        return "Vehicle Name: {}, Capacity: {}".format(self.name, self.capacity)


class Bus(Vehicle):
    def __init__(self, name, capacity, fare_per_passenger):
        super().__init__(name, capacity)
        self.fare_per_passenger = fare_per_passenger

    def calculate_total_fare(self):
        return self.capacity * self.fare_per_passenger


bus = Bus("City Bus", 50, 2.5)
print(bus.get_info())