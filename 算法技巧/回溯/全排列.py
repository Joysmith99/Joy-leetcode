class Solution:

    def __init__(self):
        # 定义全局输出变量
        self.res = []
        
    # 主函数，输入一组不重复的数字，返回它们的全排列
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 定义路径
        track = []
        # 定义已经使用的值，避免重复使用，实质上我们是通过跟踪used_list状态间接实现选择列表的删改的
        used_list = [False] * (len(nums)+1)
        # 回溯主函数
        self.backtrack(track, nums, used_list)

        return self.res

    def backtrack(self, track, nums, used_list):
        # 出口条件（前序位置）：当路径和选择列表相等时，说明已经通过回溯找到
        if len(track) == len(nums):
        # 用track.copy()的原因是复制列表中的元素到一个新的对象（仅针对没有嵌套的列表），否则就会输出空值了
            # self.res.append(track.copy())
            #以下使用切片，就是不能直接传track
            # self.res.append(track[:])
            # self.res.append(list(track))
            return None
        # 不相等时，需要继续回溯
        for i in range(len(nums)):
            # 作选择
            # nums中已经选择的点需要步过
            if used_list[i]:
                continue
            # 没有做选择的，添加进track
            track.append(nums[i])
            used_list[i] =True

            self.backtrack(track, nums, used_list)
            # 撤销
            track.pop()
            used_list[i] = False