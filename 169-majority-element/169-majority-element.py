from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = defaultdict(int)
        
        for i, element in enumerate(nums):
            dic[element] += 1
        
        majority = len(nums)/2
        
        for element, count in dic.items():
            if count > majority:
                return element
        