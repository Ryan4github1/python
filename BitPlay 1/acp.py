def rightmostSetBit(n):
    position = 1
    while n > 0:
        if (n & 1) == 1:
            print("Rightmost set bit is at position:", position)
            return
        n >>= 1
        position += 1
    print("No set bit found")

number = int(input("Enter your number: "))
binary_string = bin(number)
binary = binary_string.replace("0b", "")
print("Binary value:", binary)

rightmostSetBit(number)