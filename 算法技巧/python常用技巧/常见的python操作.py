### TODO：数字运算
a, b = 5, 2
## 除法
res = a / b # 2.5
## 地板除（向下取整）
res = a // b # 2
## 取余
res = a % b # 1

## =====切片(适用于数组、元组、字符串)===== ##
# 以数组为例，注意切片格式为[start:end:step]。其中start和end注意是左闭右开（跟range一样），step默认为1
lst = [1,2,3,4]
# 以下意思等同，都代表取整个列表。
lst = lst[:] = lst[::] = lst[0:]
# 以下会省略最后一个，相当于pop()
lst[0:-1]

### ========== TODO:列表的常见使用方式 ========== ###
## ========== 一维列表 ========== ##
## 声明空列表
lst = []
lst = list()
## 新建定值列表
lst = [1,2,3,4]
## 新建递增列表
len = 100
lst = list(range(len))
# 采用列表推导式
lst = [i for i in range(len)]
## 新建递减列表
lst = list(reversed(range(len)))
## 新建定长同值列表
lst = [0] * len
# 应用：新建布尔列表
lst = [True] * len

## 本地修改lst，不返回（返回None）的方法，注意都是.function()的形式
# 列表后追加
lst.append(5)
# 删除某个值（从左往右遇到的第一个）
lst.remove(1)
# 删除某个位置的值
del lst[1]
# 插入（位置，值）
lst.insert(-1, 6)
# 排序（从小到大）
lst.sort()
# 反序（从大到小）
lst.reverse()

## 不修改lst，返回值的方法
# 访问某个元素
item = lst[1]
# 返回某个值的计数
count = lst.count(1)
# 找到某个值的索引，并返回索引
index = lst.index(2)
# 排序，并返回排序后列表
sorted_list = sorted(lst)
# 计算长度
length = len(lst)
# 最大/最小值
max = max(lst)
min = min(lst)
# 求和
sum = sum(lst)

## 修改lst，也返回值的方法
# 从后面删除，并返回删除的值
pop = lst.pop()
# 删除某个位置的值
item = lst.pop(1)

## ========== 二维列表 ========== ##
## 新建空二维列表
matrix = [[]]
## 新建定值二维列表
matrix = [[1,2,3], [4,5,6], [7,8,9]]
## 新建m行n列的列表（采用列表推导式）
m,n = 2,3
# 生成0矩阵
matrix = [[0 for i in range(m)] for j in range(n)]
# 生成每个元素索引之和的矩阵
matrix = [[i+j for i in range(m)] for j in range(n)]
## 操作二维列表
## 修改元素
matrix[0][0] = 1 # 单个
matrix[0] = [1,2,3] # 一行
## 添加行/列
# 添加行
new_line = [1,2,3]
matrix.append(new_line)
# 添加列
for line in matrix:
    line.append(0)
## 删除行/列
del matrix[0]  # 删除第一行
for line in matrix:
    del line[0]  # 删除第一列
## 获取行/列数
row_num = len(matrix)  # 获取行
col_num = len(matrix[0]) # 获取列（所有行都具有相同的列数）
## TODO:转置(列表推导式)
transpose_matrix = [[row[i] for row in matrix] for i in range(col_num)]

### ==========TODO:字典(MAP)的常见使用方式 ========== ###
## 声明简单字典
dct = {}
dct = dict()
## 初始化字典
dct = {'A':1, 'B':2, 'C':3}
## 取单值
# 用得少，没有的key会报错
a = dct['A']
# 用得多，字典中没出现的key：返回None,也可以指定显示。出现过的正常显示。注意并没有修改原来的字典
a = dct.get('A') # 1
a = dct.get('A', 3) # 1(因为A存在，返回真实的)
d = dct.get('D') # 默认：None
d = dct.get('D', "没有这个key") # 没有这个key
## 遍历字典
for key in dct.keys():
    value = dct[key]
for value in dct.values():
    print(value)
# 两个值都取（常用）
for key, value in dct.items():
    print(key, value)
## 修改键值
dct['A'] = 4
## 添加键值
# 一般方式
dct['D'] = 1
# 迭代方式
dct['D'] = dct.get('D', 0) + 1  # 如果D新创建，那么dct.get('D', 0)返回0，如果D已有，就增加值
# 常用：统计频率
dict1 = {}
list1 = ['￥', '￥', '￥', '$', '$', '$', '$', '$']
for i in list1:
    dict1[i] = dict1.get(i, 0) + 1
print(dict1)
## 删除键值
del dct['A']
## 字典长度
length = len(dct)
## 清空字典
dct.clear()
## 两个字典，一个更新另一个【注意：已有的键值，后者覆盖前者；没有的键值会新添加】
dct1 = {'A':1, 'B':2, 'C':3}
dct2 = {'A':2, 'B':3, 'D':4}
dct1.update(dct2)
print(dct1)  # {'A':2, 'B':3, 'C':3, 'D':4}

### ==========TODO:字符串的常见使用方式 ========== ###
## 声明字符串
str = ''
str = ""
## 索引取值（无法直接使用索引修改）
str = 'abcdefg'
s1 = str[0]  # a
## 字符串的拼接（增加）
# 一般的拼接（加号拼接）
str = str + 'hijklmn'
# 带有分隔符的连接
str = "|".join(str)  # 分隔符为"|"，将会在str的每个字符间起作用
## 字符串的删除
# 使用切片（与列表、元组相同）略

## 字符串的修改（重要）
# 由于字符串是不可变类型，不能通过索引直接更改
nums = 1
str.replace('a','b',nums)  # 将'a'替换为'b'，并根据修改次数nums确定
## 查找字符索引
# index：找到返回索引，找不到返回error
str.index('a')
# find：找到返回索引，找不到返回-1
str.find('a')

## 统计长度
length = len(str)
## 字符串排序（实际上是字母对应的ASCII数字的排序）
str_list = sorted(str)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']需要还原为字符串
str = "".join(str_list)
## 字符串分割为字符子列表
str_list = str.split() # 注意分隔默认值为""，空格（不是空字符）
str_list = str.split('b')  # 按照b进行分割：['a', 'cdefg']
## 删除字符串前后的空格（其它字符）
# 删除空格（默认为空格）
str.strip()
# 删除其它字符，需要进行指定
str.strip('%')

## 其它操作
# 首字母大写
str.capitalize()
# 全部大写
str.upper()
# 全部小写
str.lower()
# 交换大小写顺序
str.swapcase()
# 元素（子序列）计数
str.count('a')
str.count('ab')  # 1

### ============= TODO: collections 库的用法 ====================== ###
# Leetcode中内置了collections，可以直接使用。
# 声明：
import collections
## 双向队列deque
deque = collections.deque()
# 队列加入元素
deque.append(lst)
## 方法
# 移除头部/尾部队列
deque.popleft()
deque.pop()

## 计数器Counter()
my_list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
counter = collections.Counter(my_list)
count_apples = counter['apple']  # 返回 'apple' 出现的次数
counter.update(['orange', 'orange'])  # 增加 'orange' 的计数
counter.subtract(['orange'])  # 减少 'orange' 的计数
most_common = counter.most_common(1)  # 返回出现次数最多的元素及其计数

counter1 = collections.Counter(['a', 'b', 'a'])
counter2 = collections.Counter(['a', 'a', 'a'])
are_equal = (counter1 == counter2)  # 比较两个 Counter 对象



