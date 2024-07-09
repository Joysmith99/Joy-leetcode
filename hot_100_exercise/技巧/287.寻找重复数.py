# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#####################################################################################################

# 注意这里是寻找重复元素，与136.只出现一次的数字 有很大区别
# 常见的作法自然还是使用字典存储，遍历对应的value，找出大于1的，但是不满足不常量空间为O(1)【此时为O(n)】

# TODO: 思路1：如何原地修改？很简单，先排序，之后比较相邻的值即可（这个面试的时候至少能写出来）
class Solution1(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 对数组进行原地排序
        nums.sort()
        # 遍历数组
        n = len(nums) - 1
        for i in range(n):
            # 这里不用担心数组越界
            if nums[i] == nums[i+1]:
                return nums[i]
            else:
                i += 1

# 时间复杂度：O(nlogn)+O(n)，注意nums.sort()使用的是Timsort，时间复杂度为O(nlogn)，原题修改因此空间复杂度O(1)
# 空间复杂度O(1)

# TODO:思路2：把数组当做一个环形链表看待，从而可以使用快慢指针
class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义子函数
        def next(i):
            return nums[i]
        slow = fast = 0
        # 第一次相遇
        while True:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                break
        slow = 0
        # 第二次相遇
        while slow != fast:
            slow = next(slow)
            fast = next(fast)
        return slow

# TODO:思路3（较为抽象）
# 思路1并没有使用题目的性质：数组取值范围[1, n]在index范围[0, n]内。因此当我们发现数字index = nums[k]时说明这个就是重复的