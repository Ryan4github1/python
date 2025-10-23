def sort012(arr):
    zero = arr.count(0)
    one = arr.count(1)
    two = arr.count(2)
    return [0]*zero + [1]*one + [2]*two

arr = [2, 0, 1, 2, 1, 0]
print("Sorted array:", sort012(arr))