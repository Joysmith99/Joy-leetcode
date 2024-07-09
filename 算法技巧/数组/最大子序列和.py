from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 使用双指针
        p1 = 0
        p2 = len(nums)
        res = 0

        # 当p1和p2相遇停止
        while p1 >= p2:
            # 最大子数组一定出现在p1和p2都为正数的区间内
            while nums[p1] <= 0:
                p1 += 1
            while nums[p2] <= 0:
                p2 -= 1 
            curr_res = sum(nums[p1:p2])
            p1 += 1
            p2 -= 1

            res = max(curr_res, res)
            
        return res
    
if __name__ == '__main__':
    solution = Solution()
    lst = [1,-1,2,3]
    print(sum(lst[0:2]))