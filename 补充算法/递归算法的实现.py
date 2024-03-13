# 使用递归方法，求一个数列在给定区间[L,R]的最大值
class Solution1(object):
    def findmax(self, array, left, right):

        n = len(array)
        if left == right:
            return array[left]
        else:
            # 找到中点
            mid = left + ((right-left)>>1)
            leftmax = self.findmax(array, left, mid)
            rightmax = self.findmax(array, mid+1, right)
            return max(leftmax, rightmax)
        
# 实现归并排序:
# 递归法+归并融合
class Solution2(object):
    # 递归法
    def mergesort(self, array, left, right):
        if left == right:
            return
        else:
            mid = left + ((right-left)>>1)
            self.mergesort(array, left, mid)
            self.mergesort(array, mid+1, right)
            self.merge(array, left, mid, right)
    # 归并融合排序的实现
    def merge(self, array, left, mid, right):
        # 生成临时数组
        help = list(right-left+1)
        i = 0
        point1 = left
        point2 = mid+1
        # point1和point2都没有越界时
        while ((point1 <= mid) & (point2 <= right)):
            if array[point1] <= array[point2]:
                help[i] = array[point1]
                i += 1
                point1 += 1
            else:
                help[i] = array[point2]
                i += 1
                point2 += 1
        # point1或者point2越界时
        while point1 <= mid:
            help[i] = array[point1]
            i += 1
            point1 += 1
        while point2 <= right:
            help[i] = array[point2]
            i += 1
            point2 += 1

        array[left:right] = help
        return array
        
# 实现小和问题：
# BF方法：O(n2)
class Solution3(object):
    def small_sum1(self, array):
        length = len(array)
        sum_list = []
        for i in range(1, length):
            point = i-1
            count = 0
            while point >= 0:
                if array[i] > array[point]:
                    count += array[point]
                    point = point-1
                else:
                    point = point-1
            sum_list.append(count)
        small = sum(sum_list)

        return small
    # 使用归并法O(nlogn)
    # def small_sum2(self, array):

if __name__ == '__main__':

    # solution1 = Solution1()
    solution3 = Solution3()
    array1 = [1,3,5,2,4,6]
    small = solution3.small_sum1(array1)
    print(small)
    