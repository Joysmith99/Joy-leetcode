## 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
## 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
#######################################################################################################

# TODO:使用异或操作。
# 事实上这道题可以拓展，不一定是1个只出现一次的数字，可以找到1个出现奇数次的数字
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 使用异或操作即可，因为a^a=0, a^0=a
        res = 0
        for num in nums:
            res ^= num
        return res
    
if __name__ == '__main__':

    nums = [1,1,2,2,3,3,4]
    solution = Solution()
    res = solution.singleNumber(nums)
    print(f"==>> res: {res}")
    