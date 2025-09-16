def linear_recursion(n):
    if n == 0:
        return 0
    return n + linear_recursion(n-1)
n = int(input("Enter a number: "))
print("Linear recursion result:", linear_recursion(n))