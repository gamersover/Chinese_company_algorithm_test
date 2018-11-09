#-*- coding:utf-8 -*-
"""
递归求解组合问题
"""

def combination(a, n):
    if n == len(a):
        return [a]
    elif n == 1:
        return [[i] for i in a]
    else:
        return [[a[0]] + i for i in combination(a[1:], n-1)] + [i for i in combination(a[1:], n)]

a = ['A', 'B', 'C', 'D', 'E']
print(len(combination(a, 3)))
print(*combination(a, 3), sep='\n')