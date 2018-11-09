# coding:utf-8
"""
经典题：拼凑面额
描述：给你六种面额1、5、10、20、50、100元的纸币，
假设每种币值的数量都足够多，编写程序求组成N员（N为0-10000的非负整数）的不同组合的个数
"""
def CoinsNumber(N, coins):
    dp = [0 for j in range(N+1)]
    dp[0] = 1
    for i in range(1, len(coins)+1):
        for j in range(coins[i-1], N+1):
            dp[j] += dp[j-coins[i-1]]
    return dp[N]


N = 100
coins = [1,5,10,20,50,100]
print(CoinsNumber(N, coins))