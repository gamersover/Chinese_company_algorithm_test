#-*- coding:utf-8 -*-
"""
test37的另一个问题:从前往后数与从后往前数，1的个数都要大于0个数，这样的数组有多少个？
"""

'''
愚蠢的方法：先求出满足从前往后数满足的所有数组S0，再求出从后往前数满足的所有数组S1，求S0与S1的并集
'''

S0 = set()
def pre_generate(A, n_0, n_1, i):
    if i >= len(A):
        global S0
        S0.add(''.join(map(str, A)))
#         print(A)
        return
    if n_1 > n_0: 
        A[i] = 0
        pre_generate(A, n_0+1, n_1, i+1) 
    A[i] = 1                          
    pre_generate(A, n_0, n_1+1, i+1)

S1 = set()
def post_generate(A, n_0, n_1, i):
    if i < 0:
        global S1
        S1.add(''.join(map(str, A)))
#         print(A)
        return
    if n_1 > n_0: 
        A[i] = 0
        post_generate(A, n_0+1, n_1, i-1) 
    A[i] = 1                          
    post_generate(A, n_0, n_1+1, i-1)

A = [0]*9
pre_generate(A, 0, 0, 0)
post_generate(A, 0, 0, len(A)-1)
s = S0 & S1
print(len(s))
# print(s)