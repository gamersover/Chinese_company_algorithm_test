#coding:utf-8
"""
问题描述：在8*8的棋盘上，放置8个皇后，使得8个皇后不互相攻击，一共有多少中解法
思路：显然每一行只能放置一个皇后，使用A[i] = Xi表示第i个皇后放置在Xi位置上，
假设已经将A[0] = X0,..A[i-1] = X(i-1),求A[i]可能的取值。
将A[i]可能的取值从0-7遍历，假设A[i]=Xi,判断是否会攻击，如果不会寻找下一行，如果会，寻找下一个位置
"""
count = 0
def queue(A, cur):
    global count
    if(8==cur):
        print(A)
        count += 1
        return
    for i in range(8):
        A[cur], flag = i, True
        for j in range(cur):
            if A[j] == i or abs(i-A[j]) == cur - j:
                flag = False
        if flag:
            queue(A, cur+1)

queue([None]*8, 0)
print(count)
                
            