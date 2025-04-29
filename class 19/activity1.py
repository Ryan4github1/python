lst=[]
print(lst)
lst=[1,2,3,4,5,6,7,8,9,10,15,30,90]
print(lst)
print("no of items on lst=",len(lst))
print(lst[3])
print("count:",lst.count(6))
lst[2]=25
print(lst)
lst.pop
print("list after removing last element:",lst)
lst.append(100)
print("list after adding elemnt:",lst)
lst.remove(25)
print("list after removing elemnt",lst)
lst.insert(1,90)
print("list after adding element:",lst)
print("reverse lst:",lst[::-1])
lst.sort()
print("sort in ascending order:",lst)
lst.reverse()
print("sort in descending order:",lst)