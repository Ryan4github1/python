def reverse_bits(num):
    result = 0
    while num > 0:
        result = (result << 1) | (num & 1)
        num >>= 1
    return result

n = int(input("Enter a number: "))
rev = reverse_bits(n)
print("Reversed bits number =", rev)