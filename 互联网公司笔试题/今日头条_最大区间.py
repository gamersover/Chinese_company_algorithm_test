#coding=UTF-8
'''
给定一个数组序列，需要求选出一个区间，使得该区间是所有区间中经过如下计算的值最大的一个：
区间中的最小值*区间所有数的总和，最后程序输出经过计算后的最大值即可，不需要输出具体的区间，如给定序列[6,2,1],
则根据上述公式，可得到所有可以选定的各个区间的计算值
[6] = 6*6 = 36
[2] = 2*2 = 4
[1] = 1*1 = 1
[6,2] = 2*8 = 16
[2,1] = 1*3 = 3
[6,2,1] = 1*9 = 9
从上述计算可见选定区间[6],计算值为36
输入描述：第一行输入数组序列长度n，第二行输入数组序列
例： 输入
3
6 2 1
输出
36
思路：对于某个数，找到一个区间，该区间最小值是该数的，计算该区间的值，遍历每个数，找到最大区间
'''
def maxRegion(arr):
    max_value = 0    
    for i in range(len(arr)):
        sum_a = arr[i]
        k = 1
        while i+k < len(arr):
            if arr[i+k] >= arr[i]:
                sum_a += arr[i+k]
                k+=1
            else:
                break
        
        k = 1 
        while i-k >=0:
            if arr[i-k] >= arr[i]:
                sum_a += arr[i-k]
                k+=1
            else:
                break
            
        max_value = max(sum_a*arr[i], max_value)
    return max_value

arr = [6,2,1]
print(maxRegion(arr))