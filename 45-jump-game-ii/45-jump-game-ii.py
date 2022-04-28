class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2 or nums[0] >= len(nums)-1:
            return 1
        dp = [[0, 0] for _ in range(len(nums))]
        
        for i in range(1, nums[0]+1):
            dp[i][0] = nums[0]
            dp[i][1] = 1
        
        
        for i in range(1, len(nums)):
            if i <= dp[i][0]:
                if dp[len(nums)-1][1] > 0:
                    print(dp)
                    return dp[len(nums)-1][1]
                
                if i+nums[i] > dp[i][0]:
                    print(i+nums[i], len(nums), i+nums[i] > len(nums))
                    if i+nums[i]+1 > len(nums):
                        rangeMax = len(nums)
                    else:
                        rangeMax = i+nums[i]+1
                    print(rangeMax)
                    for j in reversed(range(i+1, rangeMax)):
                        dp[j][0] = i+nums[i]
                        if dp[j][1] == 0:
                            dp[j][1] = dp[i][1]+1      
                
                """
                if i+nums[i] > dp[i][0]:
                    dp.append([i+nums[i], dp[i-1][1]+1])
                else: #i+nums[i] <= dp[i-1]
                    dp.append([dp[i-1][0], dp[i-1][1]])
                """
            else:
                return -1
            
        return 0