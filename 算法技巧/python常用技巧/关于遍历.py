
from typing import List, ListNode
# 迭代遍历数组
def traverse(arr: List[int]):
    for i in range(len(arr)):
        pass

# 递归遍历数组
def traverse(arr: List[int], i: int):
    if i == len(arr):
        return
    # 前序位置
    traverse(arr, i + 1)
    # 后序位置

# 迭代遍历单链表
def traverse(head: ListNode):
    p = head
    while p != None:
        p = p.next

# 递归遍历单链表
def traverse(head: ListNode):
    if head == None:
        return
    # 前序位置
    traverse(head.next)
    # 后序位置