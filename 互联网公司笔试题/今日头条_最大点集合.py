#coding=UTF-8
'''
P为给定的二维平面整数点集，定义P中某点x，如果x满足P中任意点都不在x的右上方区域内(横纵坐标都大于x)，则称
其为'最大的'.求出所有最大点的集合。(所有点的横纵坐标不重复)
例：输入
5
1 2
5 3
4 6
7 5
9 0
输出
4 6
7 5
9 0
思路：首先按照横坐标降序排序，比如[9,0] [7,5], [5,3], [4,6], [1,2]
[i,j]前面的点集合表示横坐标大于该点的集合，记为C, 如果在集合C中的纵坐标没有大于j的，
则[i,j]是最大点，如何有大于j的，则不是。
可以找到[i,j]前面点的纵坐标的最大值，判断j是否大于该值，即可判断该点是不是最大点
'''
def findMaxPoint(point_arr):
    point_arr.sort(key=lambda item:-item[0])
    n = len(point_arr)
    print(*point_arr[0], sep=" ")
    curr_max = point_arr[0][1]
    for i in range(1, n):
        if point_arr[i][1] > curr_max:
            curr_max = point_arr[i][1]
            print(*point_arr[i], sep=" ")


if __name__ == "__main__":
	point_arr = [[1,2], [5,3], [4,6], [7,5], [9,0], [6,7]]
	findMaxPoint(point_arr)