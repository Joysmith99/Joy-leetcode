class Solution():
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = list(set(nums))
        count = 1
        for i in range(len(new_nums)-1):
            
            if (new_nums[i] + 1 == new_nums[i+1]):
                count = count + 1
            else:
                continue
        return count
    
if __name__ == '__main__':
    solution = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(solution.longestConsecutive(nums))
