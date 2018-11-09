#coding=UTF-8
'''
有一条街道，沿西——东方向有n栋房子，每栋房子都有一个希望的方向，请问如何划分，可以使得东西方向划分错的房子最少，
求出最少值
W必须在E前面，可以全是E，或W
输入：n个字母，含W,E，其中W表示西，E表示东
输出：最小值
输入：EEEWW
输出：2
解析：将所有房子都划分为E

思路：用0表示E,1表示W,则原始为00011
则可能情况为11111， 11110， 11100，11000,10000,00000
将可能情况与原始情况对比 ，得到错误最小的
'''


hope_seq = input()
seq_len = len(hope_seq)
hope_seq = list(map(lambda e:int(e=='W'), hope_seq))
possible_seq = [1]*seq_len
min_fault = sum(map(lambda i,j:int(i^j), hope_seq, possible_seq))
for i in range(seq_len-1, -1, -1):
    possible_seq[i] = 0
    s = sum(map(lambda i,j:int(i^j), hope_seq, possible_seq))
    if s < min_fault:
        min_fault = s
    
print(min_fault)
    

    