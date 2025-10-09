# a=[4,5,6,7,8,9,10]
# print("maximum number is: ",max(a))
# print("minimum number is; ",minimum(a))
def minimum(arr,size):
    temp=arr[0]
    for i in range(1,size):
        temp=min(temp,arr[i])
    return temp
def maximum(arr,size):
    temp=arr[0]
    for i in range(1,size):
        temp=max(temp,arr[i])
    return temp
arr=[2,3,4,5,6,7,8,9,10]
size=len(arr)
print(minimum(arr,size))
print(maximum(arr,size))