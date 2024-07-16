# 给你一个整数数组 nums ，判断是否存在三元组 
# [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
# 请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
#########################################################################################################

# nsum问题的核心在于：排序+双指针（左右指针）
# TODO：思路：三个数字，需要三个变量，如果采用暴力枚举，将会是O(n^3)的时间复杂度
# 首先将数组由小到大排序后，选择一个变量下标i进行遍历。将变量以右的区间定义为左右指针的出发点，即left=i+1, right = len(nums)-1
# 在子区间中进行逻辑设置【三个】：
# 1.如果nums[i]>0，一定没有满足的，直接跳出，返回res=[]
# 2.如果当前元素与之前元素相同，需要进行跳过
# 3.在12满足后，进行sum和大于，等于，小于的相关逻辑设计，注意left和right也需要跳过重复值

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 数组排序
        nums.sort()
        # 定义结果：
        res = []

        for i in range(len(nums)-2):
            # 1.判断nums[i]的情况
            if nums[i] > 0: break
            # 2.判断nums[i]是否为重复元素
            if i > 0 and nums[i] == nums[i-1]: continue
            # 3.进一步逻辑设置
            # 定义变量：【局部】左右指针
            left, right = i+1, len(nums)-1
            # 左右指针的移动的逻辑：
            while left < right:
                # 先求和
                sum = nums[i] + nums[left] + nums[right]
                # 按照当前sum的大小，判定具体逻辑
                # 移动左指针
                if sum < 0:
                    left += 1
                    # 判定重复元素
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                # 同理，移动右指针，是对称的操作
                elif sum > 0:
                    right -= 1
                    # 判定重复元素
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                else:
                    res.append(nums[i], nums[left], nums[right])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        
        return res


