#coding=UTF-8
'''
在魔法学院，小明为了拿奖学金，需要考试取得一定的成绩。对于即将面临的n门考试平均分至少要到达avg分，
每门课程的满分为r。小明凭自己的实力考试，第i门科目只能考ai分，但小明得到了精灵法师的魔法祝福加成，
可以花费一些祝福值提高某科目的成绩，但最高分不能超过满分，对于第i门科目，小明可以花费bi祝福值提高成绩1分
为了使得平均分达到avg分，问小明最少需要花费多少祝福值？
输入：
第一行输入n r avg  接下来n行每行输入ai，bi
输出：
输出最少花费的祝福值
例：输入
5 5 4
5 2
4 7
3 1
3 2
2 5
输出
4
'''
def minBlessValue(n, r, avg, a, b):
    diff = n * avg - sum(a)
    magic_value = 0
    b_ = [(i, b[i]) for i in range(n)]
    b_ = sorted(b_, key=lambda e:e[1])
    for item in b_:
        if r - a[item[0]] < diff:
            magic_value += item[1] * (r-a[item[0]])
            diff -= (r-a[item[0]])
        else:
            magic_value += item[1] * diff
            break
    return magic_value


n = 5
r = 5
avg = 4
a = [5, 4, 3, 3, 2]
b = [2, 7, 1, 2, 5]
print(minBlessValue(n, r, avg, a, b))

        
         
    
  
    
    