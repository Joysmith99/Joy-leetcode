# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
#####################################################################################################################

# TODO: 思路1：使用暴力枚举BF。
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


# TODO: 思路2：
# 使用查找表（有序：平衡二叉树；无序：查找表）：哈希表

class Solution2():
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用一个字典结构作为哈希表
        hashtable = {}
        for i, value in enumerate(nums):
            if target-value in hashtable:
                return [hashtable[target-value], i]
            else:
                hashtable[value] = i
        return []

# 【思考】
# 思路1：时间复杂度为O(n2),空间复杂度为O(1)
# 思路2：时间复杂度O(n),空间复杂度O(n)：多了一个哈希表的开销

if __name__ == '__main__':
    # solution = Solution1()
    solution = Solution2()
    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))
