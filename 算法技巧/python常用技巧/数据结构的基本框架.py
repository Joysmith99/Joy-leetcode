# TODO：链表的实现框架
# 单链表节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# TODO:二叉树

# 基本的二叉树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs 和回溯
def dfs(root: 'Node'):
    if not root: return
    # 做选择
    print("我已经进入节点 %s 啦" % root.value)
    for child in root.children:
        dfs(child)
    # 撤销选择
    print("我将要离开节点 %s 啦" % root.value)

# 回溯算法把「做选择」「撤销选择」的逻辑放在 for 循环里面
def backtrack(root: 'Node'):
    if not root: return
    for child in root.children:
        # 做选择
        print("我站在节点 %s 到节点 %s 的树枝上" % (root.value, child.value))
        backtrack(child)
        # 撤销选择
        print("我将要离开节点 %s 到节点 %s 的树枝上" % (child.value, root.value))


