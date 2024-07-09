## 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋ 的元素。
## 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
##############################################################################################

# TODO: 思路1：使用一个【哈希表】存储，然后找到最大值，一定是多数元素
class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 初始化字典用于计数
        num_counts = {}

        # 遍历列表并计数
        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        # 初始化最大值和对应的键
        max_value = 0
        max_key = None

        # 找出具有最大value的key
        for key, value in num_counts.items():
            if value > max_value:
                max_value = value
                max_key = key

        return max_key
    
# TODO: 思路2：正负电荷中和问题
# 需要找到超过一半的元素，那么就把超过一半的看作正样本，不超过一半的看作负样本，正负相抵。
# 当运行到最后，count一定为正或者为负，此时得到的就是target值
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 定义计数器
        count = 0
        # 定义找到的目标值
        target = 0

        for num in nums:
            # count为0时，说明正负中和,target就应该换了
            if count == 0:
                target = num
                count += 1
            # 当下一轮target还是为num时，count加一，反之减一
            elif target == num:
                count += 1
            else:
                count -= 1

        return target

if __name__ == '__main__':
    nums = [1, 2, 2]
    solution1 = Solution1()
    solution2 = Solution2()
    res1 = solution1.majorityElement(nums)
    res2 = solution2.majorityElement(nums)
    print(f"==>> res: {res1, res2}")
    