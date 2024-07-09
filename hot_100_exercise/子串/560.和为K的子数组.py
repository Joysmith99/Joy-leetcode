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
# 前缀和可以定义为sums。举个例子，给定nums = [1,2,3,4,5]其前缀和数组sums=[1,1+2,1+2+3,1+2+3+4,1+2+3+4+5] = [1,3,6,10,15]
class Solution2(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 当数组前缀为[]时，sums为0，此时需要计数一个
        dic={0:1}
        # 定义前缀和，结果
        sums,res=0,0

        for num in nums:
            # 计算每一步的前缀和
            sums+=num
            # 计算之前sum-k出现的次数，作为结果进行累加
            res+=dic.get(sums-k,0)
            # 对当前前缀和计数一个
            dic[sums]=dic.get(sums,0)+1
        return res

# 思考：
# 1.前缀和的性质：sums[j] - sums[i]即为区间（i，j]中的子数列的和
# 2.什么时候使用前缀和：子串（子数列）的求和问题
# 3.为什么前缀和常常与哈希表（字典）一起使用？因为需要记录先前的前缀的个数，就避免了BF，从而减少了时间复杂度
# 4.该问题是否可以看做是另一种形式的 TODO:两数之和【是的】