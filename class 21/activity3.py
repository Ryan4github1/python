test_dict={'id1':45,'id2':95,'id3':45,'id4':62,'id5':84,'id6':45,'id7':39,'id8':75,'id9':45,}
print("original dictionary:",test_dict,"n")
K=int(input("Enter the number to count:"))
res = 0
for key in test_dict:
    if test_dict[key] == K:
        res = res+1
print("No of times",K,"is present in the dictionary:",res)