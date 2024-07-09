# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
# 滑动窗口每次只向右移动一位,返回滑动窗口中的最大值。
######################################################################################################

# TODO: 思路1:直接的做法是使用双指针作为滑动窗口的区间，再使用切片函数来找到最大值
# 然而，会出现超时问题。时间复杂度达到了O(nk),因为每一次遍历是O(n)，而在窗口中找到最大值为O(k)，因此复杂度为O(nk)
class Solution1(object):
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

# TODO: 还有什么方法？
# 对于一个“固定窗口”的滑动结构，能够想到的则是“先进先出”的队列结构
# 而滑动窗口的遍历时间不可避免，那么如何尽可能的缩减每个窗口内找到最大值的时间，使得O(k) -> O(1)
# 思路2：采用单调队列。我们使用python中的collections.deque()创建双端队列来实现
import collections

class Solution2(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        res = []

        for i in range(len(nums)):
            # 如果队列不为空，且队列头部的元素已经不在滑动窗口内，移除头部元素
            if deque and deque[0] < i - k + 1:
                deque.popleft()

            # 如果队列不为空，且队列尾部的元素小于新加入的元素，移除尾部元素
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()

            deque.append(i)

             # 当滑动窗口形成时，将队列头部元素（当前滑动窗口的最大值）加入结果列表
            if i >= k - 1:
                res.append(nums[deque[0]])

        return res
