#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """return the  fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    num_change = 0
    sum_change = 0

    for i in coins:
        while sum_change < total:
            sum_change += i 
            num_change += 1
        if sum_change == total:
            return num_change
        sum_change -= i
        num_change -= 1
    return -1
