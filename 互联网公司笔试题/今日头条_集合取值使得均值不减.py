# coding:utf-8
"""
送集合b中取元素到集合a中，如果该操作使得两个集合的均值都不减少，称为magic操作，请问
最多可以magic操作多少次?
注意：如果添加相同的元素到a中，a中的均值不变
思路：添加均值不减，有两个情况：
1. b中元素在a中，且b中元素小于等于b的均值
2. b中元素不在a中，b中元素小于等于b的均值，大于等于a的均值
添加的元素尽可能的小，这样a，b中的均值增加才会慢，所以先将b排序
"""
a = [1,2,5]
b = [3,4,2,5,6]

s_a = sum(a)
s_b = sum(b)
len_a = len(a)
len_b = len(b)
_b = sorted(b)

magic_ops = 0
for i in range(len(_b)-1):
	avg_a = s_a / len_a
	avg_b = s_b / len_b
	if _b[i] in a and _b[i] <= avg_b:
		s_b -= _b[i]
		len_b -= 1
		magic_ops += 1
	elif _b[i] >= avg_a and _b[i] <= avg_b:
		s_a += _b[i]
		len_a += 1
		s_b -= _b[i]
		len_b -= 1
		magic_ops += 1

print(magic_ops)