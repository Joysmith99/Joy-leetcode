


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0

        for i in range(1, len(height)-1):
            
            left, right = 0, len(height)-1
            left_max, right_max = 0, 0

            while left < i: 
                if height[left] > height[i]:
                    left_max = max(left_max, height[left])
                left+=1
            
            while i < right: 
                if height[right] > height[i]:
                    right_max = max(right_max, height[right])
                right-=1
            
            if left_max == 0 or right_max == 0:
                continue
            else:
                res += min(left_max, right_max) - height[i]
        
        return res
    
# 如何仅使用两个双指针呢？这样时间复杂度就大大降低了
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 定义：需要记录的值有四个：左右指针的位置，以及左右指针各自左右的最大值
        left ,right = 0, len(height)-1
        left_max, right_max = 0, 0
        # 定义结果
        res = 0

        # 左右指针问题的停止条件
        while left < right:
            # 先计算左右最大值
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            # 根据当前位置的高度来进行计算，注意此时的height[]一定会小于等于对应的max值，因为上面先计算了最大值
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
            
        return res
          