# 使用暴力枚举
class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


# 使用哈希法
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


if __name__ == '__main__':
    solution = Solution1()
    # solution = Solution2()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))
