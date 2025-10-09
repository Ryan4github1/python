import array as arr
a = arr.array('i',[6,5,3,7])
print(a)
sum=0
for i in range(len(a)):
    sum=sum+a[i]
print("mean=",sum/len(a))