#!/usr/bin/python3
"""
Function to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        count = total // coin
        num_coins += count
        total -= coin * count
    
    return num_coins if total == 0 else -1

# Example usage:
# print(makeChange([1, 2, 25], 37))  # Output: 7
# print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

