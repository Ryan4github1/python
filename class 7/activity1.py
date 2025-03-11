mc=input("Do you have a medical Cause. If yes then type in Y, if no type in N: ")
if mc=="N" or mc=="n":
    attper=int(input("Enter the attendance percentage:"))
    if attper>75:
        print("you're allowed to write exam.")
    else:
        print("you're not allowed")
elif mc=="Y" or mc=="y":
    print("you're allowed to write exam")
else:
    print("Invalid Input")