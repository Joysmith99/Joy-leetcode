# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
###############################################################################

## 【错误思路】使用滑动窗口做有关“求和”的字串题目
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 定义双指针
        pl, pr = 0, 1
        # 定义结果数
        res = 0

        n = len(nums)
        # 使用滑动窗口
        # 边界条件
        while pl < pr and pr <= n:
            print(nums[pl:pr])
            # 定义扩张条件
            if sum(nums[pl:pr]) < k:
                pr += 1
            # 定义收缩条件
            elif sum(nums[pl:pr]) > k:
                pl += 1
            # 此时满足条件时
            else:
                res += 1
                pr += 1
                pl += 1
        return res
    
# 这样做一定通不过测试用例的原因是：数组中的数字可以有正有负，扩张条件和收缩条件无法定义
# 事实上，上述做法适用于list全为正，k也为正的情况
# 记住：滑动窗口主要是用来解决字串的（带约束）的匹配问题，使用字串和作为滑动窗口的约束一定是错误的！！！
# 因此，需要使用其他方式

# TODO: 
# 正确思路为“前缀和”+“哈希表”