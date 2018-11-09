#coding=UTF-8
'''
输入一段英文，去掉两端的空格，去掉单词之间多余的空格
思路：先找到第一个不是空格位置i，打印该字符，再从i+1开始判断
如果当前不是空格就打印
如果当前是空格，判断下一个是不是空格，如果下一个不是，就打印当前字符(空格)，否则不打印
'''
def dropSpace(seq):
    for i in range(len(seq)):
        if seq[i] != " ":
            print(seq[i], end="")
            for j in range(i+1, len(seq)):
                if seq[j] == " ":
                    if j != len(seq) - 1:
                        if seq[j+1] != " ":
                            print(seq[j], end="")
                else:
                    print(seq[j], end="")
            return


seq = "   i  have something   to do ? am i   "
dropSpace(seq)

