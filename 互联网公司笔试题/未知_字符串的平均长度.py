#coding=UTF-8
'''
给定字符串aabbccccd，其中连续子串有aa,bb,cccc,d，其长度分别为2,2,4,1,平均长度为(2+2+4+1)/4=2.25
要求，输入一个字符串，输出字符串的平均长度，(结果四舍五入保留两位小数)
例:输入 aabbccccd
      输出2.25
'''
from decimal import Decimal
def getStrAvgLen(s):
    i, j = 0, 0
    length, count = 0, 0
    while i < len(s):
        while j < len(s) and s[j] == s[i]:
            j += 1
        length += j - i
        count += 1
        i = j
    avg = Decimal(length / count)
    return round(avg, 2)


print(getStrAvgLen("aabbccccd"))
    
    

        
        
        