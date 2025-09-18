def headrec(n):
    if n!=0:
        headrec(n-1)
        print(n)
x=int(input("Enter the number:" ))
headrec(x)
