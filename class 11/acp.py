r=int(input("enter the amount of rows: "))
k=r-1
for i in range(1,r+1):
    print(""*(k),"*"*i,end=' ')
    k=k-1
    print()