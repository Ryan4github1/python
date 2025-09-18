def incdec(n,num):
    if (n<1 or n>num):
        return
    print(n)
    incdec(n-1,num)
    print(n)
num=int(input("Enter any number n: "))
incdec(num,num)