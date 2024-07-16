# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间
# 需要注意区间并未按照左端点从小到大排列
#################################################################################

# 思路很简单，没有什么技巧

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 按照起始点start进行排序
        intervals.sort(key=lambda x: x[0])
        # 定义结果列表
        res = []
        # 先将第一个列表放进去
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            current = intervals[i]
            # 调用最后一个元素
            last = res[-1]
            # 比较current的start和last的end的大小关系
            # 如果current[0]小于等于last[1]，说明区间是包含的
            if current[0] <= last[1]:
                last[1] = max(current[1], last[1])
            # 如果不包含，就增加新的list
            else:
                res.append(current)
        
        return res