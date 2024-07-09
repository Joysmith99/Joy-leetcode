# 创建一个原始列表
original_list = [1, 2, [3, 4]]
# 使用 copy() 方法进行浅复制
shallow_copy = original_list.copy()
# 修改浅复制的内容
shallow_copy[0] = 100
shallow_copy[2][0] = 300
# 打印原始列表和浅复制
# 原始列表： [1, 2, [300, 4]]
# 浅复制： [100, 2, [300, 4]]
print("原始列表：", original_list, id(original_list))
print("浅复制：", shallow_copy, id(shallow_copy))

# 其它的拷贝方式
copy1 = original_list[:]
copy2 = list(original_list)
print(id(copy1), id(copy2))
# 分析原因：python对于列表的浅拷贝，只会针对数字（字符串）等简单数据类型（不可变类型）进行对象创建，而对于嵌套列表之类可递归的结构，只会复制引用而非列表本身
# 因此，对于浅拷贝的嵌套列表，更改列表也会影响原始列表的值