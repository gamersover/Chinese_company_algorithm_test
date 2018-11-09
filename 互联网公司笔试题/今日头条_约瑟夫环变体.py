# coding:utf-8
"""
n个人，编号为0 1 2 ..., 
A数组含有m个数，循环取A数组中的数，作为约瑟夫环的步长，每次删掉走到的那个数，
求最后剩下的那个数

比如有4个人，0 1 2 3
数组A = [3, 1]
第一次取3，走到第三个数为2，删掉2后变为0 1 3，下一个数是3
第二次去1，删掉从3开始的第一个数，就是3，变为0 1，下一个数是0
第三次去循环接着取3，删掉从0开始的第3个数，就是0，则最后剩下1，输出1

通过70%！！！
"""

def getLast(n, m, A):
	arr = [i for i in range(n)]
	curr = 0
	for i in range(n-1):
		idx = (curr + A[i % m]-1) % len(arr)
		del arr[idx]
		curr = idx
	return arr[0]
	

N = int(input())
for i in range(N):
	inp = [int(j) for j in input().split()]
	n, m = inp[0], inp[1]
	A = inp[2:]
	print(getLast(n, m, A))