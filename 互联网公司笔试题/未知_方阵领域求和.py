#coding=UTF-8
'''
给定一个n阶方阵s，和一个数r(0<=r<=n)。要求输出一个方阵w,其中w中的第i行，第j列的元素的值为
方阵s中的第i行，第j列的元素的距离小于等于r的元素的和;
其中A(ij)到A(mk)的距离为max(|i-m|,|j-k|)
输入：第一行为n r，后面为方阵s
输出：方阵w
例:输入：
3 1
1 1 0
0 1 1
1 1 1
输出：
3 4 3
5 7 5
3 5 4
'''
def getMatrix_w(s, n, r):
    for i in range(n):
        for j in range(n):
            v = 0
            for k in range(max(0, i-r), min(n, i+r+1)):
                for m in range(max(0, j-r), min(n, j+r+1)):
                    v += s[k][m]
            if j == n-1:
                print(v)
            else:
                print(v, end=" ")

s = [[1,1,0], [0,1,1], [1,1,1]]
n = 3
r = 1
getMatrix_w(s, n, r)