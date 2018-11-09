# coding: utf-8
"""
在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同， 
则称这种编码为格雷码(Gray Code)，请编写一个函数，使用递归的方法生成N位的格雷码。
给定一个整数n，请返回n位的格雷码，顺序为从0开始。
思路：由n-1位gray码生成n为gray
2位gray码是00 01 11 10
3位gray码在头部添0变为000 001 011 010，然后逆序，再在头部添1变为
110 111 101 100
两个相结合就是000 001 011 010 110 111 101 100
"""
def getGray(n):
	if n == 1:
		return ["0", "1"]
	else:
		gray = getGray(n-1)
		new_gray_1 = ["0" + s for s in gray]
		new_gray_2 = ["1" + s for s in gray[::-1]]
		return new_gray_1 + new_gray_2

print(getGray(3))
