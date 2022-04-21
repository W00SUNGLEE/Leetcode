from collections import defaultdict

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        dict1 = defaultdict(int)
        dict2 = defaultdict(int)
        
        cnt = 0
        for i in range(len(s1)):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1
            if s1[i] != s2[i]:
                cnt += 1

        if cnt == 0 or cnt == 2:
            return dict1 == dict2
        
        else:
            return False