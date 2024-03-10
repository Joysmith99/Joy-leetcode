# 使用暴力枚举。
# 时间复杂度为O(n^2),空间复杂度为O(1)
class Solution1():
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


# 使用查找表（有序：平衡二叉树；无序：查找表）：哈希表
# 时间复杂度O(n),空间复杂度O(n)：多了一个哈希表的开销
class Solution2():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = {}
        for i, value in enumerate(nums):
            if target-value in hashtable:
                return [hashtable[target-value], i]
            else:
                hashtable[value] = i
        return []


if __name__ == '__main__':
    # solution = Solution1()
    solution = Solution2()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))
