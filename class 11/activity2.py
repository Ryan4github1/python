row=int(input("enter the amount of rows: "))
n=1
for i in range(row):
    for j in range(i+1):
        print(n, end=' ')
        n+=1
    print()