class parrot:
    species="dog"
    def __init__(self,name,age):
        self.nam=name
        self.a=age
bullobj=dog("bull",10)
beagleobj=dog("beagle",25)
print(bullobj.nam," is ", bullobj.a, "years old") 
print(beagleobj.nam," is ", beagleobj.a, "years old")
print(beagleobj.nam," is ",beagleobj.species)
print(bullobj.nam," is ",bullobj.species)