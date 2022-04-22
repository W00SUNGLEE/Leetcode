class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0 
        dic = {}
        solution = 0
        
        for end, char in enumerate(s):
            if char in dic and start <= dic[char]:
                start = dic[char] + 1
            else:
                solution = max(solution, end - start + 1)
            dic[char] = end
            
        return solution
