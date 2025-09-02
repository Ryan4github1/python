def powerof8(number):
    if number <= 0:
        return False
    if (number & (number - 1)) != 0:
        return False
    shifts = 0
    while number > 1:
        number = number >> 1
        shifts += 1

    return shifts % 3 == 0
n = int(input("Enter a number: "))
if powerof8(n):
    print("This number is a power of 8")
else:
    print("This number is not a power of 8")