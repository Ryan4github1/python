def tailrec(a,num):
    if (a>num):
        return
    print(a)
    tailrec(a+1,num)
n=int(input(" Enter n to print 1 to n :"))
tailrec(5,n)