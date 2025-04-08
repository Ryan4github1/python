word=input("Enter the word: ")
letter=input("enter a letter: ")
for i in word:
    if i==letter:
        print("found")
        break
else:
    print("not found")