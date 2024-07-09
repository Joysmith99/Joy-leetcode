## 求位运算的最右侧的低位1的方法，如果给定num=5，则right_one=1
# num = 5
# right_one = num & (~num + 1)
# print(right_one)

## 求数组在给定范围[L, R]的中点，不要写为mid = (L + R) / 2，可能会溢出:
L = 1
R = 5
mid1 = L + (R-L) / 2
# 更简化的方式：使用右移运算符来代替除以2（左乘，右除）
mid2 = L + ((R-L)>>1)
print(mid1, mid2)

##