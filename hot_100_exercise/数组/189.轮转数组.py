# 给定一个整数数组 nums，将数组中的元素向右轮转k个位置，其中k是非负数。
# 示例：
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
################################################################

# 思路1：简单的方式就是list末尾出栈，然后再加入列首
# 缺点是时间空间复杂度高
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            tmp = nums.pop()
            nums.insert(0, tmp)

        return nums

# 思路2：采用数学的取模方式来进行idx的定位,(i+k) % n
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_nums = [0] * n
        for i in range(n):
            new_nums[(i+k) % n] = nums[i]

        return new_nums
    
if __name__ == '__main__':
    solution = Solution2()
    res = solution.rotate([1,2,3,4,5,6,7], 3)
    print(res)
