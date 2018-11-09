#coding:utf-8
"""
假定一种编码的编码范围是a ~ y的25个字母，从1位到4位的编码，如果我们把该编码按字典序排序，
形成一个数组如下： a, aa, aaa, aaaa, aaab, aaac, … …, b, ba, baa, baaa, baab, baac … …, yyyw, yyyx, yyyy 
其中a的Index为0，aa的Index为1，aaa的Index为2，以此类推。 编写一个函数，输入是任意一个编码，
输出这个编码对应的Index. 
输入描述:
输入一个待编码的字符串,字符串长度小于等于100.

输出描述:
输出这个编码的index

输入例子1:
baca

输出例子1:
16331
思路：计算比第一个字母小的，长度为4的个数，然后计算等于第一个字母，长度为3的个数，递归求除去第一个字母即可
比如baca，先计算a开头长度为4的个数
然后计算b开头，长度为3并小于aca的个数
然后计算以ba开始，长度为2并小于ca的个数
...
"""
def number(c):
    return ord(c) - ord("a") + 1

def getIndex(s, m):
    if len(s) == 0:
        return 0
    index = 0
    n = number(s[0])
    for i in range(0, m):
        index += 25**i
    index = index * (n-1)
    return index + getIndex(s[1:], m-1) + 1

print(getIndex("qqq", 4) - 1)