class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]
        
        if n < 3:
            return dp[n]
        
        else:
            for i in range(3,n):
                dp.append(dp[i-2] + dp[i-1])
            return dp[n-2] + dp[n-1]