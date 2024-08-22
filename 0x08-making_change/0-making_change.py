#!/usr/bin/python3
"""Making Change - Coin Change Problem"""


def makeChange(coins, total):
    """function that returns the fewest number of coins needed to meet
    the total
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1