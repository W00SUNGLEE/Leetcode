class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        else: # n > 1
            dp = [nums[0], nums[0]]
            dp2 =[0, nums[1]]
         
            for i in range(2, len(nums)):
                dp.append(max(dp[i-1], dp[i-2]+nums[i]))
                dp2.append(max(dp2[i-1], dp2[i-2]+nums[i]))
                
            return max(dp[n-2], dp2[n-1]) 