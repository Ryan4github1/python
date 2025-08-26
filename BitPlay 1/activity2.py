def setOrNot(number, n):
    mask = 0
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n -1 )):
            print("SET(yes bit value is 1)")
        else:
            print("NOT SET(bit value is 0)")
number = int(input("enter your number:"))
binary_string = bin(number)
n = int(input("Enter the bit position:"))
binary = binary_string.replace('0b',' ')
print("binary value",binary)
setOrNot(number, n)