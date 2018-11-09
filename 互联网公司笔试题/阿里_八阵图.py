#coding:utf-8
"""
八卦阵相传是由诸葛亮创设的一种战斗队形和兵力部署，由八种阵势组成。为了方便，采用矩阵来描述一个八卦阵，
它由八个单阵组成，每个单阵由多个兵力区域组成形成一种阵势，如下图所示，其中数字为一个兵力区域的士兵个数。
假设单阵与单阵之间兵力区域不会相邻，且单阵中每个兵力区域至少存在一个相邻兵力区域（
注：相邻是指在其左上，正上，右上，右方，右下，正下，左下，左方与其相邻），
请用最快的速度计算出八个单阵中的兵力（士兵个数）的最大值和最小值。
输入:
输入描述，例如：
第一行输入是八阵图的行数。
第二行输入是八阵图的列数。
后续行输入每个区域兵力。每一行的数据中间使用空格分开，当前一行输入完成后回车输入下一行数据。
输出:
输出描述，例如：
输出八个单阵中兵力最大值和最小值。
输入范例:
20
20
34  0   0   0   0   0   0   0   0   0   0   0   0   0   0   10  0   0   0   30
0   23  10  5   5   0   0   0   5   5   5   5   5   0   0   0   30  0   40  0
0   9   0   0   5   0   0   0   4   4   4   4   4   0   0   0   0   30  0   0
0   8   7   7   0   5   0   0   3   3   3   3   0   0   0   0   7   0   9   0
0   9   0   0   5   0   5   0   0   12  12  0   0   0   0   10  0   0   0   9
0   0   0   0   5   0   0   5   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   12  12  0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
0   0   0   0   0   0   0   0   0   0   0   0   0   5   0   0   0   0   0   0
40  30  3   6   6   0   0   0   0   0   0   0   0   5   5   0   0   0   10  0
0   0   20  0   0   6   6   0   0   0   0   0   0   0   5   6   5   10  10  0
40  30  3   7   6   0   0   0   0   0   0   0   0   0   0   6   0   0   10  0
0   0   0   0   0   0   0   17  0   0   0   0   17  0   0   6   5   7   7   0
0   0   0   0   0   0   0   0   7   0   0   7   0   0   0   0   0   0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   20  0   0   7   0   0   0   0   4   4   0   0   0   0   0   10  0   0   0
0   30  0   7   0   0   0   0   0   5   5   0   0   0   0   0   0   10  0   50
0   40  7   0   0   0   0   0   0   5   5   0   0   0   0   0   0   0   50  0
43  30  25  10  50  0   0   0   6   6   6   6   0   0   0   0   0   50  0   0
输出范例:
323
116
思路：深度优先遍历
"""
def get_sum(x, y):
    s = 0
    def dfs(x, y):
        nonlocal s
        visited[x][y] = True
        for d in direction:
            new_x, new_y = x+d[0], y+d[1]
            if 0 <= new_x < n_row and 0 <= new_y < n_col and \
                matrix[new_x][new_y] > 0 and visited[new_x][new_y] == False:
                s += matrix[new_x][new_y]
                dfs(new_x, new_y)
    dfs(x, y)
    return s

def getMaxMin(n_row, n_col):
    arr = []
    for _ in range(8):
        for i in range(n_row):
            for j in range(n_col):
                if visited[i][j] == False and matrix[i][j] > 0:
                    s = get_sum(i, j) + matrix[i][j]
                    arr.append(s)
    print(max(arr))
    print(min(arr))

if __name__ == "__main__":
    n_row = int(input())
    n_col = int(input())
    matrix = []
    for i in range(n_row):
        row_list = [int(i) for i in input().split()]
        matrix.append(row_list)
    visited = [[False for j in range(n_row)] for i in range(n_col)]
    direction = [(0,1), (0,-1), (1,0), (1,-1), (-1,0), (-1,-1), (1,1), (-1,1)]
    getMaxMin(n_row, n_col)
        