# coding:utf-8
"""
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。
输入描述:
输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.
输出描述:
对于每组数据，输出一个整数，代表最少需要删除的字符个数。
输入例子1:
abcda
google
输出例子1:
2
2
思路：求出最长回文子串，然后用长度减去最长长度即可
使用动态规划算法求最长回文子串的长度
dp[i][j]表示s[i][j]的最长长度，如果是s[i]==s[j]，表示两端相等，那么就等于中间的最长长度dp[i+1][j-1]加2
如果s[i]!=s[j]，两端字符不相等，则就等于左边与右边的最大值即max(dp[i+1][j], dp[i][j-1])
"""
import sys
def getValue(s):
    dp = [[0 for j in range(len(s))] for i in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                if j-i > 1:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return len(s) - dp[0][len(s)-1]


if __name__ == '__main__':
    while True:
        try:
            s = sys.stdin.readline().strip()
            print(getValue(s))
        except:
            pass
