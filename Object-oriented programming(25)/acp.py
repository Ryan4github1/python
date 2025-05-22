class parrot:
    species="parrot"
    def __init__(self,name,age):
        self.nam=name
        self.a=age
bluobj=parrot("blu",10)
wooobj=parrot("woo",25)
print(bluobj.nam," is ", bluobj.a, "years old") 
print(wooobj.nam," is ", wooobj.a, "years old")
print(bluobj.nam," is ",bluobj.species)
print(wooobj.nam," is ",wooobj.species)