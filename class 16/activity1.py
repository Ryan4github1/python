try:
    k=int(input("put in the number"))
    p=int(input("put in a number"))
    print(k/p)
    if p==0:
        raise ZeroDivisionError
except ZeroDivisionError:
    print("the second number should not be zero")
finally:
    print("thank you")