class Solution:
    def arraySign(self, nums: List[int]) -> int:
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            
            elif nums[i] < 0:
                cnt += 1
                
        if cnt%2 == 0:
            return 1
        
        else: #cnt%2 == 1
            return -1