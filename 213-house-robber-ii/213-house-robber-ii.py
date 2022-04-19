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
        
        
        
        
        
        
        
        
        
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        else: # n > 1
            dp = [[nums[0], True]]
            
            if nums[0] > nums[1]:
                dp.append([nums[0], True])
                       
            else: # nums[0] <= nums[1]:
                dp.append([nums[1], False])
            
            if n == 2:
                return dp[1][0]
         
            else: # n > 2
                for i in range(2, len(nums)):
                    if dp[i-1][0] >= dp[i-2][0]+nums[i]:
                        dp.append([dp[i-1][0], dp[i-1][1]])
                  
                    else: # dp[i-1][0] < dp[i-2][0]+nums[i]
                        dp.append([dp[i-2][0]+nums[i], dp[i-2][1]])
                
                
                print(dp)
                if dp[n-1][1] == True:
                    return max(dp[n-2][0], dp[n-1][0]-nums[0])
                else: # dp[n-1][1] == False:
                    return dp[n-1][0]
        """