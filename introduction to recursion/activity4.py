def print_number(n):
    if (n<= 10):
        print(n)
        print_number(n+1)
    else:
        return

print_number(1)