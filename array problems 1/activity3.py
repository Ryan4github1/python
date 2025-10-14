def rotate(a, k, n):
    k = k % n
    def reverse_subarray(arr, start, end):
        while start < end:
            arr[start], arr[end], = arr[end], arr[start]
            start += 1
            end -= 1
    reverse_subarray(a, 0, n-1)
    reverse_subarray(a, 0, k-1)
    reverse_subarray(a, k, n-1)
    return a
arr=[1,2,3,4,5]
k=3
n=len(arr)
print("after rotating by,",k,":",rotate (arr,k,n))