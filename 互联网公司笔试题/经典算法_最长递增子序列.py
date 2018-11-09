# -*- coding:utf-8 -*-
"""
问题：找出一个数字序列中最长递增序列的长度
思路1：动态规划，假设序列61728345，用一个b数组记录每个数字当前的升序数
比如6的升序数为1,1的升序数为1,2的升序数为2，
假设已经知道前面0，i-1的升序数，现在i的升序数，只需要在i的前面从右往左找，
从i-1,i-2,..0找，找个第一个比第i个数小的,比如说j，则b[i]=b[j]+1,
如果没有找到，则b[i]=1
思路2：比如67128345，先排序12345678，然后求这两个序列的最长公共子序列就可以
思路3：最好的思路，维护一个数组B,其中数组表示递增序列长度为i的最小末尾数是多少？数组B作如下操作：
首先B[0] = [6]，表示LIS长度为1的最小末尾数为6，然后取7,7插入到B数组中的位置是1，所以
B[1] = 7,表示LIS长度为2的最小末尾数为7，此时B=[6,7],然后取1，1插入到B中的位置是0，
此时B[0]=6,因为1<6，所以B[0]=1,表示LIS为1的最小末尾数为1，此时B=[1,7],
然后取2,2插入到B中的位置是1，而2<B[1]=7，所以B[1]=2,此时B=[1,2],
依此类推，知道取5时，B=[1,2,3,4],5插入到B中位置为4，所以B[4]=5,
B的角标一直到了4，所以LIS的长度为5.注意：B中数组的值不一定是LIS。
插入到B中，原来B数组有序，所以可以用二分查找，复杂度降低到O(NlogN)
"""
# 思路一
def get_lis(a):
    b = [1]*len(a)
    max_len = b[0]
    for i in range(len(a)):
        for j in range(i,-1,-1):
            if a[j]<a[i]:
                b[i] = b[j] + 1
                break
        if b[i] > max_len:
            max_len = b[i]
    return max_len

# 思路二
def binary_insert(b, item):
    start = 0
    end = len(b)
    while start<end:
        mid = (start+end)>>1
        if b[mid]==item:
            return mid
        if b[mid]>item:
            end = mid
        else:
            start = mid+1
    return end

def get_lis2(a):
    b = []
    b.append(a[0])
    for i in range(1, len(a)):
        index = binary_insert(b, a[i])
        if index == len(b):
            b.append(a[i])
        elif b[index] > a[i]:
                b[index] = a[i]
    return len(b)

a = '67128345'
# print(get_lis(a))
print(get_lis2(a))


