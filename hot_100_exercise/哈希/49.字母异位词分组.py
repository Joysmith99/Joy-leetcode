class Solution():
    def groupAnagrams(self, strs):
        hashtable = {}
        for s in strs:
            s_ = "".join(sorted(s))
            if s_ not in hashtable:
                hashtable[s_] = [s]
            else:
                hashtable[s_].append(s)
        return list(hashtable.values())
    
if __name__ == '__main__':
    solution = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(solution.groupAnagrams(strs))