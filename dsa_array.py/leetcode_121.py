"""
Leetcode :- 121
Best time to buy and sell a stock
"""

# prices = [7, 2, 1, 5, 6, 4, 8]    #in output return the maximum profit here i.e. (8 - 1) = 7

# Brute Force 
prices = [7, 2, 1, 5, 6, 4, 8]
n = len(prices)
max_profit = 0
maxi = 0

for i in range(0, n-1):
    for j in range(i+1, n):
        if prices[j] - prices[i] > 0:
            max_profit = prices[j] - prices[i]
            maxi = max(maxi , max_profit)

        elif prices[j] - prices[i] < 0:
            max_profit = 0

print("maximum profit is:" , maxi)   # T.C ~ O(n2)


# Optimal Solution

prices = [7, 2, 1, 5, 6, 4, 8]
max_profit = 0
min_price = float("inf")

for i in range(0, len(prices)):
    min_price = min(min_price, prices[i])
    max_profit = max(max_profit , prices[i] - min_price)

print("Maximum Profit is =", max_profit)      # T.C = O(n)