#coding=UTF-8
'''
如果一个整数比如123，将每个数字拆开后，可以构成两组数之和相等的整数称为‘好数’,{1,2}与{3},两组数之和都为3
现给出一个范围[l,n]，要求输出该范围内的好数的个数
输入：第一行为l n
输出：好数的个数
例：输入：1 50
       输出：4
'''
def is_sum_exist(a, n):
    for i in range(len(a)-1, -1, -1):
        if is_sum_exist(a[: i], n-a[i]) or n-a[i] == 0:
            return True
    return False

def is_good_number(x):
    x = list(map(int, str(x)))
    if sum(x) % 2 != 0:
        return False
    half = sum(x)//2
    if max(x) > half:
        return False
    return is_sum_exist(x, half)

def getGoodNumberCounts(low, high):
    count = 0
    for i in range(low, high+1):
        if is_good_number(i):
            count += 1
    return count

print(getGoodNumberCounts(1,10000))