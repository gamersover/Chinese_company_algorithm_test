# coding:utf-8
"""
小易非常喜欢拥有以下性质的数列:
1、数列的长度为n
2、数列中的每个数都在1到k之间(包括1和k)
3、对于位置相邻的两个数A和B(A在B前),都满足(A <= B)或(A mod B != 0)(满足其一即可)
例如,当n = 4, k = 7
那么{1,7,7,2},它的长度是4,所有数字也在1到7范围内,并且满足第三条性质,所以小易是喜欢这个数列的
但是小易不喜欢{4,4,4,2}这个数列。小易给出n和k,希望你能帮他求出有多少个是他会喜欢的数列。 
输入描述:
输入包括两个整数n和k(1 ≤ n ≤ 10, 1 ≤ k ≤ 10^5)


输出描述:
输出一个整数,即满足要求的数列个数,因为答案可能很大,输出对1,000,000,007取模的结果。

输入例子1:
2 2

输出例子1:
3
思路：动态规划，dp[i][j]表示长度为i，最后一位是j的数列的个数
dp[i][j] = dp[i-1][1] + dp[i-1][2] + ... + dp[i][j] 最后一位小于j的
           + dp[i-1][j+1] + dp[i-1][m] + ... m表示不能被j整除的，
"""
n = 10
k = 100
dp = [[0 for i in range(k+1)] for i in range(n+1)]
for j in range(1, k+1):
    dp[1][j] = 1

# # 第一种思路：计算不能被j整除的
# for i in range(2, n+1):
#     for j in range(1, k+1):
#         for m in range(1, j+1):
#             dp[i][j] += dp[i-1][m]
#             dp[i][j] %= 1000000007
#         for m in range(j+1, k+1, 1):
#             if m % j != 0:
#                 dp[i][j] += dp[i-1][m]
#                 dp[i][j] %= 1000000007

# 第二种，先计算所有的，再减去能被j整除的
for i in range(2, n+1):
    for j in range(1, k+1):
        sum1 = 0
        for m in range(1, k+1):
            sum1 += dp[i-1][m]
            sum1 %= 1000000007
        sum2 = 0
        for m in range(j+j, k+1, j):
            sum2 += dp[i-1][m]
            sum2 %= 1000000007
        dp[i][j] = (sum1 - sum2 + 1000000007) % 1000000007

res = 0
for j in range(1, k+1):
    res += dp[n][j]
    res %= 1000000007
print(res)