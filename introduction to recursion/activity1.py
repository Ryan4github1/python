n=int(input("Enter the number:"))
if n==0 or n==1:
    print(1)
else:
    ans=1
    for i in range(2,n+1):
        ans=ans*i
    print("factorial of",n,"is =",ans)
