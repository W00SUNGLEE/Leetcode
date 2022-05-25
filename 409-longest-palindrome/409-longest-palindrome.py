from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        answer = 0

        dic = defaultdict(int)
        
        for i in range(len(s)):
            dic[s[i]] += 1

        odd = False
        for value in dic.values():
            if value % 2 == 0: #even
                answer += value
            
            else: #odd
                answer += value-1
                odd = True
        
        if odd:
            return answer + 1
        else: #even
            return answer