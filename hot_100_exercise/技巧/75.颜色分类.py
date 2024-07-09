## 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
## 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
## 必须在不使用库内置的 sort 函数的情况下解决这个问题。
##########################################################################################################################
# 如果使用.sort()，那么就是一行代码。注意.sort()直接原地修改nums。而使用sorted(nums)会返回list, nums不会变化
# nums.sort()
## TODO: 如何不使用.sort()方法呢？

## 题目叫做“荷兰国旗问题”（数字分割为三段）
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        # 定义双指针l和r作为边界，idx为移动指针
        l, r, idx = 0, n-1, 0

        # 停止条件为idx到达2的左边界r时
        while idx <= r:
            # 如果idx当前值为0，与l交换，idx和l的值自增
            if nums[idx] == 0:
                nums[idx], nums[l] = nums[l], nums[idx]
                idx += 1
                l += 1
            # 如果idx当前值为1，只有idx自增
            elif nums[idx] == 1:
                idx += 1
            # 如果idx当前值为2，与r交换，r自减，但是idx不变（因为有可能现在idx为1，循环后需要跟l交换）
            else:
                nums[idx], nums[r] = nums[r], nums[idx]
                r -= 1
        
        return nums


# TODO: 思考
# 1.这道题是进阶版的4.移动零
# 2.如果对nums做本地修改，可以不强制使用return函数
# 3.什么时候使用idx角标，什么时候又使用num元素？【当需要进行数组本地替换时，使用idx角标，方便交换数组位置；当只需要遍历操作，不做修改时，使用nums】
# 4.为什么r自减后，idx不移动？【因为r和idx在一边】如果idx为n-1的话，l自增时，idx是否移动？【不移动】
