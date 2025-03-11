print("1. car")
print("2. Bike")
vehchoice=int(input("press 1 for car and press 2 for bike: "))
if vehchoice==1:
    print("1. BMW")
    print("2. Pagani")
    carchoice=int(input("press 1 for BMW and pres 2 for Pagani:"))
    if carchoice==1:
        print("you chose BMW. Rate of 10$ per hour")
    elif carchoice==2:
        print("you chose Pagani. Rate of 150,000$ per hour")
    else:
        print("invalid choice")

elif vehchoice==2:
    print("1. Trek")
    print("2. Giant")
    bikechoice=int(input("press 1 for Trek and pres 2 for Giant:"))
    if bikechoice==1:
        print("you chose Trek. Rate of 10$ per hour")
    elif bikechoice==2:
        print("you chose giant. Rate of 0.1$ per hour")
    else:
        print("invalid choice")
else:
    print("invalid input")