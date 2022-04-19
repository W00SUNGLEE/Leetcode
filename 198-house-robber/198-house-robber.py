class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        else: # n > 1
            dp = [nums[0], max(nums[0], nums[1])]
            
            if n == 2:
                return dp[1]
         
            else: # n > 2
                for i in range(2, len(nums)):
                    dp.append(max(dp[i-1], dp[i-2]+nums[i]))
                print(dp)
                return dp[n-1] 
            
                   