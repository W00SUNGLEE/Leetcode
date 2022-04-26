from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = defaultdict()
        for char in s:
            if char not in dic.keys():
                dic[char] = 1
            else:
                dic[char] += 1
            
        for key, value in dic.items():
            if value == 1:
                return s.index(key)
            
        return -1
                
            
            