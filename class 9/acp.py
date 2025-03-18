num = int(input("Enter a digit number: "))
noofdigits=0
t=num
while t > 0:
    x = t % 10
    noofdigits+=1
    t //= 10
if num==sum:
    print("this is an armstrong number")
else:
    print("this is not an armstrong number")