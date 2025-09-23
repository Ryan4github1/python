def maxelementarray(a):
    length = len(a)
    if length == 1:
        return a[0]
    return max(a[0], maxelementarray(a[1:]))
a = [ 989, 454, 292, 676, 898, 373, 999]
print("largest elemtn of array: ",maxelementarray(a))
