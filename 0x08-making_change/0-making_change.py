#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    dp = [float('inf')] * (total + 1)
    
    dp[0] = 0
    
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
