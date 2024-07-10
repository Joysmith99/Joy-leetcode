# 给你一个字符串 s，一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
# 注意：
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#######################################################################################################################

## TODO:这道题是进行字符串的匹配，并不是求和，因此采用滑动窗口
# 该题变量很多，需要理清楚哪些是必要的。
# windows：窗口字符计数，need：目标字符计数，pl和pr代表窗口的左右指针，valid代表字符串的个数的命中情况，只有valid == len(need)才会推进缩减。
# start和length都是所选子串的定位符
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        # 用于窗口值计数
        window = Counter()
        # 用于t的计数
        need = Counter(t)
        # 定义窗口的左右指针
        pl, pr = 0, 0
        # 定义每个字符个数是否满足条件
        valid = 0
        # 最小覆盖字串的起始值与对应长度
        start, length = 0, float('inf')

        # 使用滑动窗口
        # 判断窗口需要扩张的条件
        while pr < len(s): # pr最多取n-1
            # 字符移入窗口
            c = s[pr]
            pr += 1
            # 进行逻辑的更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧是否需要缩减的条件：只有找到了符合条件的字串才开始缩减
            while valid == len(need):

                # 缩减时，要先判断现在找到的是不是最优，并更新
                if pr - pl < length:
                    # 更新start和length，说明找到了更短的子串
                    start = pl
                    length = pr - pl
                # 字符弹出窗口
                d = s[pl]
                pl += 1
                # 进行逻辑的更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                
        return "" if length == float('inf') else s[start:start+length]