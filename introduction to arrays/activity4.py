arr = [82,45,74]
first = second = float('-inf')
for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("First:", first)
print("Second:", second)