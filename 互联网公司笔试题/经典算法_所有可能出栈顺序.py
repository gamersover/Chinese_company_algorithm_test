#coding:utf-8
"""
经典题：所有可能的出栈顺序
思路：a表示原序列，s表示入栈，s_表示出栈顺序
某一个时刻可能执行两种情况：
1.a内元素压栈到s 模拟压栈
2.s内元素压栈到s_ 模拟出栈
"""
def get_all_seq(a, s, s_):
    # 全部出栈
    if len(a)==0 and len(s)==0:
        print(s_)
    # 第一种情况
    if len(a) != 0:
        s.append(a.pop())
        get_all_seq(a, s, s_)
        a.append(s.pop()) # 回溯，还原状态
    # 第二种情况
    if len(s) != 0:
        s_.append(s.pop())
        get_all_seq(a, s, s_)
        s.append(s_.pop()) # 回溯还原状态

a = [1,2,3,4]
s, s_ = [], []
get_all_seq(list(reversed(a)), s, s_)