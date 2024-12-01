#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The total amount to reach.

    Returns:
        int: The fewest number of coins needed to meet the total.
             Returns 0 if total is 0 or less.
             Returns -1 if the total cannot be met by any combination of coins.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

if __name__ == "__main__":
    coins = [1, 6, 10]
    total = 37
    print(makeChange(coins, total))  
