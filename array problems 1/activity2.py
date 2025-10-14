def reverse(a,a_size,n):
    temp=0
    while (temp<a_size):
        start = temp
        end = min(temp+n-1,a_size-1)
        while (start<end):
            a[start],a[end]=a[end],a[start]
            start += 1;
            end -= 1
        temp += n
a=[5,2,5678,32,56,98,14,6153,731]
n=2
a_size = len(a)
reverse(a,a_size,n)
print(a)