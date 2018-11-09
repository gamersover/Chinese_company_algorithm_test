#coding=UTF-8
'''
在一个长度不限的字符串中，穷举所有将指定字符替换为另一个指定字符的字符串数组；输出以“，”分隔；
输出次序遵从二进制值的升序，
例如将997中的字符9替换为8，则输出为997,987,897,887
输入：字符串  待替换字符  替换字符
输出：穷举替换的字符串数组
输入：997 9 8
输出997,987,897,887
'''
'''
算法复杂度过高，怎么修改
'''
#---第一种方法复杂高---
# inp = input().split()
# raw_str = inp[0]
# reped_char = inp[1]
# rep_char = inp[2]
# 
# len_str = len(raw_str)
# 
# index = list(filter(lambda i: raw_str[i]==reped_char, range(len_str)))
# 
# 
# for a in range(2**len(index)):
#     new_str = raw_str
#     bin_li = list(bin(a).replace('0b',''))
#     bin_li = ['0']*(len(index)-len(bin_li)) + bin_li
#     for i in list(filter(lambda i: bin_li[i]=='1', range(len(index)))):
#         new_str = new_str[:index[i]] + rep_char + new_str[index[i]+1:]
#     if a < 2**len(index) -1:
#         print(new_str, end=',')
#     else:
#         print(new_str)

#---递归复杂度没测试---
"""
递归思路：f(997) = [9 + f(97), 8 + f(97)]
f(97) = [9 + f(7), 8 + f(7)]
f(7) = 7
"""
def f(s, raw, repla):
    if len(s) < 1:
        return [""]

    if s[0] == raw:
        return [s[0] + i for i in f(s[1:], raw, repla)] + \
            [repla + i for i in f(s[1:], raw, repla)]
    else:
        return [s[0] + i for i in f(s[1:], raw, repla)]

if __name__ == "__main__":
    s = "997"
    raw = "9"
    repla = "8"
    print(*f(s, raw, repla), sep=",")
        
        
