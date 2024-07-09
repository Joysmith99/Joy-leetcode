# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
# 滑动窗口每次只向右移动一位,返回滑动窗口中的最大值。
######################################################################################################

# TODO: 思路1:直接的做法是使用双指针作为滑动窗口的区间，再使用切片函数来找到最大值
# 然而，会出现超时问题。时间复杂度O(n),空间复杂度O(n)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pl, pr = 0, k
        n = len(nums)
        res = []

        while pr <= n:
            max_value = max(nums[pl:pr])
            res.append(max_value)

            pl += 1
            pr += 1
        
        return res

# 还有什么方法？对于一个“固定窗口”的滑动结构，能够想到的则是“先进先出”的队列结构