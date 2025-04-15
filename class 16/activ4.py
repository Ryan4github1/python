valid = False
while not valid:
    try:
        n=int(input("Enter the number: "))
        if n%2==0:
            print("bye")
            valid = True
    except ValueError:
        print("Invalid")
