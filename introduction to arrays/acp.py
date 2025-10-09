def reversearray(a):
    rev = []
    for i in range(len(a)-1, -1, -1):
        rev.append(a[i])
    return rev

a = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Reversed array:", reversearray(a))