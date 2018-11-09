# -*- coding:utf-8 -*-
"""
经典算法：最长公共子串
问题：是最长公共子序列的特例问题，子串就是连续的子序列
思路：动态规划，全局的最长长度记为max_length
记a1,a2,...,ai与b1,b2,..,bj的最长公共子串长度为LCS(i,j),
1.如果ai = bj,有a1,a2,..,a(i-1)与b1,b2,..,b(j-1)的最长公共子序列长度为LCS(i-1,j-1)，
又因为ai=bj，所以LCS(i,j) = LCS(i-1, j-1) + 1
2.如果ai!=bj，判断前面公共子串的长度LCS(i-1,j-1)和max_length的大小，如果前者大于后者，更新max_length,
然后LCS[i][j]=0
"""

def get_lcs(a, b):
    max_length = 0
    len_a = len(a)
    len_b = len(b)
    dp = [[0 for i in range(len_b+1)] for i in range(len_a+1)]
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            elif a[i-1] != b[j-1]:
                if dp[i-1][j-1] > max_length:
                    max_length = dp[i-1][j-1]
                dp[i][j] = 0
    return max_length

if __name__ == "__main__":
    a = 'ababdefg'
    b = 'mmm'
    print(get_lcs(a,b))