def cube(n):
    return n**3
def div (n):
    if n%3==0:
        return cube(n)
    else:
        print("this no is not divisible by 3")
number=int(input("Enter the no:"))
answer=div(number)
print(answer)