# -*- coding:utf-8 -*-
"""
经典算法：最长公共子序列
问题：从序列A中按照顺序抽取若干项组成的新序列成为子序列，C是两个序列A,B的公共子序列是指C既是A的子序列，又是B
子序列，最长公共子序列就是指子序列中最长的，给定两个序列A,B，求最长公共子序列的长度
思路：动态规划，记a1,a2,...,ai与b1,b2,..,bj的最长公共子序列长度为LCS(i,j),
1.如果ai = bj,有a1,a2,..,a(i-1)与b1,b2,..,b(j-1)的最长公共子序列长度为LCS(i-1,j-1)，
又因为ai=bj，所以LCS(i,j) = LCS(i-1, j-1) + 1
2.如果ai!=bj，则LCS(i,j)要不等于LCS(i-1,j)，要不等于LCS(i,j-1)
"""

def get_lcs(a,b):
    len_a = len(a)
    len_b = len(b)
    lcs = [[0 for i in range(len_b+1)] for j in range(len_a+1)]
    for i in range(len_a+1):
        for j in range(len_b+1):
            if i==0 or j==0:
                lcs[i][j] = 0
            elif a[i-1] == b[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            elif a[i-1] != b[j-1]:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])
    print(lcs[len_a][len_b])

if __name__ == "__main__":
    a = 'abfgedgeg'
    b = 'afegm'
    get_lcs(a, b)