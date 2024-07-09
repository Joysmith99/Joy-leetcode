# 使用双指针
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 定义快指针和慢指针
        quick, slow =0, 0
        length = len(nums)
        while quick <= length:
            # 如果快慢指针位置不是0，就自己跟自己交换；如果快指针位置不是0，慢指针位置为0，就要交换
            if nums[quick] != 0:
                nums[quick], nums[slow] = nums[slow], nums[quick]
                slow += 1
            # 如果快指针位置为0，快指针往前移
            quick += 1

        return nums