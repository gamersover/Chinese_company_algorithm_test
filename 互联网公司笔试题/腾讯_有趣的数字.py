# coding:utf-8
"""
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，差最小的有多少对呢？差最大呢？


输入描述:

 输入包含多组测试数据。

 对于每组测试数据：

 N - 本组测试数据有n个数

 a1,a2...an - 需要计算的数据

保证:

 1<=N<=100000,0<=ai<=INT_MAX.
输出描述:

对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。


输入例子1:
6
45 12 45 32 5 6

输出例子1:
1 2
"""
import sys
def printValue(arr, N):
	arr.sort()
	min_arr = []
	min_count, max_count = 0, 0
	for i in range(1, N):
		min_arr.append(arr[i]-arr[i-1])
	if arr[0] == arr[N-1]:
		min_count, max_count = N*(N-1)//2, N*(N-1)//2
	else:
		min_v = min(min_arr)
		if min_v == 0:
			count = 0
			for k in min_arr:
				if k == 0:
					count += 1
				else:
					min_count += (count+1)*count // 2
					count = 0
			min_count += (count+1)*count // 2
		else:
			for k in min_arr:
				if min_v == k:
					min_count += 1
		
		left = 0
		while arr[left] == arr[0]:
			left += 1
		right = 0
		while arr[N-right-1] == arr[N-1]:
			right += 1
		max_count = left*right
	print(min_count, max_count)

	


if __name__ == '__main__':
	while True:
		try:
			N = int(sys.stdin.readline())
			arr = [int(i) for i in sys.stdin.readline().split()]
			printValue(arr, N)
		except:
			break
