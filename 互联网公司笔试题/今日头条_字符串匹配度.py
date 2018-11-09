# coding:utf-8
"""
ElasticSearch计算query匹配度方法：
输入："mbh"切词后分别为"m", "b", "h"(模拟切词后的3个关键字), "amhbgyhdc"(模拟一个ES的一个文档)
关键字"m"出现在第2个位置，"b"出现在第4个位置，"h"出现在第3、7个位置，但是第3个位置与query关键字逆序，
为简化流程，可以排除掉；
如果没有匹配到关键字，打分为0分；
如果匹配到所有关键字，打分为100分，但要区分出相似程度，
m-b隔了1个词，100-1=99；
b-h隔了2个词，99-2=97；
最后这个例子的匹配程度为97分；
实现一个简单的算法，计算匹配度问题(有多个匹配时，需要找出得分最高的匹配)，匹配度可能是负分
思路：找到关键字在文档中出现的每一个位置
比如关键字为"mbh"，文档为"amhbgyhdc"
关键字出现在每个位置数组为[[1], [3], [2, 6]]
                   m    b      h
如果该数组中，有一个为空，相似度为0
去掉后一个数组中小于等于前一个数组最小值的数，数组变为[[1], [3], [6]]
因为2小于[2,6]的前一个数组[3]的最小值3
再判断数组中，是否有一个空，有相似度为0
去掉前一个数组中大于等于后一个数组最大值的数，数组变为[[1], [3], [6]]
再判断数组中，是否有一个空，有相似度为0
经过上面两个步骤之后，这个数组中的任意取每个子数组中的数，都可以构成匹配原关键字的字符串
而这时匹配到的距离只取决于开始和最后两个数的距离，中间那些数不会影响最终结果
所以找到第一个匹配到的最大值，与最后一个匹配到的最小值即可
"""
keywords = "eb"
document = "aeabecaaa"


def find(k ,d):
	dp = [[] for i in range(len(k))]
	for j in range(len(d)):
		idx = keywords.find(d[j])
		if idx != -1:
			dp[idx].append(j)

	if len(dp[0]) == 0:
		return 0
	for i in range(1, len(dp)):
		if len(dp[i-1]) == 0:
			return 0
		dp[i] = [j for j in dp[i] if j > min(dp[i-1])]		

	if len(dp[-1]) == 0:
		return 0
	for i in range(len(dp)-2, -1, -1):
		if len(dp[i+1]) == 0:
			return 0
		dp[i] = [j for j in dp[i] if j < max(dp[i+1])]
	
	if len(dp[0]) == 0:
		return 0
	start = max(dp[0])
	m = max(dp[-2])
	for item in dp[-1]:
		if item > m:
			m = item
			break
	s = m - start - len(dp) + 1
	return 100-s


print(find(keywords, document))

