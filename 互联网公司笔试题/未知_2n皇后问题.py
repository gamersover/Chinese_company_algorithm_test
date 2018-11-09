#coding=UTF-8
'''
给定一个n*n的棋盘，棋盘中有一些位置不能放皇后，现在要向棋盘中放入n个黑皇后和n个白皇后，使得任意两个黑皇后不在同一行、
同一列或同一条对角线上，任意的两个白皇后都不在同一行、同一列或同一条对角线上。问总共有多少种放法？，n<=8
输入描述：
输入的第一行为一个整数n，表示棋盘的大小。接下来的n行，每行n个0或1，如果一个整数为1，表示对应的位置可以放皇后，
如果一个整数为0，表示对应的位置不可以放皇后。
输出描述：
输出一个整数，表示总共有多少中放法
示例:
4
1 1 1 1
1 0 1 1
1 1 1 1
1 1 1 1
思路：八皇后问题改版
'''

def is_safe(i, j, grid, cur, white, black):
    if i == j or grid[cur][i] == 0 or grid[cur][j] == 0:
        return False
    for k in range(cur):
        if white[k] == i or abs(white[k] - i) == cur - k:
            return False 
        if black[k] == j or abs(black[k] - j) == cur - k:
            return False
    return True

def queue(white, black, cur, n, grid):
    global count
    if cur == n:
        count += 1
        return
    for i in range(n):
        for j in range(n):
            white[cur], black[cur] = i, j
            flag = is_safe(i, j, grid, cur, white, black)
            if flag:
                queue(white, black, cur+1, n, grid)

n = 4
grid = [[1,0,1,1], [1,1,1,1], [1,1,1,1], [1,1,1,1]]
white = [None for i in range(n)]
black = [None for i in range(n)]
cur = 0
count = 0
queue(white, black, cur, n, grid)
print(count)
            