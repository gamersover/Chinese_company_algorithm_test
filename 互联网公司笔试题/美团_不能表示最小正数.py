# coding:utf-8
"""
给出1 1 0 2几个数字，能够表示的数0，1，2，10，11，12，20，110，112，。。。，
不能表示的最小正数是3
现在给出一个数字的字符串，请问由给出的数字中不能组成的最小正数是多少？
"""
def get_min_number(s):
    num_str = '123456789'
    for i in num_str:
        if i not in s:
            return i
    if '0' not in s:
        return '10'
    else:
        dic = {}
        for i in num_str:
            dic[i] = s.count(i)
        t = sorted(dic.items(), key=lambda kv: (kv[1], int(kv[0])))[0]
        m = t[1]
        count_0 = s.count('0')
        if m - 1 >= count_0:
            res = t[0] + '0'*(count_0+1)
        else:
            res = t[0] * (m+1)
        return res
                  
if __name__ == "__main__":
    s = input()
    print(get_min_number(s))