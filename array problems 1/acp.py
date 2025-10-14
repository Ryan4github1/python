def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    array_sum = sum(arr)
    return total_sum - array_sum

n = int(input("Enter n: "))
arr = list(map(int, input("Enter the numbers separated by space: ").split()))
print("The missing number is:", find_missing_number(arr, n))