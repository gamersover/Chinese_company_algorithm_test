#coding:utf-8
"""
经典题：K个不同字符的最长子串
描述：字符串中包含k个不同字符的最长子串
思路：使用两个指针left, right和一个字典，讲right指向的元素放入字典，
字典的value是该元素出现的最近位置，然后从left开始删除字典中的元素，直到字典中的元素个数不超过k,
如果left指向的元素的最近位置是left, 即left在字典中的值是left，那么就可以在字典中删除left指向的元素，
因为如果left指向的元素的最近位置不是left，表示删除left指向元素后，str[left:right]中的字符个数不会减少
"""
def get_largeset_seq(seq, k):
    left = 0
    result = 0
    d = {}
    for right in range(len(seq)):
        d[seq[right]] = right
        while len(d) > k:
            if d.get(seq[left]) == left:
                d.pop(seq[left])
            left += 1
        result = max(result, right - left + 1)
    return result

print(get_largeset_seq("dabacad", 5))