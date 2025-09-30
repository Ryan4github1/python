def ways(money):
    if money < 0:
        return 0
    if money == 0:
        return 1
    totalways = 0
    for take in range(1, money+1):
        totalways += ways(money - take)
    return totalways

money = int(input("enter the amount of money: "))
print("number of ways to divide : ", ways(money))