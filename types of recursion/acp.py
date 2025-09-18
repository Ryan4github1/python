def take_input():
    num = int(input("Enter a number: "))
    if num < 0:
        return
    else:
        take_input()

take_input()