def longest_consecutive_ones(n):
    binary=bin(n)[2:]
    longest=max(binary.split('0'))
    return len(longest)

n= int(input("Enter a number: "))
print("Longest consecutive 1:",longest_consecutive_ones(n))