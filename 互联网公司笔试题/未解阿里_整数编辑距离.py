# -*- coding: utf-8 -*-
"""
 给定两个长度为 n ( 0 < n <= 8 ) 的数字串 (由 1 到 9 构成)，我们希望对第一个数字串做一系列如下操作：
    1. 将数字串的某一位加 1
    2. 将数字串的某一位减 1
    3. 交换数字串中任意两个数字的位置
    最终使得第一个数字串变成第二个数字串，请问最少需要多少次操作.
"""

import sys

first_str = sys.stdin.readline()
second_str = sys.stdin.readline()

sys.stdout.write(first_str)
sys.stdout.write(second_str)
    
    
            