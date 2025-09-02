def powerof2(number):
    if number <=0:
        return False
    return (number &(number - 1)) == 0
n = int(input("Enter a number: "))
if powerof2(n):
    print("\nThe number is power of 2")
else:
    print("\nThe number is not power of 2")
    