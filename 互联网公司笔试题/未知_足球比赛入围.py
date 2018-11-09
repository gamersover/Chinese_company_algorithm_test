#coding=UTF-8
'''
大学生足协决定举办全国性的大学生足球赛，由每个学校派遣一支队伍代表该校参赛，比赛分区分为几个赛区进行，最终的总决赛中，
将有不超过n支队伍参加。经过激烈的角逐，有机会参与总决赛的队伍以及决出。
协会对比赛的规则进行了调整，以便使得比赛更具有观赏性。
1.总决赛的参赛队伍为n支，n为偶数；
2.进入前1/2的队伍才有资格进入淘汰赛；
3.队伍按积分排名，具体规则为：胜一场加3分，平一场加1分，输一场加0分，队伍首先按照积分降序排序，积分相同按净胜球数降序排列，
仍然相同的按进球数降序排列。
4.基于上述规则，尚未出现有排名异议的情况发生。
输入：测试数据有多组，每组测试数据的第一行为一个整数n(1<=n<=50),为参与总决赛的球队数，随后的n行为球队的名字，由不超过
30个大小写的拉丁字母构成。随后的n*(n-1)/2行为赛事的开展情况，每行的格式为name1-name2 num1:num2,表示两支队伍
的比分情况，确保不会有两支队伍重名，也不会出现队伍自己与自己比赛的情况，且每场比赛只出现一次。
输出：对每组测试数据，输出n/2行，为按字母序排列的进入淘汰赛的n/2支队伍的名单，每个名字在单独的行输出。
例：输入：
4
A
B
C
D
A-B 1:1
A-C 2:2
A-D 1:0
B-C 1:0
B-D 0:3
C-D 0:3
2
a
A
a-A 2:1
输出：
A
D
a
'''
'''
!!!!!!!!多样例输入没搞定!!!!!!!
'''
import sys

def get_finalist(n, teams_name, compet_results):
    dic = dict()
    for name in teams_name:
        dic[name] = [0, 0, 0]
    
    for item in compet_results:
        cr = item.split()
        cr = cr[0].split("-") + [int(i) for i in cr[1].split(":")]
        if cr[2] < cr[3]:
            dic[cr[1]][0] += 3
            dic[cr[1]][1] += 1
        elif cr[2] == cr[3]:
            dic[cr[0]][0] += 1
            dic[cr[1]][0] += 1
        else:
            dic[cr[0]][0] += 3
            dic[cr[0]][1] += 1
        dic[cr[1]][2] += cr[3]
        dic[cr[0]][2] += cr[2]
    
    sort_dic = sorted(dic.items(), key=lambda i:i[1], reverse=True)
    finalist = [sort_dic[i][0] for i in range(n//2)]
    finalist.sort()
    return finalist

while True:
    try:
        res = []
        n = int(input())
        teams_name = [input() for i in range(n)]
        compet_results = [input() for i in range(n*(n-1)//2)]
        res += get_finalist(n, teams_name, compet_results)
        print(*res, sep="\n")
    except:
        break
    

        