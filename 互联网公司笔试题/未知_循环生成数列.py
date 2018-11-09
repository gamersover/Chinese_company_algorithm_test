#coding=UTF-8
'''
数列a为1 2 3
数列A为1 2 2 3 3 1 1 1 2 2 2 。。。。。数列A中的元素按a中的元素顺序循环生成
其中数列A可以写为[1] [2 2] [3 3] [1 1 1] [2 2 2]
按照每组的长度变为1 2 2 3 3 。。。。。与原数组A一样
要求输入第一行为整数n m,第二行为数列a (m为数列a中元素的个数)
输出：输入数列A的前n项
例：输入 
10 3
3 2 1
输出
3
3
3
2
2
2
1
1
1
3
'''
a = [2,1,3]
n = 10
m = len(a)

number = a[0]
i = 0
A = []
while len(A) < n:
    for j in range(number):
        A.append(a[i % m])
    i += 1
    if i < len(A):
        number = A[i]
    else:
        number = a[i]
print(*A[:n], sep="\n")
    
