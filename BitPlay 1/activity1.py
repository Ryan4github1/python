def numberOfBits(n):
    ones = 0
    zeroes = 0
    while (n):
        if (n&1==1):
            ones += 1
        else:
            zeroes += 1
        n>>=1
    print("NUmber of ones=", ones, "\nNumbers of zeroes=",zeroes)
numbers =int(input("Enter your number "))
binary_string = bin(numbers)
binary= binary_string.replace('0b',' ')
print("binary value",binary)
numberOfBits(numbers)