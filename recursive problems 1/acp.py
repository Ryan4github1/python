def power(base, num):
    if num == 0:
        return 1
    return base * power(base, num - 1)

b = int(input("Enter the base: "))
e = int(input("Enter the power: "))
print(power(b, e))