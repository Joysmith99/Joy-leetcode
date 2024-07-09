from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 定义虚拟头节点,并创建新的链表dummy
        dummy = ListNode(-1)

        p = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val > p2.val:
                p.next = p2
                p2 = p2.next
            else:
                p.next = p1
                p1 = p1.next
            p = p.next
            print(p.val, p.next)
            print(dummy.val, dummy.next)

        if p1:
            p.next = p1
        else:
            p.next = p2
        # dummy永远指向的头节点
        return dummy.next

# 测试代码
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")

# 创建两个有序链表
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# 调用合并函数
merged_list = Solution().mergeTwoLists(list1, list2)

# 打印合并后的链表
print_list(merged_list)
