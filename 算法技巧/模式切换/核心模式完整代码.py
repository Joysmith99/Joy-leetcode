## python本身并不具有链表，树等结构，需要自行实现

# TODO:链表的python实现定义
# 单链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表，原理是先构建一个ListNode实例，通过next链接到下一个ListNode上，以此类推
def create_listnode(arr):
    if arr == None or len(arr) == 0:
        return None
    # 初始化链表
    head = ListNode(arr[0])
    # 定义当前指针
    cur = head
    for i in range(1, len(arr)):
        # 将cur的下一位置指向下一个链表结构
        cur.next = ListNode(arr[i])
        # 将cur指针移动到下一个链表
        cur = cur.next
    return head

# 打印链表，并转化为数组
def print_listnode(head):
    if head is None:
        return []
    # 定义存储数组
    res = []
    # 定义链表指针
    cur = head
    # 当该指针存在不为None时
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

# TODO:二叉树的python实现

# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 题目：将数组转化为二叉树
def create_tree(nums):
    def dfs(index):
        if index >= len(nums) or nums[index] is None:
            return None
        node = TreeNode(nums[index])
        node.left = dfs(2 * index + 1)
        node.right = dfs(2 * index + 2)
        return node

    return dfs(0)

# 打印二叉树
def print_tree(root, res):
    if not root:
        return
    # 前序位置(前序遍历)
    # res.append(root.val)
    print_tree(root.left, res)
    # 中序位置（中序遍历）
    res.append(root.val)
    print_tree(root.right, res)
    # 后序位置（后续遍历）
    res.append(root.val)

    return res

if __name__ == '__main__':
    lst = [1,2,3,4,5,6,7]
    node = create_tree(lst)
    res = []
    res = print_tree(node, res)
    print(res)
    
        