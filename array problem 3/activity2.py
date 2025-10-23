def pushzerotoend(a,a_size):
    zero = 0
    nonzero = 0
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero += 1
        nonzero += 1
a=[1,0,1,0,0,455,1,8,34,0,1,0,0,1,1]
a_size = len(a)
print(a)
pushzerotoend(a,a_size)
print("array after pushing all zero's to the end of the array:")
print(a)