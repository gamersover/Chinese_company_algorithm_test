# coding:utf-8
"""：
象棋大小为8*8， 以左下角为起点，向上为y轴，向右为x轴，求马走k次可以达到坐标（x，y）的次数,
数可能很大，将最终结果模上1000000007
输入：
k
x y
k为马总共走了多少步
x,y为目的坐标
输出：
最终到达(x,y)的总次数

思路：动态规划问题，第k次，可能到达的坐标，以及到达该坐标的次数，使用字典{(x, y):times}
比如k=0,dict = {(0,0):1}
k=1, 可能走到的坐标有(1,2),和(2,1),dict={(1,2):1,(2,1):1}
。。。
设第k-1次，dict={(x0,y0):t1, (x1,y1):t2,....}
那么第k次，从x0,y0可以到的位置，加上t1次，x1,y1可以到的位置加上t2次
"""
direction = ((1,2), (2,1), (1,-2), (2,-1), (-1,-2), (-2,-1), (-1,2), (-2,1))

def get_next_poses(dict):
    new_dict = {}
    for pos in dict.keys():
        for d in direction:
            pos_x = pos[0] + d[0]
            pos_y = pos[1] + d[1]
            if 0 <= pos_x < 8 and 0 <= pos_y < 8:
                new_dict[(pos_x, pos_y)] = (new_dict.get((pos_x, pos_y), 0) \
                                            + dict.get(pos))%1000000007
    return new_dict
  
def main(x_dest, y_dest, k):
    dict = {(0, 0):1}
    for i in range(k):
        dict = get_next_poses(dict)
    return dict.get((x_dest, y_dest), 0)

print(main(3,3,30))