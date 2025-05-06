dic={'id1':45,'id2':95,'id3':45,'id4':62,'id5':84,'id6':45,'id7':39,'id8':75,'id9':45,}
print("original dictionary:", dic,"n")
res={}
for key, value in dic.items():
    if value not in res.values():
        res[key]=value
print("after removing duplicates:",res)