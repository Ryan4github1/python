numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers_1, numbers_2)
print("Addition of two lists")
print(list(result))

nums = [1, 2, 3, 4, 5, 6]
def sq(n):
    return n*n
square = list(map(sq,nums))
print("square of numbers in the list")
print(square)