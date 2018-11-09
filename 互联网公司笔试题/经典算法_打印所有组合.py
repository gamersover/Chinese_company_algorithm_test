# coding:utf-8
"""
经典题：打印所有组合
思路：f(1234) = 1 + f(234), f(234)
1作为前缀，求234的组合，
2作为前缀, 求34的组合
3作为前缀，求4的组合
"""
def listAll(a, prefix):
	if len(a) == 0:
		print(prefix)
    
	for i in range(len(a)):
		listAll(a[i+1:], prefix+a[i])


a = ['1', '2', '3', '4']
listAll(a, "")
