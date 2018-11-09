# coding:utf-8
"""
经典题：最少硬币找零问题
假设硬币的价值为1,3,5,9,10， 每种硬币可以取无限个，如何用若干种硬币组合为某种面额的钱，使得
硬币的个数最少？
两种方法：1.dp[j] = min(dp[j], dp[j-coins[i-1]]+1) 与01背包问题相似
2.dp[j] = min(dp[j-coins[i]]) + 1 for i in range(1, N+1)
"""
def CoinsZero(N, V, coins):
    dp = [float('inf') for j in range(V+1)]
    dp[0] = 0
    for i in range(1, N+1):
        for j in range(coins[i-1], V+1):
            dp[j] = min(dp[j], dp[j-coins[i-1]]+1)
    return dp[V]


N = 5
V = 14
coins = [9,3,1,5,10]
print(CoinsZero(N, V, coins))