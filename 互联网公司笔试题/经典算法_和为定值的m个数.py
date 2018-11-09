# -*- coding:utf-8 -*-
"""
问题描述:从1，2，...n，这n个整数中取出m个数之和为s，求所有可能情况
思路:1.列表中添加n,在1..n-1中寻找和为s-n的多个数
2.列表中不添加n,在1.。n-1中寻找和为s的多个数
"""
li = []
def sumofk(s, n):
    if n <= 0 or s <= 0:
        return 
    if s == n:
        print(*li, n)
    li.append(n)
    sumofk(s-n, n-1)
    li.pop()
    sumofk(s, n-1)

sumofk(8, 7)