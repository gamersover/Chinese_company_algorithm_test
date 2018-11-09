#coding:utf-8
"""
经典题： 第一个缺失的正整数
描述：给出一个数组，求出该数组中第一个缺失的正整数
思路：对于数组中的元素a[i], 判断在a[i]-1位置上的元素是否是a[i],即a[i]==a[a[i]-1]?
"""
def find_first_number(arr):
    i = 0
    N = len(arr)
    while i < N:
        if arr[i] == i + 1:
            i += 1
        else:
            if 1 <= arr[i] <= N and arr[i] != arr[arr[i] - 1]:
                swap_a, swap_b = i, arr[i] -1
                arr[swap_a], arr[swap_b] = a[swap_b], a[swap_a]
            else:
                i += 1

    for i in range(N):
        if arr[i] != i + 1:
            return i + 1
    return N + 1


a = [2, 2, -3, 1]
print(find_first_number(a))