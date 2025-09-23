def arraytotalsum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0] + arraytotalsum(a[1:])
a =[ 1, 2, 1111111, 9999999]
print("Array total sum: ", arraytotalsum(a))
