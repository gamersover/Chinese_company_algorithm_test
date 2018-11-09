# -*- coding:utf-8 -*-
"""
任意二叉树中，求任意两个节点的最近公共祖先
思路：1.深度优先遍历，找到两个节点的路径（从根节点到该节点）
2.两条路径分别为7->4->2->1， 5->2->1
存储在堆栈中,1是根节点，将两个堆栈截取到相同长度后，在逐一比较节点是否相同，步骤与
两个链表的第一个公共节点相似。
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.isvisited = False


def dfs(root, node1, node2):
    li = [root]
    flag = [0, 0]
    while True:
        if root is node1:
            root.isvisited = True
            li1 = li.copy()
            flag[0] = 1
        if root is node2:
            root.isvisited = True
            li2 = li.copy()
            flag[1] = 1
        if all(flag):
            return li1, li2
        if root.left is not None and not root.left.isvisited:
            root.left.isvisited = True
            li.append(root.left)
            root = root.left
        elif root.right is not None and not root.right.isvisited:
            root.right.isvisited = True
            li.append(root.right)
            root = root.right 
        else:
            li.pop()
            if len(li) == 0:
                raise Exception 
            root = li[-1]

def get_closest_parent(li1, li2):
    if len(li1) > len(li2):
        long_list = li1
        short_list = li2
    else:
        long_list = li2
        short_list = li1
    
    long_list = long_list[:len(short_list)-1]
    short_list = short_list[:-1]
    for i in range(len(short_list)-1, -1, -1):
        if long_list[i] is short_list[i]:
            return long_list[i]
     
if __name__ == "__main__":
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node3.left = node5
    li1, li2 = dfs(root, node5, node4)
    parent = get_closest_parent(li1, li2)
    print(parent.data)
    
            
    