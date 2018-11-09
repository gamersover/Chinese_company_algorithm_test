# coding:utf-8
"""
画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
小Q有他独特的绘画技巧,每次小Q会选择一条斜线, 如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。 
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数N和M(1 <= N, M <= 50), 表示画板的长宽。
接下来的N行包含N个长度为M的字符串, 其中包含字符'B','Y','G','X',分别表示蓝色,黄色,绿色,空白。整个表示小Q要完成的作品。


输出描述:
输出一个正整数, 表示小Q最少需要多少次操作完成绘画。

输入例子1:
4 4
YXXB
XYGX
XBYY
BXXY

输出例子1:
3

例子说明1:
XXXX
XXXX
XXXX
XXXX
->
YXXX
XYXX
XXYX
XXXY
->
YXXB
XYBX
XBYX
BXXY
->
YXXB
XYGX
XBYY
BXXY
思路：遇到Y，沿着-1方向，将Y变为X,将G变为B
遇到B，沿着1方向，将B变为X，将G变为Y
遇到G，沿着-1方向，做Y的操作，沿着1方向作B的操作
"""
def find_y(arr, i, j, row, col):
    curr_i = i - 1
    curr_j = j - 1
    while curr_i >= 0 and curr_j >= 0 and \
         (arr[curr_i][curr_j] == 'Y' or arr[curr_i][curr_j] == "G"):
        if arr[curr_i][curr_j] == "Y":
            arr[curr_i][curr_j] = "X"
        else:
            arr[curr_i][curr_j] = "B"
        curr_i -= 1
        curr_j -= 1

    curr_i = i + 1
    curr_j = j + 1

    while curr_i < row and curr_j < col and \
         (arr[curr_i][curr_j] == 'Y' or arr[curr_i][curr_j] == "G"):
        if arr[curr_i][curr_j] == "Y":
            arr[curr_i][curr_j] = "X"
        else:
            arr[curr_i][curr_j] = "B"
        curr_i += 1
        curr_j += 1

def find_b(arr, i, j, row, col):
    curr_i = i + 1
    curr_j = j - 1
    while curr_i < row and curr_j >= 0 and \
         (arr[curr_i][curr_j] == 'B' or arr[curr_i][curr_j] == "G"):
        if arr[curr_i][curr_j] == "B":
            arr[curr_i][curr_j] = "X"
        else:
            arr[curr_i][curr_j] = "Y"
        curr_i += 1
        curr_j -= 1

    curr_i = i - 1
    curr_j = j + 1

    while curr_i >= 0 and curr_j < col and \
         (arr[curr_i][curr_j] == 'B' or arr[curr_i][curr_j] == "G"):
        if arr[curr_i][curr_j] == "B":
            arr[curr_i][curr_j] = "X"
        else:
            arr[curr_i][curr_j] = "Y"
        curr_i -= 1
        curr_j += 1

def find_g(arr, i, j, row, col):
    find_y(arr, i, j, row, col)
    find_b(arr, i, j, row, col)

        


if __name__ == "__main__":
#     arr = [["Y", "X", "X", "B"],
#            ["X", "Y", "G", "X"],
#            ["X", "B", "Y", "Y"],
#            ["B", "X", "X", "Y"]]
#     row = 4
#     col = 4
    row, col = [int(i) for i in input().split()]
    arr = [list(input()) for j in range(row)]
    count = 0
    for i in range(row):
        for j in range(col):
            if arr[i][j] == "Y":
                arr[i][j] = "X"
                find_y(arr, i, j, row, col)
                count += 1
            elif arr[i][j] == "B":
                arr[i][j] = "X"
                find_b(arr, i, j, row, col)
                count += 1
            elif arr[i][j] == "G":
                arr[i][j] = "X"
                find_g(arr, i, j, row, col)
                count += 2
                

    print(count)