"""
 序列中任意个连续的元素组成的子序列称为该序列的子串。
现在给你一个序列P和一个整数K，询问元素和是K的倍数的子串的最大长度。
比如序列【1,2,3,4,5】，给定整数K为5，其中满足条件的子串为{5},{2,3},{1,2,3,4},{1,2,3,4,5}
那么答案就是5
输入：第一行含一个整数N,第二行包含N个整数，第三行包含一个整数K，
"""
def get_max_len(arr, n, k):
    dp = [[0 for i in range(n)] for j in range(n)]

    for j in range(n):
        dp[n-1][0] += arr[j]

    if dp[n-1][0] % k == 0:
        return n

    for i in range(n-2, -1, -1):
        for j in range(n-i):
            if j == 0:
                dp[i][j] = dp[i+1][j] - arr[i+1]
            else:
                dp[i][j] = dp[i+1][j-1] - arr[j-1]
            if dp[i][j] % 5 == 0:
                return i+1
    return 0

if __name__ == '__main__':
    arr = [1, 2]
    n = len(arr)
    k = 5
    print(get_max_len(arr, n, k))