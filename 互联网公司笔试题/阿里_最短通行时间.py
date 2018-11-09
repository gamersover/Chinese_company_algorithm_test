#coding=UTF-8
'''
某一城市有N个路口，每个路口都有通行的时间限制，比如当时间为3时，表示0-2可以通过，3-5不可以通过，6-8可以通过
两个路口存在道路，道路之间有通行时间。要求从i路口到j路口的最短通行时间
输入描述：第1行为路口个数n，接着n行有两个数字，第一个数字为路口的编号，第二个数字为路口的通行限制时间，
第n+2行为总的道路数m，接着的m行有三列，前面两列表示2个路口之间有道路，第三列表示该道路的通行时间。
最后一行有两列，第一列表示出发点，第二列表示目的地
例：输入
4
0,3
1,5
2,6
3,8
4
0,1,5
1,2,7
2,3,10
0,2,3
0,3
输出：
13
思路：迪杰斯拉算法
'''

# _N = int(input())
# 
# _intersections = []
# for i in range(0,_N):
#     x,y = input().split(',')
#     _intersection= [int(x),int(y)]
#     _intersections.append(_intersection)
# 
# _M = int(input())
# _roads= []
# for j in range(0,_M):
#     u,v,w = input().split(',')
#     _road= [int(u),int(v),int(w)]
#     _roads.append(_road)
# 
# _s,_t = input().split(',')
# _s,_t = int(_s),int(_t)

N = 4 # 路口数
intersections = [[0,3], [1,5], [2,6], [3,8]] # 路口和开放时间
M = 4 # 道路数
roads = [[0,1,5], [1,2,7], [2,3,10], [0,2,3]] # 路口与路口之间的道路以及通过时间
s, t = 0, 3 # 源路口，目的路口


curr_time = 0
dic = {i:float("inf") for i in range(N)}
dic[s] = 0
visited = []
while len(visited) < N-1:
    visited.append(s)
    for road in roads:
        # 存在通路
        if s == road[0] or s == road[1]:
            arrive_time = curr_time
            # 不允许通行
            if (curr_time//intersections[s][1]) % 2 != 0:
                arrive_time = ((curr_time//intersections[s][1])+1) *intersections[s][1]
            
            arrive_time += road[2]
            
            if s == road[0]:
                dic[road[1]] = min(arrive_time, dic.get(road[1]))
            elif s == road[1]:
                dic[road[0]] = min(arrive_time, dic.get(road[0]))

    unvisited = {}
    for k, v in dic.items():
        if k not in visited:
            unvisited[k] = v

    s, curr_time = sorted(unvisited.items(), key=lambda i:i[1])[0]

print(dic[t])



