#coding=UTF-8
'''
小易老师是非常严厉的,它会要求所有学生在进入教室前都排成一列,并且他要求学生按照身高不递减的顺序排列。
有一次,n个学生在列队的时候,小易老师正好去卫生间了。学生们终于有机会反击了,于是学生们决定来一次疯狂的队列,
他们定义一个队列的疯狂值为每对相邻排列学生身高差的绝对值总和。
由于按照身高顺序排列的队列的疯狂值是最小的,他们当然决定按照疯狂值最大的顺序来进行列队。
现在给出n个学生的身高,请计算出这些学生列队的最大可能的疯狂值。小易老师回来一定会气得半死。 

当队列排列顺序是: 25-10-40-5-25, 身高差绝对值的总和为15+30+35+20=100。
这是最大的疯狂值了。

输入例子1:
5
5 10 25 40 25

输出例子1:
100
思路:1.先将队列排序，用0，1，2，3，..表示排序后的下标
2.将最小的数放在中间，然后将最大的两个数放在最小数的旁边，接着再将次小的两个数放在两个最大数的旁边
比如0,1,2,3,4,5,6：
0
5 0 6
2 5 0 6 1
3 2 5 0 6 1 4
3.当队列长度为奇数时，按照步骤2放，可以完成
4.当队列长度n为偶数时，可以去掉最后添加的元素，之后按2的步骤执行
5.执行2步骤有以下规律  i N-i... 4 N-4 2 N-2 0 N-1 1 ... N-3 3 N-j, j
  从0的右边从左往右分别是N-j,j,其中j=1,3,5,7..
  从0的左边从右往左分别是N-i,i,其中i=2,4,6,8..
'''
def crazy_number(arr):
    arr.sort()
    # 判断序列长度为偶数还是奇数，并求出最后添加的那个下标left
    if len(arr) %2 == 0:
        crazy = [0]*(len(arr) - 1)
        left = len(arr) // 2
        if left % 2 == 0:
            left -= 1
    else:
        crazy = [0]*len(arr)
        left = None

    # 处理中间
    crazy[len(crazy)//2] = arr[0]
    # 处理中间的左边
    idx = 2
    for i in range(len(crazy)//2-1, -1, -2):
        crazy[i] = arr[len(arr) - idx] 
        if i - 1 >= 0:
            crazy[i-1] = arr[idx]
        idx += 2
    # 处理中间的右边
    idx = 1
    for i in range(len(crazy)//2+1, len(crazy), 2):
        crazy[i] = arr[len(arr) - idx]
        if i + 1 < len(crazy):
            crazy[i+1] = arr[idx]
        idx += 2

    number = 0
    for i in range(len(crazy)-1):
        number += abs(crazy[i+1] - crazy[i])
    # 处理最后一个添加的数
    if left is not None:
        number += max(abs(arr[left]-crazy[0]), abs(arr[left]-crazy[-1]))
    return number

print(crazy_number([0,1,2,3,4,5,6,7]))
            
        
          



     