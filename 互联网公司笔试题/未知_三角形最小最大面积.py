#coding=UTF-8
'''
在平面上有很多点，其中任意三个点都可以构成三角形，求这些点构成三角形的面积的最小值和最大值
输入：多个实例，每个实例第一行为点的个数，后面为点的坐标，一次可以输入多个实例，以0位结尾结束输入
输出：每行对应每个实例的面积的最小值和最大值
例：输入
4
-5 -5
-4 3
4 1
3 -2
3
1 0
2 0
0 2
0
输出：
10.5 33.0
1.0 1.0
思路：1.三个点的面积公式
2.假设有abcdef 5个点，只需计算ab(c,d,e,f), bc(d,e,f), cd(e,f), def 这10个三角形的面积
'''
def get_area(x, y, z):
    return abs((z[0]-x[0])*(y[1]-x[1])-(z[1]-x[1])*(y[0]-x[0])) / 2

def getMinMaxArea(n, points):
    _min, _max = float('inf'), 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                temp = get_area(points[i], points[j], points[k])
                _min = min(_min, temp)
                _max = max(_max, temp)
    return _min, _max

n = 3
points = ((1,0), (2,0), (0,2))
print(*getMinMaxArea(3, points))
                
                