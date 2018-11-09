"""
给出两个相同长度的由字符 a 和 b 构成的字符串，定义它们的距离为对应位置不同的字符的数量。
如串”aab”与串”aba”的距离为 2；串”ba”与串”aa”的距离为 1；串”baa”和串”baa”的距离为 0。
下面给出两个字符串 S 与 T，其中 S 的长度不小于 T 的长度。我们用|S|代表 S 的长度，|T|代表 T 的长度，
那么在 S 中一共有|S|-|T|+1 个与 T 长度相同的子串，现在你需要计算 T 串与这些|S|-|T|+1 个子串的距离的和。
思路：abbaabbaabba 与 abba，比较长度时
s: abbaabbaabba
t: abba
    abba
     abba
      abba
       abba
        abba
         abba
          abba
           abba
可以看到，在s数组中,从第3个开始，到倒数第3个之间，所有字符都与t中的每个字符做了比较，
而前面i个，是比较s中第i个字符与t的前面i个字符
后面i个，是比较s中的第i个字符与t的后面i个字符
但是必须考虑特殊情况
"""
from collections import Counter
def get_count(char, string):
    d = Counter(string)
    return len(string) - d.get(char, 0)

def get_distance(s, t):
    len_s = len(s)
    len_t = len(t)

    start = len_t - 1
    end = len_s - len_t + 1
    count = 0
    # 如果start比end小
    if start < end:
        # 比较左边
        for i in range(0, start):
            count += get_count(s[i], t[:i+1])
        # 比较右边
        for i in range(end, len_s):
            count += get_count(s[i], t[i-len_s+len_t:])
        # 比较中间
        for i in range(start, end):
            count += get_count(s[i], t)
            
    # 如果end小于等于start
    elif end <= start:
        # 比较左边
        for i in range(0, end):
            count += get_count(s[i], t[:i+1])
        # 比较右边
        for i in range(start, len_s):
            count += get_count(s[i], t[i-len_s+len_t:])
        # 比较中间
        for i in range(end, start):
            count += get_count(s[i], t[i-len_s+len_t:i+1])
    return count

if __name__ == "__main__":
    s = "aabaaabaaaba"
    t = "abaaaaa"
    print(get_distance(s, t))