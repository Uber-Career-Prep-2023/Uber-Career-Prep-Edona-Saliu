"""
Time spent: 15 mins
Approach: DP
Time Complexity: O(n*amount)
Space Complexity: O(amount)

"""

def coinchange(coins, amount):
    changes = (amount + 1)* [0]
    changes[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            changes[i] += changes[i - coin]

    return changes[amount]

print(coinchange([3,7,20], 20))
print(coinchange([1, 6, 10], 15))