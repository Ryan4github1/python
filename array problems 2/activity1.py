def calculateprofit(arr,arr_size):
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i-1]
    return profit
prices=[456,123,89,12,869,1902,59472]
profit =calculateprofit(prices,len(prices))
print(profit)