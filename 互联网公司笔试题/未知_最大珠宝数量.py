#coding=UTF-8
'''
现有一张藏宝图，记录了黄金山上从山脚到山顶的每条道路散落的珠宝数量，例如：
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
宝藏猎人需要从山脚到达山顶，那么应该如何选择一条路径，使其获得的珠宝数量最多呢？规定：从山脚到山顶的过程中，宝藏猎人只能
朝左上角或正上方前进。因此示例的路径为5->7->8->3->7，最大值为30
输入描述：
输入数据的第一行代表山的高度N，之后一共有N行数据，且从上到下数第i行有i个整数，代表第i层从左到右每条路径上的珠宝数量。
输出描述：
输出能得到的最大的珠宝数量
示例：输入
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
输出：
30
'''
def getMax(n, a):
    dp = [[0 for i in range(j+1)] for j in range(n)]
    for j in range(n):
        dp[n-1][j] = a[n-1][j]
    
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + a[i][j]
    return max(dp[0])

if __name__ == "__main__":
    a = [[7], [3,8], [8,1,0], [2,7,4,4], [4,5,2,6,5]]
    n = 5
    print(getMax(n, a))

        