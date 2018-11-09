#coding:utf-8
"""
经典题：01背包问题
"""
def ZeroOnePack(N, V, weight, value):
    """
    经典背包问题，每个物品只有一个
    """
    dp = [[0 for j in range(V+1)] for i in range(N+1)]
    for i in range(1, N+1):
        for j in range(weight[i-1], V+1):
            # 第i个物品可以选择放或者不放
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]]+value[i-1])
    max_value = dp[N][V]
    return max_value

def ZeroOnePack_2(N, V, weight, value):
    """
    经典背包问题：空间优化
    """
    dp = [0 for j in range(V+1)]
    for i in range(1, N+1):
        # 容量倒序，是为了防止dp[j-weigh[i-1]]取了当前时刻的值，会造成每个物品不止取了一次
        for j in range(V, weight[i-1]-1,-1):
            dp[j] = max(dp[j], dp[j-weight[i-1]]+value[i-1])
    return dp[V]

def ZeroOnePack_3(N, V, weight, value):
    """
    完全背包问题：每个物品可以使用无限次
    """
    dp = [0 for j in range(V+1)]
    for i in range(1, N+1):
        # 容量正序，与zeroonepack正好相反，这样可以使得每个物品不止取一次
        for j in range(weight[i-1], V+1):
            dp[j] = max(dp[j], dp[j-weight[i-1]]+value[i-1])
    return dp[V]

def MultiZeroOnePack(N, V, weight, value, number):
    """
    多重背包问题：每个问题取得个数有上限
    """
    dp = [0 for i in range(V+1)]
    for i in range(1, N+1):
        for j in range(V, weight[i-1]-1, -1):
            max_ = dp[j]
            for k in range(1, number[i-1]+1):
                if k <= j // weight[i-1]:
                    max_ = max(dp[j-k*weight[i-1]] + k*value[i-1], max_)
            dp[j] = max_
    return dp[V]

N = 3
V = 8
weight = [1,2,2]
value = [6,10,20]
number = [10,5,2]
print(MultiZeroOnePack(N, V, weight, value, number))