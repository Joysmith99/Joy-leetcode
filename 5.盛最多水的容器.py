# BF方法：超时
class Solution1(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 定义两个指针p1和p2
        p1 = p2 = 0
        # 定义高度列表的长度
        length = len(height)
        # 定义储水列表
        water_container = []
        # 遍历两次计算
        for i in range(length):
            for j in range(i+1, length):
                # 计算每个时刻的储水值
                water = min(height[i], height[j]) * (j-i)
                water_container.append(water)
        
        return max(water_container)
    
class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 定义左右指针p1和p2
        pl = 0 
        pr = len(height)-1
        # 定义储水列表
        water_container = []
        # 收敛条件pl = pr
        while pl != pr:
            # 每次移动左右指针中数字最小的
            if height[pl] >= height[pr]:
                water_container.append(height[pr] * (pr-pl))
                pr = pr - 1
            elif height[pl] <= height[pr]:
                water_container.append(height[pl] * (pr-pl))
                pl = pl + 1
        
        return max(water_container)
    
if __name__ == '__main__':
    # solution = Solution1()
    solution = Solution2()
    height = [3, 2, 4, 5]
    print(solution.maxArea(height))