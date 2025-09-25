num = int(input("Enter a number: "))
rev = 0
original = num
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print(f"Reverse of {original} is {rev}")