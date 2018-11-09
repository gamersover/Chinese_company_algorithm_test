#coding:utf-8
"""
经典算法：数独问题
思路：递归
"""
def get_all_number(a, i, j):
    s = set()
    for col in range(9):
        s.add(a[i][col])
    for row in range(9):
        s.add(a[row][j])
    for row in range(3):
        for col in range(3):
            s.add(a[i//3*3+row][j//3*3+col])
    return s

def search_empty_pos(a, l):
    for i in range(9):
        for j in range(9):
            if a[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False
            
def soduku(a):
    l = [0, 0]
    if not search_empty_pos(a, l):
        return True
    for num in range(1,10):
        if num not in get_all_number(a, l[0], l[1]):
            a[l[0]][l[1]] = num
            if soduku(a):
                return True
            a[l[0]][l[1]] = 0
    return False


if __name__ == "__main__":
    a = [[3, 0, 0, 0, 1, 0, 0, 9, 0],
         [0, 0, 0, 0, 0, 3, 5, 0, 0],
         [0, 7, 0, 0, 0, 9, 0, 0, 6],
         [0, 0, 0, 0, 0, 0, 0, 4, 0],
         [1, 0, 0, 3, 7, 2, 0, 0, 8],
         [0, 9, 0, 0, 0, 0, 0, 0, 0],
         [8, 0, 0, 7, 0, 0, 0, 6, 0],
         [0, 0, 6, 2, 0, 0, 0, 0, 0],
         [0, 2, 0, 0, 4, 0, 0, 0, 7]]
    soduku(a)
    print(*a, sep="\n")
         
    
    
    