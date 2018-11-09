#coding=UTF-8
'''
多啦A梦有n个豆沙包，每个豆沙包都有自己的美味度，每过一天，豆沙包的美味度就会下降，
一个豆沙包每天美味度下降的数值是一样的，当美味度下降到小于等于0的时候，这个豆沙包就不能吃了，
大雄每天都会偷吃两个当前美味度最高的豆沙包（如果美味度一样的情况下，他
会优先选择每天下降数值较大的那个吃）。当多啦A梦发现当前能吃的豆沙包的数量小于m个情况下，他就会发怒。
求所有豆沙包，在多啦A梦发怒的时候的状态。
每天事情的发生顺序如下：大雄偷吃豆沙包，豆沙包美味度下降指定数值，多啦A梦检查当前剩余的豆沙包。
输入：第一行两个正整数n和m，接下来的n行，每行两个正整数，分别表示每个豆沙包的初始美味度和每天美味度的下降速度。
并且没有两个初始美味度和美味度下降速度都一样的豆沙包。
输出：输出n行，每一行一个整数，表示多啦A梦发怒时每个豆沙包的状态，-1表示被大雄吃了，0表示豆沙包已经不能吃了，正整数表示
豆沙包当前的美味度。
例：输入：
5 1
20 1
25 5
20 6
10 11
9 11
输出：
-1
-1
-1
0
0
'''
def decline(state):
    for i in state.items():
        if i[1][0] != -1:
            i[1][0] = max(i[1][0] - i[1][1], 0)

def eat(state):
    sort_food = sorted(state.items(), key = lambda i:i[1], reverse=True)
    for i in range(2):
        if sort_food[i][1][0] > 0:
            state[sort_food[i][0]][0] = -1

def check(state, m):
    s = 0
    for i in state.items():
        if i[1][0] > 0:
            s += 1
    if s < m:
        return False
    else:
        return True

def print_state(state):
    state = sorted(state.items(), key=lambda i:i[0])
    for i in state:
        print(i[1][0])


if __name__ == "__main__":
    n, m = 5, 1
    state = {0:[20, 1], 1:[25, 5], 2:[20, 6], 3:[10, 11], 4:[9, 11]}

    while check(state, m):
        eat(state)
        decline(state)

    print_state(state)