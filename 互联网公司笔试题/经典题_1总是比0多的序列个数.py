#-*- coding:utf-8 -*- 
'''
由0和1组成长度为10的数组中，对于满足条件的i(0<i<10),a[0:i]中1的个数总是大于0的个数，
请问这样的数组有多少个
'''


def generate(A, n_0, n_1, i):
    """
    A:生成的数组
    i:第几个位置
    n_0:前i个数中0出现的次数
    n_1:前i个数中1出现的次数
    """
    global a
    if i >= len(A):
        print(A)
        a += 1
        return
    if n_1 > n_0:   #第i个数可以等于0情况，1出现的次数大于0出现的次数
        A[i] = 0
        generate(A, n_0+1, n_1, i+1)  #0的个数加1，1的个数不变，继续求解第i+1个
    A[i] = 1                          
    generate(A, n_0, n_1+1, i+1)      #0的个数不变，1的个数加一，继续求解第i+1个

if __name__ == "__main__":
    a = 0
    A = [0]*5
    generate(A, 0, 0, 0)
    print(a)