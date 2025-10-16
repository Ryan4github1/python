def maxDifference(arr):
    max_diff = max(arr) - min(arr)
    return max_diff

arr = [2, 8, 1, 10, 5]
print("Maximum difference:", maxDifference(arr))