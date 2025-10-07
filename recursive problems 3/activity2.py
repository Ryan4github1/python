keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def printcombination(combination, curr, output, n):
    if(curr == n):
        print(*output,sep=",")
        return
    # print all the possible combination by iterating first 1 to 3 for number an finding that index in keypad.
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printcombination(combination,curr + 1, output, n)#recursive call
        output.pop()
        if(combination[curr] == 0 or combination[curr] == 1):
            return


combination = [3,2,2]
n = len(combination)
printcombination(combination, 0, [], n)