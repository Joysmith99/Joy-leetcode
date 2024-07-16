# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
############################################################################################

# 遇到求最值的问题，一般考虑动态规划dp
# TODO:对比子串中560.和为K的子数组题目，那道题考的是前缀和，因为有一个明确的优化目标K，再加上前缀和的性质是频繁计算一个索引区间的元素之和，因此能够使用
# 动态规划三要素：重叠子问题、最优子结构、状态转移方程。
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # 设nums[i]结尾的最大子数组和为dp[i]
        dp = [0] * n

        # base case
        dp[0] = nums[0]
        # 状态转移方程
        for i in range(1, n):
            # nums[i]每次只有两种选择，一种是跟之前的相加，第二种是自成一个子数组
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        
        res = float('-inf')
        for i in range(n):
            res = max(res, dp[i])
        return res