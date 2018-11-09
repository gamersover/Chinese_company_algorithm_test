#coding:utf-8
"""
2**a + 2**b - 2**c二进制表示中1的个数
假设结果是大于0的
"""

def solution(a, b, c):
    if c==a:
        return 1
    else:
        return b+1-c
    

if __name__ == "__main__":
    a, b, c = [int(i) for i in input().split()]
    print(solution(a, b, c))
    