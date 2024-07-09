from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 增删改查
class Solution:
    def addnode(head:Optional[ListNode], node:Optional[ListNode], x:int) -> Optional[ListNode]:

        # 遍历head方法
        p1 = head
        while p1 != None:  # while p1也行
            p1 = p1.next
        # 本地删除
        dummy = ListNode(-1)
        dummy.next = head
