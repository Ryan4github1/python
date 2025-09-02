def powerof4(number):
    if number <=0 or (number &( number -1)) !=0:
        return False
    return (number & 0x55555555) !=0
n=int(input("Enter a number: "))
if powerof4(n):
    print("\nThis number is power of 4")
else:
    print("\nThis number is not power of 4")
    