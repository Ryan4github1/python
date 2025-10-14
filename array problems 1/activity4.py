def leader(arr, n):
    max_from_right = arr[n - 1]
    print("Leaders in array:", max_from_right, end=" ")
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            print(arr[i], end=" ")
            max_from_right = arr[i]

arr = [6,3,8,2,1]
n = len(arr)
leader(arr, n)