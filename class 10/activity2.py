word=input("Enter the word:")
letter=input("Enter the character:")
cnt=0
for i in word:
    if letter==i:
        cnt=cnt+1
print("No of times",letter,"present in the ",word,"=",cnt)