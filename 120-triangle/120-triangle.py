import sys

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float("inf") for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        
        dp[0][0] = triangle[0][0]
        
        for i in range(len(triangle)-1):
            for j in range(len(triangle[i])):
                dp[i+1][j] = min(dp[i+1][j], triangle[i+1][j] + dp[i][j])
                dp[i+1][j+1] = min(dp[i+1][j+1], triangle[i+1][j+1] + dp[i][j])
                
        return min(dp[len(dp)-1])